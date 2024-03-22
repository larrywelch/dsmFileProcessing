# Overview

# Setup
Make sure to create a virtual environment using the requirements.txt file.  

Make sure to create a .env file for all configuration values found in the configuration.py file.  

# Environment Variables
Environment variables are set using the .env file.  The pyton debugger uses powershell, which doesn't allow for batch files.  

# Utilities

## CreateSQLTable
Creates/Recreates SQL DB tables using the final results files from the final_results_files folder

## RestEnvUtil
Resets the Azure environment by:
- Clearing the Azure Storage Containers
- Deleting all data from the SQL Database

