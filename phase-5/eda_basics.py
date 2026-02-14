# Exploratory Data Analysis (EDA) Basics
import pandas as pd

data = {
    "score": [72, 85, 90, 60, 88],
    "age": [19, 20, 21, 19, 22]
}

df = pd.DataFrame(data)
print("Head of the DataFrame:\n", df.head())
print("\nSummary Statistics:\n", df.describe())
print("\nData Types and Non-Null Counts:")
df.info()