import openpyxl
import dbANDtable
import myUpdate
table_name = 'sksksksk'
current_dbname = 'kkk'
current_database= openpyxl.load_workbook('data/data02.xlsx')
columns_list = {'1', '2', '3', '4'}
myUpdate.insert(table_name, current_database, current_dbname, columns_list)
