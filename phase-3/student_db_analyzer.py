# Mini Project: Student Database Analyzer

# In this mini project, you will create a simple student database using SQLite and perform various analyses on the data. You will create a table to store student information, insert sample data, and then write SQL queries to analyze the data.

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
cursor.execute("INSERT INTO students (name, age, score) VALUES ('Kiran', 19, 60)")
cursor.execute("INSERT INTO students (name, age, score) VALUES ('Meera', 22, 88)")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("All students:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM students WHERE score >= 80")
print("\nStudents with score >= 80:")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT AVG(score) FROM students")
avg_score = cursor.fetchone()[0]
print("\nAverage score:", avg_score)

cursor.execute("SELECT age, AVG(score) FROM students GROUP BY age")
print("\nAverage score by age:")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()