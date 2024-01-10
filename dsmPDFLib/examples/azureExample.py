#
# Use the Azure Library to perform functions
#

import string
import os
from pdfLib.azureConfig import azureConfig
from pdfLib.azureFunctions import azureFunctions
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def listBlobs(azConfig:azureConfig):
  print('[listBlobs] blobs contains:')
  blobs = azureFunctions.getBlobs(azConfig)

  for blob in blobs:
    print(blob.name)

  print('[listBlobs] success!')
  
def uploadSampleFile(azConfig:azureConfig):
  print('[uploadSampleFile] uploading sample file...')
  
  # Get the sample file - note that this tests expects a folder to exist (sample-pdfs) and for it to contain a sample.pdf file
  base_path = os.path.dirname(os.path.realpath(__file__))
  samplesDir = os.path.join(base_path,'../sample-pdfs')
  fileName = os.path.join(samplesDir, 'sample.pdf')
  print(fileName)
  
  # Upload the file - we get back a BlobServiceClient 
  blobClient = azureFunctions.uploadFile(azConfig, fileName)
  assert blobClient != None
  
  # Now let's delete the file - include = Deletes the blob along with all snapshots.
  print('[uploadSampleFile] deleteing sample file from blob storage...')
  blobClient.delete_blob('include')
  
  print('[uploadSampleFile] success!')


def downloadBlob(azConfig:azureConfig):
  print('[downloadBlob] blobs contains:')
  blobs = azureFunctions.getBlobs(azConfig)
  blobList = list(blobs)
  number_of_blobs = len(blobList)
  if (number_of_blobs > 0):
    # download the first blob
    blob = blobList[0]
    stream = azureFunctions.downloadBlob(azConfig, blob.name)
    assert stream != None   
    stream.close()
    print('[downloadBlob] success!')


def main():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

  azConfig = azureConfig(connectionString, containerName)
  
  print('Executing listBlobs()...')
  listBlobs(azConfig)
  print('')
  
  print('Executing downloadBlob()...')
  downloadBlob(azConfig)
  print('')
  
  print('Executing uploadSampleFile()...')
  uploadSampleFile(azConfig)
  print('')
  
  print('Complete.')
  
main()
