# This code demonstrates how to use SQL SELECT statements to query data from a SQLite database.

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

print("Name and score:")
cursor.execute("SELECT name, score FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
    
print("\nScore > 80:")
cursor.execute("SELECT * FROM students WHERE score > 80")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nSorted by score DESC:")
cursor.execute("SELECT * FROM students ORDER BY score DESC")
rows = cursor.fetchall()
for row in rows:
    print(row)
