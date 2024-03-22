'''
  clearSQLDB - deletes all rows from the Azure sql table

'''

import pymssql

from configuration import settings
SQL_SERVER_URL = settings['sql_server_url']
SQL_DB_NAME = settings['sql_server_db_name']
SQL_USER = settings['sql_user_name']
SQL_USER_PW = settings['sql_user_pw']
SQL_PORT = settings['sql_server_port']


def clearSqlDBTable(tableName: str) :
  print(f"Deleting all rows from the Azure SQL DB Table ({tableName})...")
  conn = pymssql.connect(database=SQL_DB_NAME, server=SQL_SERVER_URL, user=SQL_USER, password=SQL_USER_PW, as_dict=True)
  cursor = conn.cursor()
  cursor.execute(f'DELETE FROM {tableName}')
  conn.commit()
  conn.close()
  print('All rows deleted')