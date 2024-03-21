'''
    The configuration settings used by the application.  Each setting contains a default value, it's not a good idea
    to check in this file with production settings or user names and passwords.  Instead, use the set-configuration-values.bat file
    to set the environment values and don't check the batch file into the source code repo.
    
    NOTE: Use the set-configuration-values.bat file to set the environment variables
    
    *** MAKE SURE TO ADD .BAT to the .gitignore and .funcignore files ***
'''

import os

settings = {
    'AzureStorageContainerConnStr': os.getenv('AZURE_STORAGE_CONTAINER_CONN_STR', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'blobConnStr': os.getenv('BLOB_CONN_STR', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'inContainerName': os.getenv('BLOB_IN_CONTAINER_NAME', 'sample-files-to-be-processed'),
    'outContainerName': os.getenv('BLOB_OUT_CONTAINER_NAME', 'sample-files-extracted'),
    'finalResultsFileName' : os.getenv('BLOB_FINAL_RESULT_FILE_NAME', 'final_results.csv'),

    'AzureServiceBusConnStr': os.getenv('AZURE_SERVICE_BUS_CONN_STR', '***SENSITIVE-SET-ENV_VARIABLE***'),
    
    'sql_user_name': os.getenv('SQL_USER_NAME', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'sql_user_pw': os.getenv('SQL_USER_PW', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'sql_server_url': os.getenv('SQL_SERVER_URL', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'sql_server_db_name': os.getenv('SQL_SERVER_DB_NAME', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'sql_server_table_name': os.getenv('SQL_SERVER_TABLE_NAME', 'final_results'),
    'sql_server_port': os.getenv('SQL_SERVER_PORT', 1433),
    'odbc-driver': os.getenv('ODBC_DRIVER-driver', '17'),
    
    'email-notification-enabled' : os.getenv('EMAIL_NOTIFICATION_ENABLED', True),
    'email-notification-svc-conn-str': os.getenv('EMAIL_NOTIFICATION_SVC_CONN_STR', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'email-notification-send-to-list' : os.getenv('EMAIL_NOTIFICATION_SEND_TO_LIST', 'larry.welch@foundationtek.com'),
    'email-notification-poller-wait-time': os.getenv('EMAIL_NOTIFICATION_POLLER_WAIT_TIME', 10),
    'email-notification-sender-address' : os.getenv('EMAIL_NOTIFICATION_SENDER_ADDRESS', '***SENSITIVE-SET-ENV_VARIABLE***'),

    'pdfClientId' : os.getenv('PDF_SERVICES_CLIENT_ID', '***SENSITIVE-SET-ENV_VARIABLE***'),
    'pdfClientSecret' : os.getenv('PDF_SERVICES_CLIENT_SECRET', '***SENSITIVE-SET-ENV_VARIABLE***')
}