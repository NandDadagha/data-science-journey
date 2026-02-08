# this script demonstrates the basics of lists in Python

temperatures = [30, 32, 29, 35, 31]

print("First temperature:", temperatures[0])
print("Last temperature:", temperatures[-1])
print("Number of readings:", len(temperatures))


temperatures[2] = 33
temperatures.append(28)

print("Updated temperatures:", temperatures)