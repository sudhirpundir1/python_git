import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9INLG1K\DEV01;'
                      'Database=AdventureWorks;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM humanresources.Employee_test')

for row in cursor:
    print(row)

