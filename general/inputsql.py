## Interact with sqlite, outputs dataobject for SELECT querries.
## returns dataobject as list of tuples
## good only for .sqlite, .sqlite3, .db, .db3 for now.
## need to implement drivers for individual propriety databases. 
## For MySQL: mysql-python, oursql, PyMySQL
## For PostgreSQL: psycopg2
## For Microsoft SQL: pymssql
## For Oracle: cx_Oracle

import sqlite3
dataobject = []
print('Give location of database file. Provide input of the form: C:\\dir1\\subdir1\\file1') #.sqlite file... okay.
filename = str(input())
conn = sqlite3.connect(filename)
cur = conn.cursor()
while True:
    print('State SQL querry, "save" to commit or "break" to finish: ')
    sqlstr = str(input())
    if sqlstr.upper().startswith('SELECT'):
        try:
            for row in cur.execute(sqlstr): # returns tuples as specified by querry
                dataobject.append(row)
            print(dataobject)
        except: print(sqlstr, ' query failed.') 
    elif sqlstr == "break": break
    elif sqlstr == "save":
        conn.commit
        break
    else:
        try: cur.execute(sqlstr)
        except: print(sqlstr, ' query failed.')        
cur.close()

#todo: 
#integrate different drivers for different databases.
#consider specific uses for temp portable sqlite in audit.
