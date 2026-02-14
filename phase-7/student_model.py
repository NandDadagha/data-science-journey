from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
data = {
    "hours": [1,2,3,4,5,6,7,8],
    "sleep": [8,7,6,6,5,5,4,4],
    "score": [50,55,65,70,75,85,90,95]
}

df = pd.DataFrame(data)

print("Dataset head:")
print(df.head())

print("\nDataset summary:")
print(df.describe())

features = df[["hours", "sleep"]]
target = df["score"]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("\nPredictions on test set:")
print(predictions)
print("\nActual scores on test set:")
print(y_test.values)