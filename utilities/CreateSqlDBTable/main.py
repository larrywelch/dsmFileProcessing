'''
  
  main.py  - This is a utility that creates the Final Results Sql Tables.  
  The utility will drop the existing table.  

'''
import os
import pandas as pd
import pymssql
from createTable import createTable
#from .writeDataToTable import writeDataFrameToSqlTable
from configuration import settings

def fullFileName(fileName: str):
  base_path = os.path.dirname(os.path.realpath(__file__))
  final_results_path = os.path.join(base_path, 'final_results_files')
  fullFileName = os.path.join(final_results_path, fileName)
  return fullFileName

def createAgriStatsTable(conn):
  # Reaf csv files into dataframe
  finalResultsDF = pd.read_csv(fullFileName('agristats-final-results.csv'))
  finalResultsDF['source_file'] = 'CreateSQLTableUtil'
  tableName='agristats_final_results' # Make sure this matches what's in the AgriStatProcessor.py
  createTable(conn, tableName, finalResultsDF, True)

def createPoultryPlanTable(conn):
  # Read the xlsx file
  finalResultsDF = pd.read_excel(fullFileName('fileoutpart1.xlsx'))

  # Remove escape chars
  finalResultsDF.replace(to_replace=[r' _x000D_'], value=[''], regex=True, inplace=True)
  finalResultsDF.columns = finalResultsDF.columns.str.replace(' _x000D_', '').str.strip()
  finalResultsDF['source_file'] = 'CreateSQLTableUtil'
  
  # Rename the columns - Any changes to this must also be made to PoultryPlanProcessor.py
  #df.rename(columns={"A": "a", "B": "c"})
  finalResultsDF.rename(
    columns=
      {
        "Leg%": "Leg% Koppel", 
        "Unnamed: 5": "Leg% Norm",
        "Eigewicht (gr)": "Eigewicht (gr) Koppel",
        "Unnamed: 7": "Eigewicht (gr) Norm",
        "Eimassa (gr)" : "Eimassa (gr) Koppel",
        "Unnamed: 9" : "Eimassa (gr) Norm",
        "Water per dag (I)" : "Water per dag (I) Koppel",
        "Unnamed: 11" : "Water per dag (I) Norm",
        "Voer per dag (gr)" : "Voer per dag (gr) Koppel",
        "Unnamed: 13" : "Voer per dag (gr) Norm",
        "vc" : "VC Koppel",
        "Unnamed: 15" : "VC Norm",
        "Voer poh cum. (kg)": "Voer poh cum. (kg) Koppel",
        "Unnamed: 17": "Voer poh cum. (kg) Norm",
        "Ei poh cum.": "Ei poh cum. Kopper",
        "Unnamed: 19": "Ei poh cum. Norm",
        "Eimassa poh cum. (kg)": "Eimassa poh cum. (kg) Kopper",
        "Unnamed: 21" : "Eimassa poh cum. (kg) Norm",
        "VC cum.": "VC cum. Koppel",
        "Unnamed: 23" : "VC cum. Norm",
        "Uitval % cum." : "Uitval % cum. Koppel",
        "Unnamed: 25" : "Uitval % cum. Norm",
        "Lichaamsgewicht (gr)": "Lichaamsgewicht (gr) Koppel",
        "Unnamed: 27" : "Lichaamsgewicht (gr) Norm"
      },
      inplace=True
  )
  
  # Reaf csv files into dataframe
  # finalResultsDF = pd.read_csv(fullFileName('poultry-plan-final-results.csv'))
  # finalResultsDF['source_file'] = 'CreateSQLTableUtil'
  
  # # Remove \r and trim the white spaces from the column names
  # finalResultsDF.replace(to_replace=[r'\r'], value=[''], regex=True, inplace=True)
  # finalResultsDF.columns = finalResultsDF.columns.str.replace('\r', '').str.strip()

  tableName='poultry_plan_final_results' # Make sure this matches what's in the PoultryPlanProcessor.py
  
  createTable(conn, tableName, finalResultsDF, True)

def main():
  print("=== Create SQL DB Tables for the DSM File Processing ===")

  # Connect to database server to run create table statement
  serverURL = settings['sql_server_url']
  dbName =  settings['sql_server_db_name']
  user = settings['sql_user_name']
  pw = settings['sql_user_pw']

  conn = pymssql.connect(database=dbName, server=serverURL, user=user, password=pw, as_dict=True)

  #createAgriStatsTable(conn)

  createPoultryPlanTable(conn)

  print("Created the final results tables in the SQL Database")
  
main()