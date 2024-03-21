# DSM File Processing Library
A python library containing the file processing functions for AgriStat CSV and Poulty Plan PDF Files.

The goal of the library is to create reusable code so that new partner files can be added quickly.  It is understood that each partner will have specific requirements, but each will likely be Zip / CSV or PDF based.

# Azure Library
The dsmAzureLib provides features for the interacting with Azure - currently limited to Azure Storage

# CSV Library
The dsmCSVLib provides features for parsing csv files to then be processed into a sql database.

# DSM File Processors
The library contains processors for all well known file types.  Currently limited to:
- Agristats - zip files
- Poultry Plan - pdf's

# PDF Library
The dsmPDFLib provides features for uploading pdf files to azure, parsing csv files to then be processed into a sql database.

# Environment Variables
The libraries, examples, and tests utilize environment variables.  The .gitignore has been updated to exclued set-env-vars.bat.  It's best to create this file within the library folders for setting the values.

