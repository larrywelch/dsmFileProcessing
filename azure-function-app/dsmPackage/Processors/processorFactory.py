'''
    The processor factory provides contains a list of know processors.  The app can request a processor for a given file.
'''

from .ProcessorConfig import ProcessorConfig
from .AgriStat.AgriStatFileProcessor import AgriStatFileProcessor

from .PoultryPlan.PoultryPlanFileProcessor import PoultyPlanFileProcessor

class processorFactory:
    
    @staticmethod
    def getProcessor(settings, fileName: str):        
        
        config : ProcessorConfig = ProcessorConfig.builder() \
            .with_azure_storage_elements(settings['blobConnStr'], settings['inContainerName'], settings['outContainerName']) \
            .with_sql_config_elements(settings['sql_user_name'], settings['sql_user_pw'], settings['sql_server_url'], settings['sql_server_port'], settings['odbc-driver'], settings['sql_server_db_name'], settings['sql_server_table_name']) \
            .with_pdf_config_elements(settings['pdfClientId'], settings['pdfClientSecret']) \
            .build()
            
        if (str.find(fileName.upper(), '.ZIP') > 0) :
            # Use agristats
            return AgriStatFileProcessor(config)
        elif(str.find(fileName.upper(), '.PDF') > 0):
            # Use Poultry Plan
            return PoultyPlanFileProcessor(config)
        else:
            return None