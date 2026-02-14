# Handling Missing Values in DataFrames

import pandas as pd

data = {
    "score": [72, 85, None, 60, 88],
    "age": [19, 20, 21, None, 22]
}

df = pd.DataFrame(data)
print("Count of Missing Values in the DataFrame:\n", df.isnull().sum())
df = df.fillna(df.mean())
print("\nDataFrame after Filling Missing Values with Mean:\n", df)