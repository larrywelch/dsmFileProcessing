'''
  main.py This utility is used to reset the Azure environment.  Use with caution as it deletes files from storage accounts and deletes 
  rows from a sql table
'''

from clearStorageContainer import clearStorage
from clearSqlDB import clearSqlDBTable


def main() :
  print("=== Resetting Environment ===")
  print("")
  print("This utility will reset the Azure environment.  It performs the following:")
  print("1. Deletes all rows from the SQL DB final_results table")
  print("2. Deletes all files from the zip files location")
  print("3. Deletes all files from the extracted zip file location")
  print("")
  confirm = ""
  while (confirm != 'Y') and (confirm != 'N'): 
    confirm = input('Confirm (Y/N)?').upper()
  
  if (confirm == 'Y'):
    print("Performing tasks, please wait...")

    clearSqlDBTable("agristats_final_results")

    clearSqlDBTable("poultry_plan_final_results")

    clearStorage()
    
  else:
    print("Nothing to do")

  print("Complete.")

main()