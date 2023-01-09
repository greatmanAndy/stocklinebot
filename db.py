import pyodbc
import pandas as pd
connection_string = "Driver=SQL Server;Server=localhost;Database={0};Trusted_Connection=Yes;Database={0};" 
cnxn = pyodbc.connect(connection_string.format("linebot"), autocommit=True)
