# This code demonstrates selection techniques in Pandas, allowing you to access specific rows and columns of a DataFrame.

import pandas as pd

data = {
    "name": ["Nand", "Asha", "Ravi"],
    "score" : [72, 85, 90],
    "age": [19, 20, 21]
}

df = pd.DataFrame(data)
print("Score: ")
print(df["score"])
print("Name and Score:")
print(df[["name", "score"]])
print("Students with score > 80:")
print(df[df["score"] > 80])