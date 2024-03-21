'''

    NOTES: 
    - Probably don't need inContainer and outContainer.  The process starts with a trigger on the 
    inContainer so we don't actually need to know it's name.
    
'''
class AgriStatConfig() :
    def __init__(self, 
                 blobConnStr: str, 
                inContainerName: str, 
                outContainerName: str,
                folderName: str,
                finalResultsFileName: str,
                userName: str,
                userPassword: str,
                serverUrl: str,
                serverPort: int,
                odbcDriver: str,
                dbName: str,
                tableName: str                
            ):
        self.blobConnStr = blobConnStr
        self.inContainerName = inContainerName
        self.outContainerName = outContainerName
        self.folderName = folderName
        self.finalResultsFileName = finalResultsFileName
        self.sqlUserName = userName
        self.sqlUserPassword = userPassword
        self.sqlServerUrl = serverUrl
        self.sqlServerPort = serverPort
        self.odbcDriver = odbcDriver
        self.sqlDBName = dbName
        self.sqlTableName = tableName            
        pass
    
    @staticmethod
    def builder():
        return AgriStatConfig.Builder()
        
    class Builder():
        
        def __init__(self):
            pass
        
        def with_azure_storage_elements(self, 
                                        blobConnStr: str, 
                                        inContainerName: str,
                                        outContainerName: str, 
                                        folderName: str,
                                        finalResultsFileName: str
                                        ):
            self.blobConnStr = blobConnStr
            self.inContainerName = inContainerName
            self.outContainerName = outContainerName
            self.folderName = folderName
            self.finalResultsFileName = finalResultsFileName
            
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
        
        def build(self):
            return AgriStatConfig(
                self.blobConnStr, 
                self.inContainerName,
                self.outContainerName, 
                self.folderName, 
                self.finalResultsFileName,
                self.sqlUserName,
                self.sqlUserPassword,
                self.sqlServerUrl,
                self.sqlServerPort,
                self.odbcDriver,
                self.sqlDBName,
                self.sqlTableName    
            )
        
