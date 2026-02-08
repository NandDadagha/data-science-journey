# this script demonstrates how to filter scores based on a condition

scores = [72, 85, 90, 68, 77]
count = 0

for score in scores:
    if score >= 80:
        print("High score:", score)
        count += 1
print("Number of high scores:", count)