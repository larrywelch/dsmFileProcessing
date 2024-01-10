#
# Tests for the azure config class
#

import os
from pdfLib.azureConfig import azureConfig

def test_createObject():
  config = azureConfig("", "")
  assert config != None
  
def test_blobSvcClientEmptyConfig():
  config = azureConfig("", "")
  assert config.getBlobServiceClient() == None

def test_blobSvcClient():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  # Assert if we don't have a connection string
  assert connectionString

  # Create our azureConfig using only the connection string - we don't need a container for this test  
  config = azureConfig(connectionString, "")
  blobSvcClient = config.getBlobServiceClient()
  assert blobSvcClient != None
  
def test_containerClientEmptyConfig():
  config = azureConfig("", "")
  assert config.getContainerClient() == None

def test_containerClient():
  # Get the connection string from the environment variable
  connectionString = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  containerName = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
  
  # Assert if we don't have a connection string or a container name
  assert connectionString and containerName
  
  # Create an azureConfig using the connection string and container name
  config = azureConfig(connectionString, containerName)
  containerClient = config.getContainerClient()
  assert containerClient != None
  
  