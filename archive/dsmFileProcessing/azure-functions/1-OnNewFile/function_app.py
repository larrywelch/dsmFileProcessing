import string
import io
import logging
import azure.functions as func

from config import settings
from dsmAzureLib.emailUtil import emailUtil

from dsmFileProcessorLib import AgriStatConfig
from dsmFileProcessorLib import AgriStatFileProcessor
from dsmFileProcessorLib import PoultyPlanFileProcessor

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

    virtualFolderName = inputblob.name.split('/')[1]
    
    # Were going to use a simple means for determining which processor to call.  As we get more we can expand    
    if (inputblob.name.upper().endswith(".ZIP")):
        # Use agristats
        config : AgriStatConfig = AgriStatConfig.builder() \
            .with_azure_storage_elements(settings['blobConnStr'], settings['inContainerName'], settings['outContainerName'], virtualFolderName, settings['finalResultsFileName']) \
            .with_sql_config_elements(settings['sql_user_name'], settings['sql_user_pw'], settings['sql_server_url'], settings['sql_server_port'], settings['odbc-driver'], settings['sql_server_db_name'], settings['sql_server_table_name']) \
            .build()
        processor = AgriStatFileProcessor(config)

    elif (inputblob.name.upper().endswith(".PDF")):
        # use Poulty Plan
        processor = PoultyPlanFileProcessor()
    else:
        # Input file isn't a zip file, nothing to do
        processor = None
        logging.info("No processor available for the file.")
        # Set the exception so that the code below will respond and generate a proper email.
        ex = Exception("No Processor Available For The File.")
    
    # Let's process the file
    if (processor != None):
        ex = processor.onNewFile(io.BytesIO(inputblob.read()))
        
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
 

