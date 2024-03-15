'''
    AgriStatsFileProcessor.py   The AgriStats file processor.  Expects a zip file as the initial source, which is then 
    extracted into it's excel spreadsheet parts.
'''

import zipfile, io
from dsmAzureLib.azureUtil import azureUtil
from dsmAzureLib.azureFunctions import azureFunctions

class AgriStatsFileProcessor():
    def __init__(self) -> None:
        pass

    def onNewFile(self, inputBytes: io.BytesIO, blobConnStr: str, containerName: str, virtualFolderName: str) -> Exception :
        print('[agriStatsFileProcessor:onNewFile]')
        try:                    
            azUtil = azureUtil(blobConnStr, containerName)
            with zipfile.ZipFile(inputBytes, 'r') as zip_ref:
                filelist = list(filter(lambda f: f.filename.upper().endswith(".XLSX"), zip_ref.infolist()))
                #logging.info("Processing content of the zip file")
                for file in filelist:
                    with zip_ref.open(file.filename, 'r') as zip:
                        #logging.info(f"File Name: {zip.name} \n")
                        # File names are prefixed with #### where ## = Year and ## = Week of the Year
                        # Chelsea's scripts expect the ###_ to be omitted - we'll do that here
                        outFileName = zip.name[zip.name.upper().index("WEEK"):]
                            
                        # Create a path using a virtual folder structure
                        # path = "{z}/{f}"
                        # p = path.format(z=virtualFolderName, f=outFileName)

                        # Use the azure utils/functions to upload the file (bytes)
                        azureFunctions.uploadBytes(azUtil=azUtil, data=inputBytes, virtualFolderName=virtualFolderName, blobName=outFileName)

            return None

        except Exception as ex:
            return ex
          
    def onFileReadyForProcessing(self):
        print('[agriStatsFileProcessor:onFileReadyForProcessing]')
        return
    
    def onFinalResultsReadyForProcessing(self):
        print('[agriStatsFileProcessor:onFinalResultsReadyForProcessing]')
        return
    