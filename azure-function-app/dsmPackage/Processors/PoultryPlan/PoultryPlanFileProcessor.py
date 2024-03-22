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
import pandas as pd
import logging
import sqlalchemy
import azure.functions as func
from io import BufferedReader

from dsmPackage.AzureLib.azureUtil import azureUtil
from dsmPackage.AzureLib.azureFunctions import azureFunctions
from dsmPackage.PDFLib.pdfUtil import pdfUtil
from dsmPackage.Processors.ProcessorConfig import ProcessorConfig
from .PoultryPlanProcess import process

class PoultyPlanFileProcessor():
    def __init__(self, config: ProcessorConfig) -> None:
        self._configuration = config
        self._finalResultsFileName = 'final_results.csv'
        self._finalResultsTableName = 'poultry_plan_final_results'
            
    def onProcessSourceFile(self, sourceFileBlob : func.InputStream) -> Exception :
        logging.info('[PoultryPlanFileProcessor:onProcessSourceFile]')
        
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
    
    '''
        Limited processing - simply convert fileoutpart1.xlsx to csv file
    '''
    def OnProcessExtractedFiles(self, sourceFileName: str):
        logging.info('[PoultryPlanFileProcessor:OnProcessExtractedFiles]')
        config = self._configuration
        
        # Create our container that we'll use to download files and upload the final results
        azUtil = azureUtil(config.blobConnStr, config.outContainerName)
        
        # Process the blob (file) 
        csvOutput = process(azUtil, sourceFileName)
        
        # Upload the final results
        data = bytes(csvOutput, 'utf-8')
        azureFunctions.uploadBytes(azUtil, data, sourceFileName, 'final_results.csv')
        
    def OnProcessFinalResults(self, sourceFileName: str):
        logging.info('[PoultryPlanFileProcessor:OnProcessFinalResults]')
        
        config = self._configuration
        
        # Create our container that we'll use to download files and upload the final results
        azUtil = azureUtil(config.blobConnStr, config.outContainerName)
        
        # Create a path using a virtual folder structure
        path = "{z}/{f}"
        fullFileName = path.format(z=sourceFileName, f=self._finalResultsFileName)
        
        # Read the file
        downloader  = azureFunctions.downloadBlob(azUtil, fullFileName)
        finalResults = pd.read_csv(io.BytesIO(downloader.readall()), sep=",", dtype=str)
          
        # Store the source zip file name within the final results (the folder name is the name of the zip file)
        finalResults['source_file'] = sourceFileName
        
        # Create the connection string using the values from the config
        #https://stackoverflow.com/questions/44760221/pyodbc-connect-works-but-not-sqlalchemy-create-engine-connect
        pyConnStr = f'Driver=ODBC Driver {config.odbcDriver} for SQL Server;Server=tcp:{config.sqlServerUrl},{config.sqlServerPort};Database={config.sqlDBName};Uid={config.sqlUserName};Pwd={config.sqlUserPassword};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        
        connection_url = sqlalchemy.URL.create(
                "mssql+pyodbc",
                query={"odbc_connect": pyConnStr}
            )
  
        # Write contents of file to the database
        engine = sqlalchemy.create_engine(connection_url, connect_args={"timeout": 30})
        engine.connect()

        finalResults.to_sql(self._finalResultsTableName, engine, if_exists='append', index=False)

        return