'''

  writeDataToTable.py - Write the DataFrame to the Sql Table

'''
import sqlalchemy

def writeDataFrameToSqlTable(dataFrame, tableName, connection_url) :
  print('Writing DataFrame to the Sql Table')
  # Write contents of file to the database
  engine = sqlalchemy.create_engine(connection_url)
  engine.connect()

  dataFrame.to_sql(tableName, engine, if_exists='append', index=False)

  print('DataFrame was successfully stored in the Sql Table')