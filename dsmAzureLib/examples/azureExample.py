#
# Use the Azure Library to perform functions
#

import os
from dsmAzureLib import emailUtil
from dsmAzureLib.azureUtil import azureUtil
from dsmAzureLib.azureFunctions import azureFunctions

def listBlobs(azUtil:azureUtil):
  print('[listBlobs] blobs contains:')
  blobs = azureFunctions.getBlobs(azUtil)

  for blob in blobs:
    print(blob.name)

  print('[listBlobs] success!')
  
def uploadSampleFile(azUtil:azureUtil):
  print('[uploadSampleFile] uploading sample file...')
  
  # Get the sample file - note that this tests expects a folder to exist (sample-pdfs) and for it to contain a sample.pdf file
  base_path = os.path.dirname(os.path.realpath(__file__))
  samplesDir = os.path.join(base_path,'../sample-pdfs')
  fileName = os.path.join(samplesDir, 'sample.pdf')
  print(fileName)
  
  # Upload the file - we get back a BlobServiceClient 
  blobClient = azureFunctions.uploadFile(azUtil, fileName)
  assert blobClient != None
  
  # Now let's delete the file - include = Deletes the blob along with all snapshots.
  print('[uploadSampleFile] deleteing sample file from blob storage...')
  blobClient.delete_blob('include')
  
  print('[uploadSampleFile] success!')


def downloadBlob(azUtil:azureUtil):
  print('[downloadBlob] blobs contains:')
  blobs = azureFunctions.getBlobs(azUtil)
  blobList = list(blobs)
  number_of_blobs = len(blobList)
  if (number_of_blobs > 0):
    # download the first blob
    blob = blobList[0]
    downloader = azureFunctions.downloadBlob(azUtil, blob.name)
    assert downloader != None   
    print('[downloadBlob] success!')


def sendEmail(azUtil:azureUtil):
  print('[sendEmail] sending email...')
  
    # Get environment variables
  emailSvcConnStr = os.environ.get('AZURE_EMAIL_SVC_CONNECTION_STRING')
  emailSvcSenderAddress = os.environ.get('AZURE_EMAIL_SVC_SENDER_ADDRESS')
  emailSvcSendToList = os.environ.get('AZURE_EMAIL_SVC_SEND_TO_LIST')
  
  assert emailSvcConnStr and emailSvcSenderAddress and emailSvcSendToList
  
  # Create the email notification object
  emn = emailUtil(emailSvcConnStr, emailSvcSenderAddress)
  emn.sendEmail('Email from Unit Test', \
    'This email was sent from the unit tests.', \
    emailSvcSendToList
    )
  
  print('[sendEmai] complete!')
  
def main():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

  azUtil = azureUtil(connectionString, containerName)
  
  print('Executing listBlobs()...')
  listBlobs(azUtil)
  print('')
  
  print('Executing downloadBlob()...')
  downloadBlob(azUtil)
  print('')
  
  print('Executing uploadSampleFile()...')
  uploadSampleFile(azUtil)
  print('')
  
  print('Executing sendEmail()...')
  sendEmail(azUtil)
  print('')
  
  print('Complete.')
  
main()
