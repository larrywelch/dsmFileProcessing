# DSM PDF Library
The library for processing pdf files - originally developed to process files provided from Poulty Plan

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

to use the library, pip install dsmPDFLib/dist/DSMPdfLib-[version].py3-none-any.whl

# Environment Variables
Some of the tests and examples require the following environment variables:
PDF_SERVICES_CLIENT_ID
PDF_SERVICES_CLIENT_SECRET

They can be set in the terminal window or using a batch file:
set PDF_SERVICES_CLIENT_ID=some_value
set PDF_SERVICES_CLIENT_SECRET=some_value

These values are obtained from the Adobe Developer Portal

# Run Tests
python setup.py pytest

# Examples
The examples folder contains example applications that use the library.  There is also an examples file one folder up that uses the pip install ....whl

## Run the examples
PDF Examples:
  python examples/pdfExample.py


# Install Python Pacakged from Requirements.txt
pip install -r requirements.txt

# Known Issues
Everything works, however we get this warning that needs to eventually be resolved if possible:
.venv\Lib\site-packages\requests\__init__.py:102
  c:\Dev_Area\DSM\git\dsmFileProcessing\dsmPDFLib\.venv\Lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.13) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
    warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "






