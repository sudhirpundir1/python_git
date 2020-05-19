import mysql.connector as mysql

conn = mysql.connect(user='sudhir', password='sudhir',
                     host='127.0.0.1')

sql1 = '''create database test;'''
sql2 = '''CREATE TABLE test.example ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );'''
sql3 = '''INSERT INTO test.example ( id, name ) VALUES ( 1, 'Sample data' );'''
sql4 = '''INSERT INTO test.example ( id, name ) VALUES ( 2, 'Sample data' );'''
cur = conn.cursor()
cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)
cur.execute(sql4)


conn.commit()
conn.close()