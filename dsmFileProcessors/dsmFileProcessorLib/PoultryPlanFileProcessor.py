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

import zipfile, io
from dsmAzureLib.azureUtil import azureUtil
from dsmAzureLib.azureFunctions import azureFunctions

class PoultryPlanFileProcessor():
    def __init__(self) -> None:
        pass
    
    def onNewFile(self,  inputBytes: io.BytesIO, blobConnStr: str, containerName: str, virtualFolderName: str) -> Exception :
        print('[PoultryPlanFileProcessor:onNewFile]')
        return None
    
    def onFileReadyForProcessing(self):
        print('[PoultryPlanFileProcessor:onFileReadyForProcessing]')
        return
    
    def onFinalResultsReadyForProcessing(self):
        print('[PoultryPlanFileProcessor:onFinalResultsReadyForProcessing]')
        return