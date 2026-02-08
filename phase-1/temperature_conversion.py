# This script demonstrates how to convert temperatures between Celsius and Fahrenheit.

celsius = [20, 25, 30, 15, 10]
fahrenheit = []
for temp in celsius:
    f = (temp * 9/5) + 32
    fahrenheit.append(f)
print("Celsius temperatures:", celsius)
print("Fahrenheit temperatures:", fahrenheit)