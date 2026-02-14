# Demonstrates a basic EDA and data cleaning pipeline using Pandas and Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "score": [72, 85, None, 60, 88, 200],
    "age": [19, 20, 21, None, 22, 19]
}

df = pd.DataFrame(data)

print("Dataset info:")
df.info()

print("\nDataset summary:")
print(df.describe())


df.fillna(df.mean(), inplace=True)

Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['score'] < (Q1 - 1.5 * IQR)) | (df['score'] > (Q3 + 1.5 * IQR))]
print("Outliers in the 'score' column:\n", outliers)

plt.hist(df['score'], bins=5, edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score Ranges')
plt.ylabel('Frequency')
plt.show()