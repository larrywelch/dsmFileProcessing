# Overview
The DMS Azure Function App for Processing Files

# Setup

## Virtual Environment
A virtual environment consists of python libraries being stored within the project folder structure.  The virtual environment utilizes a local folder named .venv.

VS Code makes it easy to create a python virtual environment.  As such, we use that with the requirements.txt file to make sure we have the proper libraries needed.  From the use Python: Create Environment..

## Configuration.py
The function app uses configuration values that are provided through the src/configuration.py.  It returns a settings json object, whose values are read using the os.getenv function.  Since many of the values are sensitive (user name, password, etc...), the default values are set to ***SENSITIVE-SET-ENV_VARIABLE***.  Use the set-configuration-values-template.txt file to set actual values and then save the file as a .bat and execute it through a terminal window.


## set-configuration-values.bat and set-configuration-values-template.txt
To avoid storing sensative information in the source code repo, use a batch file to set local environment values.  Those values are then read into the app through the configuration.py file as settings.  The set-configuration-values-template.txt contains the environment values that need to be set.  Save the file as set-configuration-values.bat with the proper values.  Then execute the batch file from a terminal window.  Once complete, local debugging is capable.

Make sure that the .functignore and .gitignore include .bat so that the batch file with sensitive data isn't included in the repo, or pushed with the function to azure.  

## local.settings.json
Note: When debugging the function app locally, the environment values set from the terminal using the batch file are not used.  Instead, the values must be set in the local.settings.json file


## local.settings.json
Some of the functions within the app use bindings for input parameters.  The bindings can't use the values retrieved using the Configuration.py approach.  Instead, the connection string values must be stored in the local.settings.json.


# Deployment
