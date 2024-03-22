# Overview
The DMS Azure Function App for Processing Files

# Setup

## Virtual Environment
A virtual environment consists of python libraries being stored within the project folder structure.  The virtual environment utilizes a local folder named .venv.

VS Code makes it easy to create a python virtual environment.  As such, we use that with the requirements.txt file to make sure we have the proper libraries needed.  From the use Python: Create Environment..

## Configuration.py
The function app uses configuration values that are provided through the src/configuration.py.  It returns a settings json object, whose values are read using the os.getenv function.  Since many of the values are sensitive (user name, password, etc...), the default values are set to ***SENSITIVE-SET-ENV_VARIABLE***.  

Use a .env instead of a batch file for setting the environment values.  Use the env-file-tempate.txt as a starting point.


## local.settings.json
When values appear in both the .env and local.settings.json file, you'll get a notice and be told that the local.settings.json values aren't used.


## local.settings.json
Some of the functions within the app use bindings for input parameters.  The bindings can't use the values retrieved using the Configuration.py approach.  Instead, the connection string values must be stored in the local.settings.json.


# Deployment
