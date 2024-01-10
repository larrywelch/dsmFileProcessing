# DSM File Processing Library
A python library containing the file processing functions for AgriStat CSV and Poulty Plan PDF Files.

The goal of the library is to create reusable code so that new partner files can be added quickly.  It is understood that each partner will have specific requirements, but each will likely be CSV or PDF based.

# CSV Library
The dsmCSVLib provides features for uploading csv files to azure, parsing csv files to then be processed into a sql database.

# PDF Library
The dsmPDFLib provides features for uploading pdf files to azure, parsing csv files to then be processed into a sql database.

# Environment Variables
The libraries, examples, and tests utilize environment variables.  The .gitignore has been updated to exclued set-env-vars.bat.  It's best to create this file within the library folders for setting the values.

