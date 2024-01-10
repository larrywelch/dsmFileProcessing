##
## The configuration object for interacting with azure
##
##
##

import string
from azure.storage.blob import BlobServiceClient, ContainerClient


class azureConfig() :
  
  def __init__(self, connectionString: string, containerName: string):
    # The connection string for the Azure Container that contains the PDF files for processing  
    self.connectionString = connectionString
    # The container name within the Azure Container that contains the PDF files for processing
    self.containerName = containerName
    # The blob service client created using the connection string and container
    self.__blobSvcClient = None
    # The container service created using the connection string and container name
    self.__containerClient = None
    
  def getBlobServiceClient(self) -> BlobServiceClient:
    if (self.__blobSvcClient == None and self.connectionString ) :
      self.__blobSvcClient = BlobServiceClient.from_connection_string(self.connectionString)
      
    return self.__blobSvcClient
  
  def getContainerClient(self) -> ContainerClient:
    blobSvcClient = self.getBlobServiceClient()
    if (blobSvcClient != None and self.containerName) : 
      self.__containerClient = self.getBlobServiceClient().get_container_client(self.containerName)
  
    return self.__containerClient
      
  
  