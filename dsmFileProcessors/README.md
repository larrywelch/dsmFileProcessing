# Overview
This library contains file processors, one for each known file type.  

https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

# Interface
Each file processor will support a well known interface so that the Azure functions can utilze them.

OnNewFile
OnFileReadyForProcessing
OnFinalResultsReadyForProcessing

# Setup
Make sure to execute the following (had to do these with elevated privilages):
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

to use the library, pip install dsmFileProcessors/dist/DSMFileProcessorLib-[version].py3-none-any.whl
