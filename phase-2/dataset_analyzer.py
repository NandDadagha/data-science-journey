# Dataset Analyzer: demonstrates DataFrame creation,
# feature engineering, filtering, and aggregation using Pandas.


import pandas as pd
data = {
    "name": ["Nand", "Asha", "Ravi", "Kiran", "Meera"],
    "score": [72, 85, 90, 60, 88],
    "age": [19, 20, 21, 19, 22]
}
df = pd.DataFrame(data)
df["passed"] = df["score"] >= 70
df["score_bonus"] = df["score"] + 5

print("DataFrame with new columns:")
print(df)

print("Shape")
print(df.shape)

print("Columns")
print(df.columns.tolist())

score_above_80 = df[df["score"] > 80]
print("Students with score above 80:")
print(score_above_80)

avg_score_by_passed = df.groupby("passed")["score"].mean()
print("Average score by pass status:")
print(avg_score_by_passed)

highest_score = df["score"].max()
print("Highest score:")
print(highest_score)