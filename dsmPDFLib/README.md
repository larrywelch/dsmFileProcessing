# DSM PDF Library
The library for processing pdf files - originally developed to process files provided from Poulty Plan

# Build Library
## To build the tar and the wheel files
python -m build

## To just build the wheel file
python setup.py bdist_wheel

to use the library, pip install dsmPDFLib/dist/DSMPdfLib-[version].py3-none-any.whl

# Environment Variables
Some of the tests and examples require the following environment variables:
AZURE_STORAGE_CONNECTION_STRING
AZURE_STORAGE_CONTAINER_NAME

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

# Known Issues
Everything works, however we get this warning that needs to eventually be resolved if possible:
.venv\Lib\site-packages\requests\__init__.py:102
  c:\Dev_Area\DSM\git\dsmFileProcessing\dsmPDFLib\.venv\Lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.13) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
    warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "

# Development Notes
Inspired by:
https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

Create a virtual environment to isolate and ensure proper packages are configured:

Command Pallete: Python:Create Environment - choose a python configuration and then choose the requirements.txt file - keep in mind that the requirements.txt file needs to contain the packages needed by the library.  That said, packages can be added using pip install .... but be sure to then update the requirements.txt file for completeness.


A few links for reference - best way to set up virtual env is using the Command Pallete.
https://docs.python.org/3/library/venv.html
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/





