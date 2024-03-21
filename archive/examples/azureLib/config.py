'''
    config.py - provides configuration values for the application.  Will use values found in environment variables, or defaults.
'''

import os

settings = {
    'AZURE_STORAGE_CONNECTION_STRING': os.getenv('AZURE_STORAGE_CONNECTION_STRING', 'DefaultEndpointsProtocol=https;AccountName=dsmfileprocessingsadev;AccountKey=pITxU1tnCVrY2IGC6vNZd203AFZdSwFc9YLub4pg2UrxrJVoNDKeD+mdiU3g5HYwzgpd/QtgZYY++AStVQpSRA==;EndpointSuffix=core.windows.net'),
    'AZURE_STORAGE_CONTAINER_NAME': os.getenv('AZURE_STORAGE_CONTAINER_NAME', 'performance-pdf'),
    'AZURE_EMAIL_SVC_CONNECTION_STRING': os.getenv('AZURE_EMAIL_SVC_CONNECTION_STRING', 'endpoint=https://dsm-file-processing-cs-dev.unitedstates.communication.azure.com/;accesskey=jNSYS7CJp08m/5gVbZ10lQqaXk+fGSZYpi2JTIW8AUV2YlgVd2Oe5zVCeNRCQRWIfP71Lcu2+h/c+NOjs8iPyg=='),
    'AZURE_EMAIL_SVC_SENDER_ADDRESS': os.getenv('AZURE_EMAIL_SVC_SENDER_ADDRESS', 'dsm-file-processing@6ec572d5-4956-4084-8c43-25e013f1fe0b.azurecomm.net'),
    'AZURE_EMAIL_SVC_SEND_TO_LIST': os.getenv('AZURE_EMAIL_SVC_SEND_TO_LIST', 'larry.welch@foundationtek.com;normanlwelch@outlook.com'),
}