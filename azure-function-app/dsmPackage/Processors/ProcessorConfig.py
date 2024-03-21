'''

    
'''
class ProcessorConfig() :
    def __init__(self, 
                 blobConnStr: str, 
                inContainerName: str, 
                outContainerName: str,
                userName: str,
                userPassword: str,
                serverUrl: str,
                serverPort: int,
                odbcDriver: str,
                dbName: str,
                tableName: str,
                pdfClientId: str,
                pdfClientSecret: str                
            ):
        self.blobConnStr = blobConnStr
        self.inContainerName = inContainerName
        self.outContainerName = outContainerName
        self.sqlUserName = userName
        self.sqlUserPassword = userPassword
        self.sqlServerUrl = serverUrl
        self.sqlServerPort = serverPort
        self.odbcDriver = odbcDriver
        self.sqlDBName = dbName
        self.sqlTableName = tableName            
        self.pdfClientId = pdfClientId
        self.pdfClientSecret = pdfClientSecret
    
    @staticmethod
    def builder():
        return ProcessorConfig.Builder()
        
    class Builder():
        
        def __init__(self):
            pass
        
        def with_azure_storage_elements(self, 
                                        blobConnStr: str, 
                                        inContainerName: str,
                                        outContainerName: str
                                        ):
            self.blobConnStr = blobConnStr
            self.inContainerName = inContainerName
            self.outContainerName = outContainerName
            
            return self
        
        def with_sql_config_elements(self,
                                     userName: str,
                                     userPassword: str,
                                     serverUrl: str,
                                     serverPort: int,
                                     odbcDriver: str,
                                     dbName: str,
                                     tableName: str
                                     ):
            self.sqlUserName = userName
            self.sqlUserPassword = userPassword
            self.sqlServerUrl = serverUrl
            self.sqlServerPort = serverPort
            self.odbcDriver = odbcDriver
            self.sqlDBName = dbName
            self.sqlTableName = tableName
            return self
        
        def with_pdf_config_elements(self,
                                     clientId: str,
                                     clientSecret: str):
            self.pdfClientId = clientId
            self.pdfClientSecret = clientSecret
            return self
        
        def build(self):
            return ProcessorConfig(
                self.blobConnStr, 
                self.inContainerName,
                self.outContainerName, 
                self.sqlUserName,
                self.sqlUserPassword,
                self.sqlServerUrl,
                self.sqlServerPort,
                self.odbcDriver,
                self.sqlDBName,
                self.sqlTableName,
                self.pdfClientId,
                self.pdfClientSecret
            )
        
