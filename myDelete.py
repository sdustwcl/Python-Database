import re
from openpyxl import load_workbook
import pandas as pd
from pandasql import sqldf


def delete(sql, dbname):
    if 'where' in sql:
        matchObj = re.search(r'^delete from (.*) where (.*);$', sql)
        tb_name = matchObj.group(1)
        db = pd.ExcelFile(r'data/' + dbname + '.xlsx')
        tb = db.parse(sheet_name=tb_name)
        writer = pd.ExcelWriter(r'data/' + dbname + '.xlsx')
        obj = matchObj.group(2).replace("=", "==").replace("!==", "!=").replace("<==", "<=").replace(">==", ">=").replace("<>", "!=")
        # print(tb.query(obj))
        tb.drop(tb.query(obj).index).to_excel(writer, sheet_name=tb_name, index=False)
        for i in db.sheet_names:
            if i != tb_name:
                db.parse(i).to_excel(writer, sheet_name=i, index=False)
        writer.save()
        print('Delete success')
    else:
        matchObj = re.search(r'^delete from (.*);$', sql)
        tb_name = matchObj.group(1)
        db = pd.ExcelFile(r'data/' + dbname + '.xlsx')
        tb = db.parse(sheet_name=tb_name)
        writer = pd.ExcelWriter(r'data/' + dbname + '.xlsx')
        df = tb.drop(tb.index)
        df.to_excel(writer, sheet_name=tb_name, index=False)
        for i in db.sheet_names:
            if i != tb_name:
                db.parse(i).to_excel(writer, sheet_name=i, index=False)
        writer.save()
        print('Delete success')

# sql = 'delete from sk where Name=\'wcl\';'
# sql = 'delete from sk where Name=\'xd\' and Age=22;'
# sql = 'delete from sk where Name=\'xd\' and Age=22 and Class<>2;'
# sql = 'delete from sk;'
# delete(sql, 'data02')
