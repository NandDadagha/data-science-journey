# Detecting Outliers using the IQR Method

import pandas as pd
data = {
    "score": [72, 85, 90, 60, 88, 200]
}
df = pd.DataFrame(data)
Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['score'] < (Q1 - 1.5 * IQR)) | (df['score'] > (Q3 + 1.5 * IQR))]
print("Outliers in the 'score' column:\n", outliers)