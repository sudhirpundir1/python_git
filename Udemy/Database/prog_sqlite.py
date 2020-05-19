import sqlite3

connection = sqlite3.connect('mydatabase.db')

c = connection.cursor()


sql = """
        CREATE TABLE IF NOT EXISTS employees (
         id INTEGER,
         name VARCHAR(64),
         department VARCHAR(32),
         phone VARCHAR(16),
         email VARCHAR(32)
        )
        """

## Execute the sql against the database (db)
c.execute(sql)

## Committing the changes
connection.commit()

## Closing the connection to the database
connection.close()
