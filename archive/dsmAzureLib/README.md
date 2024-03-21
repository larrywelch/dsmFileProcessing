# DSM Azure Library
The library that encapsulates functions for interacting with Azure - currently limited to Azure Storage

# Setup
Make sure to execute the following:
pip install build
pip install pytest
pip install pytest-runner

## Library Development Mode
https://setuptools.pypa.io/en/latest/userguide/development_mode.html
The examples will fail unless the library is made editable:
pip install --editable .

# Build Library
## To build the tar and the wheel files
python -m build

## To just build the wheel file
python setup.py bdist_wheel

to use the library, pip install dsmAzureLib/dist/DSMAzureLib-[version].py3-none-any.whl

# Environment Variables
Some of the tests and examples require the following environment variables:
## For azure functions and azure util testing
AZURE_STORAGE_CONNECTION_STRING
AZURE_STORAGE_CONTAINER_NAME

## For email testing
AZURE_EMAIL_SVC_CONNECTION_STRING
AZURE_EMAIL_SVC_SENDER_ADDRESS
AZURE_EMAIL_SVC_SEND_TO_LIST

They can be set in the terminal window or using a batch file:
set AZURE_STORAGE_CONNECTION_STRING=some_value
set AZURE_STORAGE_CONTAINER_NAME=some_value

These values should point to a valid azure storage account.  The container doesn't have to exist, it will get created if needed.

# Run Tests
python setup.py pytest

# Examples
The examples folder contains example applications that use the library.  There is also an examples file one folder up that uses the pip install ....whl

## Run the examples
Azure Examples:
  python examples/azureExample.py


# Install Python Pacakged from Requirements.txt
pip install -r requirements.txt




