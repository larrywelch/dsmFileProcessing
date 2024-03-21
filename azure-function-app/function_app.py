'''
    An Azure Function App for Processing DSM Files
    
    There are 3 functions within this app.  They are:
    1. OnProcessSourceFile - executes when a new file is added to a storage container, when complete, signals a service bus 
    2. OnExtractedFilesReady - executes when the service bus is signaled in OnNewFile, signals a service bus when complete
    3. OnFinalResultsReady - executes when the service bus is signaled in OnFileReadyForProcessing

    The functions use handler code that is located in the src folder.  Each handler
    is named the same as the function with a Handler suffix.
'''

import azure.functions as func
import logging

# Import the function handlers
import dsmPackage.OnHandlers as OnHandlers

# Import the configuration
from configuration import settings

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
    connection="AzureStorageContainerConnStr") 

# NOTE: Make sure to change the queue_name to reflect the production queue
@app.service_bus_queue_output(
    arg_name='sbOutMsgProcessExtractedFiles', 
    connection='AzureServiceBusConnStr', 
    queue_name='dsm-process-extracted-files')

def OnProcessSourceFile(sourceFileBlob: func.InputStream, sbOutMsgProcessExtractedFiles: func.Out[str]):
    # name=container/filename or zip-files/06-02-2023.zip
    # fileName = 06-02-2023.zip - this is then used as the virtual folder where the zip file is extracted
    fileName = sourceFileBlob.name.split('/')[1]
    logging.info('[OnProcessSourceFile] entered, processing the source file...')
    logging.info(f" Name:{sourceFileBlob.name}")
    
    # Call the handler
    if (OnHandlers.OnProcessSourceFileHandler(sourceFileBlob, logging)):
        # Set the service bus message to the name of the input file name
        sbOutMsgProcessExtractedFiles.set(fileName)
    else:
        pass
    
'''
    OnProcessExtractedFiles - executes when the service bus is signaled from OnNewFile
    process the extracted files into a final results file
    Signals a service bus when finished, causing OnFinalResultsReadyForProcessing to execute.
'''

@app.service_bus_queue_trigger(
    arg_name="sbInMsgProcessExtractedFiles", 
    queue_name="dsm-process-extracted-files",
    connection="AzureServiceBusConnStr") 

@app.service_bus_queue_output(
    arg_name='sbOutMsgProcessFinalResults', 
    connection='AzureServiceBusConnStr', 
    queue_name='dsm-process-final-results')

def OnProcessExtractedFiles(sbInMsgProcessExtractedFiles: func.ServiceBusMessage, sbOutMsgProcessFinalResults: func.Out[str]):
    # virtualFolder is the name of the original zip file which is then used as the virtual folder name in the extracted files
    # ex: extracted-files/06-02023.zip/week1...xlsx
    #                                  week2...xlsx
    virtualFolderName = sbInMsgProcessExtractedFiles.get_body().decode('utf-8')
    finalResultsFileName = settings['finalResultsFileName']
    logging.info('[OnProcessExtractedFiles] entered, processing the extracted files...')
    logging.info(f" Virtual Folder:{virtualFolderName}")
    
    # Call the handler
    if (OnHandlers.OnProcessExtractedFilesHandler(logging)):
        # The name of the final results file, stored in the virtual folder when complete
        blobName = f"{virtualFolderName}/{finalResultsFileName}"
        sbOutMsgProcessFinalResults.set(blobName)
        pass
    else:
        pass
    
    
'''
    OnProcessFinalResults - executes when the service bus is signaled from OnFileReadyForProcessing
    This is the final step of the file processing process.
'''

@app.service_bus_queue_trigger(
    arg_name="sbInMsgProcessFinalResults", 
    queue_name="dsm-process-final-results",
    connection="AzureServiceBusConnStr") 

def OnProcessFinalResults(sbInMsgProcessFinalResults: func.ServiceBusMessage):
    # The virtual is the name of the original zip file which is then used as the virtual folder name in the extracted files
    # The final results csv file is stored in the virtual folder and the file name is passed through the service bus message
    finalResultsFileName = sbInMsgProcessFinalResults.get_body().decode('utf-8')

    logging.info('[OnProcessFinalResults] entered, processing the final results file...')
    logging.info(f" Final Results File Name: {finalResultsFileName}")
    
    # Call the handler
    if (OnHandlers.OnProcessFinalResultsHandler(logging)) :
        pass
    else:
        pass


