# Feature Scaling

from sklearn.preprocessing import StandardScaler
import pandas as pd
data = {
    "hours": [1,2,3,4,5,6,7,8],
    "sleep": [8,7,6,6,5,5,4,4],
    "score": [50,55,65,70,75,85,90,95]
}

df = pd.DataFrame(data)

X = df.drop("score", axis=1)
Y = df["score"]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)
scaled_df = pd.DataFrame(scaled_data, columns=X.columns)
print(scaled_df)