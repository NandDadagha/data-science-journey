# This script demonstrates basic statistics in Python, including sum, avg, min, max calculations.

scores = [72, 85, 90, 68, 77]

total = sum(scores)
average = total / len(scores)
minimum = min(scores)
maximum = max(scores)

print("Sum:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Rounded Average:", round(average, 2))
print("Absolute Difference between Max and Min:", abs(maximum - minimum))