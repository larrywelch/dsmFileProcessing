# Overview
The OnNewFile function uses a blob trigger.  It runs whenever a new zip file is placed in the storage account/container.  The zip file is extracted, and the results are then stored in another container, seperating the source zip from the extracted files.

# Configuration
The function app can be configured both locally and on Azure using the Configuration section of the Azure Function App.  The configuration values can be retrieved using os.getenv, regardless of whether one is debugging locally, or running on Azure.

There is a config.py the further abstracts the details for the function.

This function utilizes configuration values for:
    service bus: signaling a service bus that the file is ready to be processed
    email: the email notification.  All other values are hard coded in the function_app.py as part of the blob_change_trigger decorator