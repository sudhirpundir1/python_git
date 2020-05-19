import mysql.connector

conn = mysql.connector.connect(user='sudhir', password='sudhir',
                              host='127.0.0.1',
                              database='world')

cursor = conn.cursor()
cursor.execute('SELECT * FROM world.city')

for row in cursor:
    print(row)
