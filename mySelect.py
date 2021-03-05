import re
import openpyxl as pyxl
import pandas as pd
from pandasql import sqldf


def select(sql, dbname):
    sql_handle = sql.replace(",", " ")
    result = sql_handle.split(' ')
    length = len(result)
    from_pos = result.index('from')
    data = pd.read_excel("data/" + dbname + ".xlsx", sheet_name=0)
    if 'where' not in result:
        if '*' in result:
            print(data)
        else:
            print(data.loc[:, result[1:from_pos]])
    else:
        matchObj = re.search(r'^(.*)where (.*);$', sql)
        obj = matchObj.group(2)
        result1 = obj.replace("=", "==").replace("!==", "!=").replace("<==", "<=").replace(">==", ">=").replace("<>", "!=")
        if result[1] == '*':
            print(data.query(result1))
        else:
            tmp = data.query(result1)
            print(tmp.loc[:, result[1:from_pos]])

# sql = 'select Name from sk where Class=1 and Num!=1 and Age=20;'
# sql = 'select Name,Age from sk where Class=1 and Num=1;'
# sql = 'select * from sk where Class=1 and Num=1;'
# sql = 'select Name,Class from sk;'
# select(sql, 'data02')
