# Demonstrates basic SQLite usage: table creation, insertion, and querying.


import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    score INTEGER,
    age INTEGER
    )
''')

cursor.execute("INSERT INTO students (name, age, score) VALUES ('Nand', 19, 72)")
cursor.execute("INSERT INTO students (name, age, score) VALUES ('Asha', 20, 85)")
cursor.execute("INSERT INTO students (name, age, score) VALUES ('Ravi', 21, 90)")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row) 
conn.close()