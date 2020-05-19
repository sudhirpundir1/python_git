import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1', user='sudhir',password='sudhir', database='test')

    cursor = connection.cursor()
    sql_insert_query = """insert into test.example (id,name) values( %s,%s)"""

    insert_tuple_1 = (5, "Json")
    insert_tuple_2 = (6, "Emma")

    cursor.execute(sql_insert_query, insert_tuple_1)
    cursor.execute(sql_insert_query, insert_tuple_2)
    connection.commit()
    print("Data inserted successfully into employee table using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")