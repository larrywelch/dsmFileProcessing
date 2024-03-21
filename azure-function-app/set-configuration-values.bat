ECHO ON

REM Storage Container Values
SET AZURE_STORAGE_CONTAINER_CONN_STR=DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net
SET BLOB_CONN_STR=
SET BLOB_IN_CONTAINER_NAME=sample-files-to-be-processed
SET BLOB_OUT_CONTAINER_NAME=sample-files-extracted
SET BLOB_FINAL_RESULT_FILE_NAME=final_results.csv

REM Service Bus Values
SET AZURE_SERVICE_BUS_CONN_STR=Endpoint=sb://dsm-file-processing-sb-dev.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=cGJpebVGyd22/IwZnNfBdxmmoiM35Ut8o+ASbD4WIg4=

REM SQL Server Values
SET SQL_USER_NAME=dsm-sql-admin
SET SQL_USER_PW=q1w2e3$q1w2e3$
SET SQL_SERVER_URL=DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net
SET SQL_SERVER_DB_NAME=dsm-agristat-db-dev
SET SQL_SERVER_TABLE_NAME=final_results
SET SQL_SERVER_PORT=1433
SET ODBC_DRIVER=17

REM Email Notification Values
SET EMAIL_NOTIFICATION_ENABLED=True
SET EMAIL_NOTIFICATION_SVC_CONN_STR=endpoint=https://dsm-file-processing-cs-dev.unitedstates.communication.azure.com/;accesskey=jNSYS7CJp08m/5gVbZ10lQqaXk+fGSZYpi2JTIW8AUV2YlgVd2Oe5zVCeNRCQRWIfP71Lcu2+h/c+NOjs8iPyg==
SET EMAIL_NOTIFICATION_SEND_TO_LIST=larry.welch@foundationtek.com
SET EMAIL_NOTIFICATION_POLLER_WAIT_TIME=10
SET EMAIL_NOTIFICATION_SENDER_ADDRESS=dsm-file-processing@6ec572d5-4956-4084-8c43-25e013f1fe0b.azurecomm.net