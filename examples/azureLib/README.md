# DSM Azure Library Examples


# Installation
It best to create a virtual environment to isolate the environment and be sure the requirements.txt file is accurate
View->Command Pallete Python:Create Environment

## Install Python Pacakged from Requirements.txt
The azure library can also be installed using straight forward pip:
pip install -r requirements.txt

or

pip install ../../dsmAzureLib/dist/DSMAzureLib-0.1.0-py3-none-any.whl
You may have to choose a Python Interpreter (View->Command Pallete Python:Select Interpreter)

NOTE:
In some cases when starting with a fresh install the virtual environment isn't quite right.  When this happens there are usually errors indicating the dsmAzureLib module can't be found, or pip can't be found.  Follow the steps below if this happend.

Start VS Code in Administrator mode and exexute the following command:
python -m ensurepip --default-pip

# Run
Be sure to set the necessary environment variables:
AZURE_STORAGE_CONNECTION_STRING
AZURE_STORAGE_CONTAINER_NAME

python main.py