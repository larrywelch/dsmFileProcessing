import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="dsmFPBlob", path="files-to-be-processed",
                               connection="AzureWebJobsStorage") 
def OnNewFile(dsmFPBlob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {dsmFPBlob.name}"
                f"Blob Size: {dsmFPBlob.length} bytes")
