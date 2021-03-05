import re
import hashlib
import openpyxl as pyxl
import pandas as pd
import dbANDtable
import myInsert
import myUpdate
import mySelect
import myDelete


def Main():
    Login()
    while True:
        command = input()
        if command == 'exit':
            exit(0)
        else:
            trans(command)


def Login():
    global user
    print("input Username and Password")
    Username = input("username:")
    Password = input("password:")
    md5_pswd = hashlib.md5(Password.encode("utf-8")).hexdigest()
    if Check(Username, md5_pswd):
        print("Welcome {} ".format(Username))
        user = Username
    else:
        print("User not exist or password is wrong!")
        Login()


def Check(Username, md5_pswd):
    global right_pswd
    rows = []
    db = pyxl.load_workbook("data/data01.xlsx")
    table = db['user']
    for row in table.iter_rows():
        rows.append(row)
    for i in range(0, 9):
        if rows[i][0].value == Username:
            right_pswd = rows[i][1].value
    # print(right_pswd)
    # print(md5_pswd)
    if md5_pswd == right_pswd:
        return True
    else:
        return False


def trans(command):
    global db
    if 'use' in command:
        matchObj3 = re.search(r'^use (.*);$', command)
        db = matchObj3.group(1)
    if 'create database' in command:
        matchObj1 = re.search(r'^create database (.*);$', command)
        db_name = matchObj1.group(1)
        dbANDtable.create_db(db_name)
    elif 'create table' in command:
        matchObj2 = re.search(r'^create table (.*) \((.*)\);$', command)
        tb_name = matchObj2.group(1)
        dbANDtable.create_table(tb_name)
    elif 'insert' in command:
        myInsert.insert(command, db)
    elif 'update' in command:
        myUpdate.update(command, db)
    elif 'select' in command:
        mySelect.select(command, db)
    elif 'delete' in command:
        myDelete.delete(command, db)
    elif 'help database' in command:
        xl = pd.ExcelFile("data/" + db + ".xlsx")
        sheet_name = xl.sheet_names
        print(sheet_name)


Main()
