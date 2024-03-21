'''

  createDBConnection.py - Create a sql database connection

'''
import pymssql

def createDBConnection(user, pw, serverURL, dbName) :
  conn = pymssql.connect(database=dbName, server=serverURL, user=user, password=pw, as_dict=True)
  print("Created a sql db connection successfully.")
  return conn

