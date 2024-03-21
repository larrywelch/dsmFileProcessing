##
## A static class for interacting with Azure.  The class requires an azureConfig object which contains
## the details for connecting and interacting with Azure
##

import os
import string
from azure.storage.blob import StorageStreamDownloader

from .azureUtil import azureUtil
from azure.core.paging import ItemPaged
from azure.storage.blob import BlobProperties, BlobClient

class azureFunctions:
  @staticmethod
  def getBlobs(azUtil: azureUtil) -> ItemPaged[BlobProperties]:
    return azUtil.getContainerClient().list_blobs()
 
  @staticmethod
  def downloadBlob(azUtil: azureUtil, blobName: string) -> StorageStreamDownloader:
    download = azUtil.getContainerClient().download_blob(blobName)
    return download
 
  @staticmethod
  def uploadFile(azUtil: azureUtil, fileName: string) -> BlobClient:
    baseFileName = os.path.basename(fileName)
    with open(file=fileName, mode="rb") as data:
      return azUtil.getContainerClient().upload_blob(name=baseFileName, data=data, overwrite=True)

  @staticmethod
  def uploadBytes(azUtil: azureUtil, data: bytes, virtualFolderName: str, blobName: str):
    path = "{z}/{f}"
    p = path.format(z=virtualFolderName, f=blobName)
    azUtil.getContainerClient().upload_blob(name=p, data=data, overwrite=True)
    return