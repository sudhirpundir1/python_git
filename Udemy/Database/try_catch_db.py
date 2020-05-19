import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')

    cursor = connection.cursor(prepared=True)
    sql_update_query = """UPDATE Employee set Salary = %s where Id = %s"""

    data_tuple = (12000, 1)
    cursor.execute(sql_update_query, data_tuple)
    connection.commit()
    print("Employee table updated using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")