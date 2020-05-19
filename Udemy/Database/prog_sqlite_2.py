import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
sql = """
    INSERT INTO employees (id,name,department,phone,email) values (1,'John Smith','IT','+9999999','Jsex@gmail.com');
    INSERT INTO employees (id,name,department,phone,email) values (2,'Tony Smith','Sales','+9999999','Js@gmail.com');
    INSERT INTO employees (id,name,department,phone,email) values (3,'Smith','Fi','+9999999','x@gmail.com');
    INSERT INTO employees (id,name,department,phone,email) values (4,'Ok John Smith','Admin','+9999999','Jex@gmail.com');
"""
cursor.executescript(sql)
conn.commit()
conn.close()