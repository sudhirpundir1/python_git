import mysql.connector as mysql
from mysql.connector import Error
try:
    conn = mysql.connect(host='127.0.0.1', user='sudhir',password='sudhir', database='test')
    record = (15,"Agra")
    cursor = conn.cursor()

    sql ='insert into test.example (id,name) values( %s,%s)'

    cursor.execute(sql, record)
    conn.commit()

sql ='''select * from test.example'''
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)