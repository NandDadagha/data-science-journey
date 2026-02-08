# This script demonstrates basics of functions in Python.

scores = [72, 85, 90, 68, 77]
def calculate_average(scores):
    total = 0
    for num in scores:
        total += num
    average = total / len(scores)
    return average

average = calculate_average(scores)
print("Average score:", average)