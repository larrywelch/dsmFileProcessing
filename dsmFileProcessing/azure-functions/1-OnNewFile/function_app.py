import string
import zipfile
import io
from azure.storage.blob import BlobClient

import azure.functions as func
import logging
from dsmAzureLib.emailUtil import emailUtil
from config import settings

app = func.FunctionApp()

def processTheFile(inputblob, virtualFolderName) :
    blobConnStr = settings["storageContainerConnStr"]
    outContainerName = settings["outContainerName"]

    try:
        
        with zipfile.ZipFile(io.BytesIO(inputblob.read()) , 'r') as zip_ref:
            filelist = list(filter(lambda f: f.filename.upper().endswith(".XLSX"), zip_ref.infolist()))
            logging.info("Processing content of the zip file")
            for file in filelist:
                with zip_ref.open(file.filename, 'r') as zip:
                    logging.info(f"File Name: {zip.name} \n")
                    # File names are prefixed with #### where ## = Year and ## = Week of the Year
                    # Chelsea's scripts expect the ###_ to be omitted - we'll do that here
                    outFileName = zip.name[zip.name.upper().index("WEEK"):]
                        
                    # Create a path using a virtual folder structure
                    path = "{z}/{f}"
                    p = path.format(z=virtualFolderName, f=outFileName)

                    # Create a blob client and upload the file
                    blobClient = BlobClient.from_connection_string(conn_str=blobConnStr, container_name=outContainerName, blob_name=p)
                    blobClient.upload_blob(zip.read(), overwrite = True)

        return None

    except Exception as ex:
        return ex

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
 
     
@app.blob_trigger(arg_name="inputblob", path="sample-files-to-be-processed",
                               connection="storageContainerConnStr") 
@app.service_bus_queue_output(arg_name='outServiceBusMsg', connection='AzureServiceBusConnectionString', queue_name='sample-file-ready-for-processing')

def OnNewFile(inputblob: func.InputStream, outServiceBusMsg: func.Out[str]):
    
    logging.info(f"New zip file ready for processing \n"
                 f"Name:            {inputblob.name}\n"
                )
    
    # Create a ZipFile using the bytes read from the inputblob
    if inputblob.name.upper().endswith(".ZIP") :
        virtualFolderName = inputblob.name.split('/')[1]
        result = processTheFile(inputblob, virtualFolderName)
        if (result == None) :
            # Complete - signal the service bus using the virtual folder name (where the zip file was extracted to)
            outServiceBusMsg.set(virtualFolderName)
            sendEmail(
                f"A New AgriStat Zip File ({virtualFolderName}) is available for processing", 
                f"{virtualFolderName} is available and will be processed soon.")
        else:
            
            sendEmail(
                f"A New AgriStat Zip File ({virtualFolderName}) failed to process", 
                f"{virtualFolderName} failed with the following exception: {result}")
            
        logging.info("Complete")
    else:
        # Input file isn't a zip file, nothing to do
        logging.info("File is not a zip file, no processing necessary")
        
        sendEmail(
             "A New AgriStat File ({virtualFolderName}) was detected, but it's not a zip file", 
            f"A New AgriStat File ({virtualFolderName}) was detected, but it's not a zip file and won't be processed.")

