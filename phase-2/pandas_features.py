# This script demonstrates features of Pandas, a powerful library for data manipulation and analysis in Python.
import pandas as pd

data = {
    "name": ["Nand", "Asha", "Ravi"],
    "score" : [72, 85, 90],
    "age": [19, 20, 21]
}

df = pd.DataFrame(data)
df["passed"] = df["score"] >= 70

df["score_bonus"] = df["score"] + 5

print("DataFrame with new columns:")
print(df)