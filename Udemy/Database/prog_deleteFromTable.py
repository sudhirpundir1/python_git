import mysql.connector as mysql

try:
    conn = mysql.connect(host='127.0.0.1', user='sudhir',password='sudhir', database='test')
    sql ='Delete from test.example where id = %s'
    id =input('Please input id to be deleted :')
    cursor = conn.cursor()
    cursor.execute(sql,(id,))
    conn.commit()
    print(f'Record deleted: {id}')
except mysql.connector.Error as e:
    print('Parameterized query error',e)
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
