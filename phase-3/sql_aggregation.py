# This code demonstrates how to use SQL aggregation functions such as AVG and COUNT to perform calculations on data in a SQLite database.

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

cursor.execute("SELECT AVG(score) FROM students")
avg_score = cursor.fetchone()[0]
print("Average score:", avg_score)

cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]
print("Number of students:", count)

cursor.execute("SELECT AVG(score) FROM students WHERE score >= 70")
avg_above_70 = cursor.fetchone()[0]
print("Average score for students with score >= 70:", avg_above_70)