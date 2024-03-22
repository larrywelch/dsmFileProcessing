'''
    An Azure Function App for Processing DSM Files
    
    There are 3 functions within this app.  They are:
    1. OnProcessSourceFile - executes when a new file is added to a storage container, when complete, signals a service bus 
    2. OnProcessExtractedFiles - executes when the service bus is signaled in OnProcessSourceFile, signals a service bus when complete
    3. OnProcessFinalResults - executes when the service bus is signaled in OnProcessExtractedFiles

    The functions use handler code that is located in the dsmPackage.OnHandlers folder.  Each handler
    is named the same as the function with a Handler suffix.
'''

import azure.functions as func
import logging

# Import the function handlers
import dsmPackage.OnHandlers as OnHandlers

# Import the configuration
from configuration import settings

# Import email notification
from sendEmailNotification import sendEmail

# Create our function app to be used by all the functions
app = func.FunctionApp()

'''
    OnProcessSoureFile:
        - A Blob Triggered Function - executes when a new file is added to the blob storage container.
        - extracts the contents of the source file into another storeage container
        - Signals a service bus when finished, causing OnFileReadyForProcessing to execute.
'''
# NOTE: Make sure to change the path to reflect the production container
@app.blob_trigger(
    arg_name="sourceFileBlob", 
    path="dsm-source-files",
    connection="AZURE_STORAGE_CONTAINER_CONN_STR") 

# NOTE: Make sure to change the queue_name to reflect the production queue
@app.service_bus_queue_output(
    arg_name='sbOutMsgProcessExtractedFiles', 
    connection='AZURE_SERVICE_BUS_CONN_STR', 
    queue_name='dsm-process-extracted-files')

def OnProcessSourceFile(sourceFileBlob: func.InputStream, sbOutMsgProcessExtractedFiles: func.Out[str]):
    # name=container/filename or zip-files/06-02-2023.zip
    # fileName = 06-02-2023.zip - this is then used as the virtual folder where the zip file is extracted
    fileName = sourceFileBlob.name.split('/')[1]
    logging.info('[OnProcessSourceFile] entered, processing the source file...')
    logging.info(f" Name:{sourceFileBlob.name}")
    
    # Call the handler
    ex = OnHandlers.OnProcessSourceFileHandler(sourceFileBlob, settings)
    if (ex == None):
        # Set the service bus message to the name of the input file name
        sbOutMsgProcessExtractedFiles.set(fileName)
        
        # Send an email
        sendEmail(
            f"A New Source File ({fileName}) is available for processing", 
            f"{fileName} is available and will be processed soon.")        
    else:
        # There was an exception
        logging.warning(repr(ex))
        
        # Send an email
        sendEmail(
            f"A New Source File ({fileName}) failed to process", 
            f"{fileName} failed with the following exception: {repr(ex)}")
            
    
'''
    OnProcessExtractedFiles - executes when the service bus is signaled from OnNewFile

    Signals a service bus when finished, causing OnFinalResultsReadyForProcessing to execute.
'''

@app.service_bus_queue_trigger(
    arg_name="sbInMsgProcessExtractedFiles", 
    queue_name="dsm-process-extracted-files",
    connection="AZURE_SERVICE_BUS_CONN_STR") 

@app.service_bus_queue_output(
    arg_name='sbOutMsgProcessFinalResults', 
    connection='AZURE_SERVICE_BUS_CONN_STR', 
    queue_name='dsm-process-final-results')

def OnProcessExtractedFiles(sbInMsgProcessExtractedFiles: func.ServiceBusMessage, sbOutMsgProcessFinalResults: func.Out[str]):
    sourceFileName = sbInMsgProcessExtractedFiles.get_body().decode('utf-8')
    logging.info('[OnProcessExtractedFiles] entered, processing the extracted files...')
    logging.info(f" Source File Name Folder:{sourceFileName}")
    
    # Call the handler
    ex = OnHandlers.OnProcessExtractedFilesHandler(sourceFileName, settings)
    if (ex == None):
        # Signal the service bus
        sbOutMsgProcessFinalResults.set(sourceFileName)
        
        # Send an email
        sendEmail(
            f"Source File ({sourceFileName}) has been extracted", 
            f"{sourceFileName} was extracted.  It's contents will be processed into final results soon.")   
    else:
        # There was an exception
        logging.warning(repr(ex))
    
        # Send an email
        sendEmail(
            f"Source File ({sourceFileName}) failed extraction", 
            f"{sourceFileName} failed extraction with the following exception: {repr(ex)}")
    
'''
    OnProcessFinalResults - executes when the service bus is signaled from OnFileReadyForProcessing
    This is the final step of the file processing process.
'''

@app.service_bus_queue_trigger(
    arg_name="sbInMsgProcessFinalResults", 
    queue_name="dsm-process-final-results",
    connection="AZURE_SERVICE_BUS_CONN_STR") 

def OnProcessFinalResults(sbInMsgProcessFinalResults: func.ServiceBusMessage):
    sourceFileName = sbInMsgProcessFinalResults.get_body().decode('utf-8')
    logging.info('[OnProcessFinalResults] entered, processing the extracted files...')
    logging.info(f" Source File Name Folder:{sourceFileName}")
    
    # Call the handler
    ex = OnHandlers.OnProcessFinalResultsHandler(sourceFileName, settings)
    if (ex == None) :
        logging.info(f'Process is complete for Source File: {sourceFileName}')
        
        # Send an email
        sendEmail(
            f"Source File ({sourceFileName}) has been fully processed", 
            f"{sourceFileName} has been fully processed and the results have stored in SQL.")           
    else:
        # There was an exception
        logging.warning(repr(ex))
        
        # Send an email
        sendEmail(
            f"Source File ({sourceFileName}) failed final processing", 
            f"{sourceFileName} failed final processing with the following exception: {repr(ex)}")        


