# DSM PDF Library
The library for processing pdf files - originally developed to process files provided from Poulty Plan

# Build Library
python setup.py bdist_wheel

to use the library, pip install dsmPDFLib/dist/DSMPdfLib-[version].py3-none-any.whl

# Run Tests
python setup.py pytest

# Development Notes
Inspired by:
https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

Create a virtual environment to isolate and ensure proper packages are configured:

Command Pallete: Python:Create Environment - choose a python configuration and then choose the requirements.txt file - keep in mind that the requirements.txt file needs to contain the packages needed by the library.  That said, packages can be added using pip install .... but be sure to then update the requirements.txt file for completeness.


A few links for reference - best way to set up virtual env is using the Command Pallete.
https://docs.python.org/3/library/venv.html
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/


# Run Tests
python setup.py pytest


