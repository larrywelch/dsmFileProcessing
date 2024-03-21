'''
    An example of how to use the AgriStat File Processor
'''

import os
import io

from dsmFileProcessorLib.AgriStat.AgriStatConfig import AgriStatConfig
from dsmFileProcessorLib.AgriStat.AgriStatFileProcessor import AgriStatFileProcessor


settings = {
    'blobConnStr': os.getenv('blobConnStr', 'DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net'),
    'inContainerName': os.getenv('inContainerName', 'sample-files-to-be-processed'),
    'outContainerName': os.getenv('outContainerName', 'sample-files-extracted'),
    'finalResultsFileName' : os.getenv('finalResultsFileName', 'final_results.csv'),
    'sql_user_name': os.getenv('sql_user_name', 'dsm-sql-admin'),
    'sql_user_pw': os.getenv('sql_user_pw', 'q1w2e3$q1w2e3$'),
    'sql_server_url': os.getenv('sql_server_url', 'dsm-file-processing-sql-svr-dev.database.windows.net'),
    'sql_server_db_name': os.getenv('sql_server_db_name', 'dsm-agristat-db-dev'),
    'sql_server_table_name': os.getenv('sql_server_table_name', 'final_results'),
    'sql_server_port': os.getenv('sql_server_port', 1433),
    'odbc-driver': os.getenv('odbc-driver', '17')
}

def main():
    print('=== Test the AgriStat File Processor ===')
    
    # Create our config
    zipFileName = '06-02-2023.zip'
    config : AgriStatConfig = AgriStatConfig.builder() \
        .with_azure_storage_elements(settings['blobConnStr'], settings['inContainerName'], settings['outContainerName'], zipFileName, settings['finalResultsFileName']) \
        .with_sql_config_elements(settings['sql_user_name'], settings['sql_user_pw'], settings['sql_server_url'], settings['sql_server_port'], settings['odbc-driver'], settings['sql_server_db_name'], settings['sql_server_table_name']) \
        .build()
    processor = AgriStatFileProcessor(config)
       
    # Test onNewFile
    print('=> Testing onNewFile...')
    
    # Open the zip file and get the bytes
    base_path = os.path.dirname(os.path.realpath(__file__))
    samplesDir = os.path.join(base_path,'../sample-files')
    fileName = os.path.join(samplesDir, zipFileName)
    with open(fileName, 'rb') as fh:
        buf = io.BytesIO(fh.read()) 
        processor.onNewFile(buf)
    
    # Test the onFileReadyForProcessing
    print('=> Testing onFileReadyForProcessing...')
    processor.onFileReadyForProcessing()
    
    # Test onFinalResultsReadyForProcessing
    print('=> Testing onFinalResultsReadyForProcessing...')
    processor.onFinalResultsReadyForProcessing()
    
    print('=== Complete ===')
    pass


main()