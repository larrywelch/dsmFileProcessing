'''
    PoultryPlanFileProcessor.py     The Poulty Plan file processor.  Expects an initial PDF file, which is then parsed using the 
    Adobe PDF API to parse it into multiple components:
        FileName
            tables
                fileoutpart0.xlsx
                fileoutpart1.xlsx
                fileoutpart2.xlsx
                fileoutpart3.xlsx
            structuredData.json
            
    fileoutputpart1.xlsx contains the table we're interested in.
'''

import io
import zipfile
import azure.functions as func
from io import BufferedReader, BufferedWriter

from dsmPackage.AzureLib.azureUtil import azureUtil
from dsmPackage.AzureLib.azureFunctions import azureFunctions
from dsmPackage.PDFLib.pdfUtil import pdfUtil
from dsmPackage.Processors.ProcessorConfig import ProcessorConfig

class PoultyPlanFileProcessor():
    def __init__(self, config: ProcessorConfig) -> None:
        self._configuration = config
    
    def onProcessSourceFile(self, sourceFileBlob : func.InputStream) -> Exception :
        print('[PoultryPlanFileProcessor:onNewFile]')
        
        config = self._configuration
        virtualFolderName = sourceFileBlob.name.split('/')[1]
        azUtil = azureUtil(config.blobConnStr, config.outContainerName)
        util = pdfUtil(config.pdfClientId, config.pdfClientSecret)
        inputBytes = io.BytesIO(sourceFileBlob.read())
        fileRef = util.extractFile(BufferedReader(inputBytes))
        
        # We now have a zip file which needs to be extracted
        # Or, we simply store the zip file in the extracted folder and then
        # let the next step extract it further      
        with io.BytesIO(fileRef.get_as_stream()) as buff:
            with zipfile.ZipFile(buff, 'r') as zip_ref:
                    filelist = zip_ref.infolist()# list(filter(lambda f: f.filename.uppe, zip_ref.infolist()))
                    for file in filelist:
                        with zip_ref.open(file.filename, 'r') as zip:
                            # File names are prefixed with #### where ## = Year and ## = Week of the Year
                            # Chelsea's scripts expect the ###_ to be omitted - we'll do that here
                            outFileName = zip.name #[zip.name.upper().index("WEEK"):]
                            
                            # Use the azure utils/functions to upload the file (bytes)
                            azureFunctions.uploadBytes(azUtil=azUtil, data=zip.read(), virtualFolderName=virtualFolderName, blobName=outFileName)
        
        return None
    
    def OnProcessExtractedFiles(self):
        print('[PoultryPlanFileProcessor:onFileReadyForProcessing]')
        return
    
    def OnProcessFinalResults(self):
        print('[PoultryPlanFileProcessor:onFinalResultsReadyForProcessing]')
        return