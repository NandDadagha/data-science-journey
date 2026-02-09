# This code demonstrates how to use the groupby function in Pandas to group data based on a specific column and perform aggregate operations on the grouped data.
import pandas as pd

data = {
    "name": ["Nand", "Asha", "Ravi"],
    "score" : [72, 85, 90],
    "age": [19, 20, 21]
}

df = pd.DataFrame(data)
df["passed"] = df["score"] >= 70
avg_score = df.groupby("passed")["score"].mean()
print("Average score based on pass status:")
print(avg_score)