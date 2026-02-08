# This script demonstrates the use of loops, lists and dictionaries together in Python.

students = [
    {"name": "Nand", "score": 72},
    {"name": "Asha", "score": 85},
    {"name": "Ravi", "score": 90}
]
for student in students:
    print(student["name"], "scored", student["score"])

for student in students:
    if student["score"] >= 80:
        print("High scorer:", student["name"])