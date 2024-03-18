import string
import io

import azure.functions as func
import logging

from config import settings
from dsmFileProcessorLib.AgriStatsFileProcessor import AgriStatsFileProcessor
from dsmFileProcessorLib.PoultryPlanFileProcessor import PoultryPlanFileProcessor
from dsmAzureLib.emailUtil import emailUtil

app = func.FunctionApp()

def sendEmail(subject: string, message: string) :
    # Get environment variables
    emailNotificationEnabled = settings['email-notification-enabled']
    if (emailNotificationEnabled != True) :
        print('[sendEmail] email notification is disabled, no email sent.')
        return
    
    print('[sendEmail] sending email...')
        
    emailSvcConnStr = settings['email-notification-svc-conn-str']
    emailSvcSenderAddress = settings['email-notification-sender-address']
    emailSvcSendToList = settings['email-notification-send-to-list']
  
    assert emailSvcConnStr and emailSvcSenderAddress and emailSvcSendToList
  
    # Create the email notification object
    emn = emailUtil(emailSvcConnStr, emailSvcSenderAddress)
    emn.sendEmail(subject, message, emailSvcSendToList)
  
    print('[sendEmail] complete!')
 
# NOTE: Make sure to change the path to reflect the production container
@app.blob_trigger(arg_name="inputblob", 
                    path="sample-files-to-be-processed",
                    connection="storageContainerConnStr") 

# NOTE: Make sure to change the queue_name to reflect the production queue
@app.service_bus_queue_output(arg_name='outServiceBusMsg', 
                              connection='AzureServiceBusConnectionString', 
                              queue_name='sample-file-ready-for-processing')

def OnNewFile(inputblob: func.InputStream, outServiceBusMsg: func.Out[str]):
    
    nl = '\n'
    logging.info(f"New zip file ready for processing {nl}"
                 f"Name:            {inputblob.name}{nl}"
                )
    
    blobConnStr = settings["storageContainerConnStr"]
    outContainerName = settings["outContainerName"]
    virtualFolderName = inputblob.name.split('/')[1]
    
    # Were going to use a simple means for determining which processor to call.  As we get more we can expand    
    if (inputblob.name.upper().endswith(".ZIP")):
        # Use agristats
        processor = AgriStatsFileProcessor()

    elif (inputblob.name.upper().endswith(".PDF")):
        # use Poulty Plan
        processor = PoultryPlanFileProcessor()
    else:
        # Input file isn't a zip file, nothing to do
        processor = None
        logging.info("No processor available for the file.")
        # Set the exception so that the code below will respond and generate a proper email.
        ex = Exception("No Processor Available For The File.")
    
    # Let's process the file
    if (processor != None):
        ex = processor.onNewFile(io.BytesIO(inputblob.read()), blobConnStr, outContainerName, virtualFolderName)
        
    if (ex == None):
        # Complete - signal the service bus using the virtual folder name (where the zip file was extracted to)
        outServiceBusMsg.set(virtualFolderName)
        sendEmail(
            f"A New AgriStat Zip File ({virtualFolderName}) is available for processing", 
            f"{virtualFolderName} is available and will be processed soon.")
    else:
        sendEmail(
            f"A New AgriStat Zip File ({virtualFolderName}) failed to process", 
            f"{virtualFolderName} failed with the following exception: {nl} {ex}")

    # Log the final message
    logging.info("Complete")
 

