#
# Tests for the azureFunctions class
#

import os
from dsmAzureLib.azureUtil import azureUtil
from dsmAzureLib.azureFunctions import azureFunctions

def test_getBlobs():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
  
  azUtil = azureUtil(connectionString, containerName)
  blobs = azureFunctions.getBlobs(azUtil)
  
  # This should not fail - we should always get a list
  assert blobs != None
  
  # Iterate the blobs
  for blob in blobs:
    assert blob != None
    
def test_downloadBlob():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
  
  azUtil = azureUtil(connectionString, containerName)
  blobs = azureFunctions.getBlobs(azUtil)
  
  # This should not fail - we should always get a list
  assert blobs != None
  
  blobList = list(blobs)
  number_of_blobs = len(blobList)
  if (number_of_blobs > 0):
    # download the first blob
    blob = blobList[0]
    stream = azureFunctions.downloadBlob(azUtil, blob.name)
    assert stream != None   
    stream.close()
    
def test_uploadFile():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
  
  azUtil = azureUtil(connectionString, containerName)
  
  # Get the sample file - note that this tests expects a folder to exist (sample-pdfs) and for it to contain a sample.pdf file
  base_path = os.path.dirname(os.path.realpath(__file__))
  samplesDir = os.path.join(base_path,'../sample-pdfs')
  fileName = os.path.join(samplesDir, 'sample.pdf')
  print(fileName)
  
  # Upload the file - we get back a BlobServiceClient 
  blobClient = azureFunctions.uploadFile(azUtil, fileName)
  assert blobClient != None
  
  # Now let's delete the file - include = Deletes the blob along with all snapshots.
  blobClient.delete_blob('include')
  
 