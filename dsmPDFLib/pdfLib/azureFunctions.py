##
## A static class for interacting with Azure.  The class requires an azureConfig object which contains
## the details for connecting and interacting with Azure
##

import io
import os
import string

from pdfLib.azureConfig import azureConfig
from io import BufferedReader
from azure.core.paging import ItemPaged
from azure.storage.blob import BlobProperties, BlobClient

class azureFunctions:
  @staticmethod
  def getBlobs(config: azureConfig) -> ItemPaged[BlobProperties]:
    return config.getContainerClient().list_blobs()

  @staticmethod
  def downloadBlob(config: azureConfig, blobName: string) -> BufferedReader:
    download = config.getContainerClient().download_blob(blobName)
    stream = io.BytesIO(download.readall())
    reader = io.BufferedReader(stream)
    return reader
  
  @staticmethod
  def uploadFile(config: azureConfig, fileName: string) -> BlobClient:
    baseFileName = os.path.basename(fileName)
    with open(file=fileName, mode="rb") as data:
      return config.getContainerClient().upload_blob(name=baseFileName, data=data, overwrite=True)
