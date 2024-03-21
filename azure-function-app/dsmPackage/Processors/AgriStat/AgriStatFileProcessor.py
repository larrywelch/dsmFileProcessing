'''
    AgriStatsFileProcessor.py   The AgriStats file processor.  Expects a zip file as the initial source, which is then 
    extracted into it's excel spreadsheet parts.
'''

import zipfile, io
import pandas as pd
import sqlalchemy
import azure.functions as func

from dsmPackage.AzureLib.azureUtil import azureUtil
from dsmPackage.AzureLib.azureFunctions import azureFunctions
from .AgriStatConfig import AgriStatConfig
from .AgriStatProcess import process

class AgriStatFileProcessor():
    def __init__(self, config: AgriStatConfig) -> None:
        self._configuration = config
        pass

    def onProcessSourceFile(self, sourceFileBlob : func.InputStream) -> Exception :
        print(f'[agriStatsFileProcessor:onProcessSourceFile] {sourceFileBlob.name}')
        inputBytes = io.BytesIO(sourceFileBlob.read())
        virtualFolderName = sourceFileBlob.name.split('/')[1]
        try:                    
            config = self._configuration
            azUtil = azureUtil(config.blobConnStr, config.outContainerName)
            with zipfile.ZipFile(inputBytes, 'r') as zip_ref:
                filelist = list(filter(lambda f: f.filename.upper().endswith(".XLSX"), zip_ref.infolist()))
                for file in filelist:
                    with zip_ref.open(file.filename, 'r') as zip:
                        # File names are prefixed with #### where ## = Year and ## = Week of the Year
                        # Chelsea's scripts expect the ###_ to be omitted - we'll do that here
                        outFileName = zip.name[zip.name.upper().index("WEEK"):]

                        # Use the azure utils/functions to upload the file (bytes)
                        azureFunctions.uploadBytes(azUtil=azUtil, data=zip.read(), virtualFolderName=virtualFolderName, blobName=outFileName)
            return None

        except Exception as ex:
            return ex
          
    def OnProcessExtractedFiles(self):
        print('[agriStatsFileProcessor:onFileReadyForProcessing]')
        config = self._configuration
        # Create our container that we'll use to download files and upload the final results
        azUtil = azureUtil(config.blobConnStr, config.outContainerName)
        
        # Process the blob (file) using Chelsea's script
        csvOutput = process(azUtil, config.folderName)
        
        # Upload the final results
        data = bytes(csvOutput, 'utf-8')
        azureFunctions.uploadBytes(azUtil, data, config.folderName, 'final_results.csv')
        
        return
    
    def OnProcessFinalResults(self):
        print('[agriStatsFileProcessor:onFinalResultsReadyForProcessing]')
        config = self._configuration
        
        # Create our container that we'll use to download files and upload the final results
        azUtil = azureUtil(config.blobConnStr, config.outContainerName)
        
        # Create a path using a virtual folder structure
        path = "{z}/{f}"
        fullFileName = path.format(z=config.folderName, f=config.finalResultsFileName)
        
        # Read the file
        #file = containerClient.download_blob(fullFileName).read()
        downloader  = azureFunctions.downloadBlob(azUtil, fullFileName)
        finalResults = pd.read_csv(io.BytesIO(downloader.readall()), sep=",", dtype=str)
    
        # Store the source zip file name within the final results (the folder name is the name of the zip file)
        finalResults['source_file'] = config.folderName
        
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

        finalResults.to_sql(config.sqlTableName, engine, if_exists='append', index=False)

        return
    