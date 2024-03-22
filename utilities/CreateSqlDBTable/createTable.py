'''
  createTable.py - Script that creates a table from a pandas DataFrame

  NOTE: The getColumnDtypes function defaults to varchar(25) - this has been sufficient for initial testing but may need to be adjusted.

Create table example
 https://medium.com/@mgangrade7/create-sql-table-using-python-for-loading-data-from-pandas-dataframe-985281dde307

'''

def getColumnDtypes(dataTypes):
    '''
    Function to create list of data types
    required for database table

    NOTE: default is varchar(25) - this may need to be adjusted
    
    '''
    dataList = []
    for x in dataTypes:
        if(x == 'int64'):
            dataList.append('int')
        elif (x == 'float64'):
            dataList.append('float')
        elif (x == 'bool'):
            dataList.append('boolean')
        else:
            dataList.append('varchar(50)')
    return dataList

def dropTable(conn, tableName) :
  dropTableStatement = 'DROP table ' + tableName
  cur = conn.cursor()
  try:
    cur.execute(dropTableStatement)
    conn.commit()
    cur.close()
    print("Dropped the existing table")
  
  except :
    pass

def createTable(conn, tableName, dataFrame, dropExisting) :
      
  # Collect column names into a list
  columnName = list(dataFrame.columns.values)

  # Collect column data types into a list
  columnDataType = getColumnDtypes(dataFrame.dtypes)

  # drop the existing table - table may not exist so we'll wrap this in a try
  if dropExisting :
     dropTable(conn, tableName)

  # Code for create table statement
  createTableStatement = 'CREATE TABLE ' + tableName + ' ('
  for i in range(len(columnDataType)):
      createTableStatement = createTableStatement + ' "' + columnName[i] + '" ' + columnDataType[i] + ','
  createTableStatement = createTableStatement[:-1] + ' );'

  cur = conn.cursor()
  cur.execute(createTableStatement)
  conn.commit()
  cur.close()

  print("Created new table")
