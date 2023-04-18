import pyodbc

connection_string = "Driver=SQL Server;Server=35.229.143.23;Database={0};Trusted_Connection=Yes;Database={0};" 
cnxn = pyodbc.connect(connection_string.format("linebot"), autocommit=True)
