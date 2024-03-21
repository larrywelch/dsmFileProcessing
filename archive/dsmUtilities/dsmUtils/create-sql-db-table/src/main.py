'''
  
  main.py  - This is a utility that creates the AgriStats Final Results Sql Table.  
  The utility will drop the existing table.  

'''

import os
import pandas as pd
from createTable import createTable
from writeDataToTable import writeDataFrameToSqlTable
from createDBConnection import createDBConnection
from sqlalchemy.engine import URL

print("=== Create SQL DB Table for Final Results ===")

# Reaf csv files into dataframe
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../input/table-source.csv')
finalResultsDF = pd.read_csv(filename)
finalResultsDF['source_file'] = 'CreateSQLTableUtil'

# Remove \r and trim the white spaces from the column names
finalResultsDF.replace(to_replace=[r'\r'], value=[''], regex=True, inplace=True)
finalResultsDF.columns = finalResultsDF.columns.str.replace('\r', '').str.strip()


# Connect to database server to run create table statement
serverURL = 'dsm-agristats-eval-sql-svr.database.windows.net'
dbName = 'dsm-pdf-eval'
user = 'dsmAdmin'
pw = 'q1w2e3$q1w2e3$'
tableName = 'final_results'
conn = createDBConnection(user, pw, serverURL, dbName)

# Create the table with the connection   
createTable(conn, tableName, finalResultsDF, True)

# Write contents of file to the database
connection_url = URL.create(
    "mssql+pyodbc",
    username=user,
    password=pw,
    host=serverURL,
    port=1433,
    database=dbName,
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)
writeDataFrameToSqlTable(finalResultsDF, tableName, connection_url)

print("Created the final_results table in the SQL Database")