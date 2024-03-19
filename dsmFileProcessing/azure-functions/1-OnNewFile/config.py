import os

settings = {
    'storageContainerConnStr': os.getenv('storageContainerConnStr', 'DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net'),
    'AzureServiceBusConnectionString': os.getenv('AzureServiceBusConnectionString', 'Endpoint=sb://dsm-file-processing-sb-dev.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=cGJpebVGyd22/IwZnNfBdxmmoiM35Ut8o+ASbD4WIg4='),
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
    'odbc-driver': os.getenv('odbc-driver', '17'),
    
    'email-notification-enabled' : os.getenv('email_notification_enabled', True),
    'email-notification-svc-conn-str': os.getenv('email_notification_svc_conn_str', 'endpoint=https://dsm-file-processing-cs-dev.unitedstates.communication.azure.com/;accesskey=jNSYS7CJp08m/5gVbZ10lQqaXk+fGSZYpi2JTIW8AUV2YlgVd2Oe5zVCeNRCQRWIfP71Lcu2+h/c+NOjs8iPyg=='),
    'email-notification-send-to-list' : os.getenv('email_notification_send_to_list', 'larry.welch@foundationtek.com'),
    'email-notification-poller-wait-time': os.getenv('email_notification_poller_wait_time', 10),
    'email-notification-sender-address' : os.getenv('email_notification_sender_address', 'dsm-file-processing@6ec572d5-4956-4084-8c43-25e013f1fe0b.azurecomm.net')
}