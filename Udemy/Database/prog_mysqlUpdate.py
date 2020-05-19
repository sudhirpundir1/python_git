import mysql.connector as mysql
#from mysql.connector import Error

try:
    conn = mysql.connect(host='127.0.0.1', user='sudhir',password='sudhir', database='test')
    cursor = conn.cursor()
    sql ='update test.example set name=%s where id = %s'
    record =("Himanchal",1)
    cursor.execute(sql, record)
    conn.commit()
    print('Record successfully updated..!')
except mysql.connector.Error as e:
    print("parameterized query failed {}".format(e))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
