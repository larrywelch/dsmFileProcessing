#
# Tests for the azure util class
#

import os
from dsmAzureLib.azureUtil import azureUtil

def test_createObject():
  azUtil = azureUtil("", "")
  assert azUtil != None
  
def test_blobSvcClientEmptyConfig():
  azUtil = azureUtil("", "")
  assert azUtil.getBlobServiceClient() == None

def test_blobSvcClient():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  # Assert if we don't have a connection string
  assert connectionString

  # Create our azureConfig using only the connection string - we don't need a container for this test  
  azUtil = azureUtil(connectionString, "")
  blobSvcClient = azUtil.getBlobServiceClient()
  assert blobSvcClient != None
  
def test_containerClientEmptyConfig():
  azUtil = azureUtil("", "")
  assert azUtil.getContainerClient() == None

def test_containerClient():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
  
  # Assert if we don't have a connection string or a container name
  assert connectionString and containerName
  
  # Create an azureConfig using the connection string and container name
  azUtil = azureUtil(connectionString, containerName)
  containerClient = azUtil.getContainerClient()
  assert containerClient != None
  
  