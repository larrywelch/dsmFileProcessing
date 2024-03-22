'''
  clearStorageContainer.py  delete all files from the Azure Storage container 
  
  The utility uses a BlobServiceClient to do the heavy lifting.  Since I'm not sure if we can delete and recreate the container, we're going to
  just get the list of blobs and delete them one at a time.
  
  '''

from azure.storage.blob import BlobServiceClient

from configuration import settings
STORAGE_CONN_STR = settings['blobConnStr']
SOURCE_FILES_CONTAINER = settings['inContainerName']
EXTRACTED_FILES_CONTAINER = settings['outContainerName']

def clearContainer(blobSvcClient, containerName):
  print(f'Deleting all blobs in the {containerName} container...')

  try:
    containerClient = blobSvcClient.get_container_client(containerName)
    blobs = containerClient.list_blobs()
    for blob in blobs:
      print(f'Deleting blob {blob.name}')
      containerClient.delete_blob(blob, delete_snapshots='include')

    print(f'Container {containerName} has been cleared.')
  except Exception as ex:
    print(ex)

def clearStorage() :
  print('Deleting all files from the Azure Storage Account/Containers')
  blobSvcClient = BlobServiceClient.from_connection_string(conn_str=STORAGE_CONN_STR)

  clearContainer(blobSvcClient, SOURCE_FILES_CONTAINER)
  
  clearContainer(blobSvcClient, EXTRACTED_FILES_CONTAINER)


