# This is a mini project that combines the concepts of loops, lists, dictionaries and functions to analyze student scores.

students = [
    {"name": "Nand", "score": 72},
    {"name": "Asha", "score": 85},
    {"name": "Ravi", "score": 90},
    {"name": "Kiran", "score": 60},
    {"name": "Meera", "score": 88}
]

def print_all_students(students):
    for student in students:
        print(student["name"], "scored", student["score"])

def calculate_average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    average = total / len(students)
    return average

def find_high_scorers(students, threshold):
    high_scores = []
    for student in students:
        if student["score"] >= threshold:
            high_scores.append(student["name"])
    return high_scores

def highest_score(students):
    highest = students[0]["score"]
    top_scorer = students[0]["name"]
    for student in students:
        if student["score"] > highest:
            highest = student["score"]
            top_scorer = student["name"]
    return top_scorer, highest

print_all_students(students)

average_score = calculate_average_score(students)
print("Average score:", average_score)

passed_students = find_high_scorers(students, 70)
print("Students who passed (70 and above):", passed_students)

high_scorers = find_high_scorers(students, 85)
print("High scorers (85 and above):", high_scorers)

top_scorer, top_score = highest_score(students)
print("Top scorer:", top_scorer, "with a score of", top_score)