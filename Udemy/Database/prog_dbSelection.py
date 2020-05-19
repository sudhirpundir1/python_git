import mysql.connector as mysql

conn = mysql.connect(host='127.0.0.1', user='sudhir',password='sudhir', database='world')

sql = '''select * from world.city where name like "K%";'''
cursor = conn.cursor()

cursor.execute(sql)

for row in cursor.fetchall():
#for row in cursor:
    print(row)