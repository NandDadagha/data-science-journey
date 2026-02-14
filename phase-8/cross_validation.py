# Cross Validation is a technique used to evaluate the performance of a machine learning model by splitting the data into multiple subsets (folds) and training/testing the model on different combinations of these subsets. This helps to ensure that the model's performance is not dependent on a specific subset of the data and provides a more reliable estimate of its generalization ability.

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import pandas as pd
data = {
    "hours": [1,2,3,4,5,6,7,8],
    "sleep": [8,7,6,6,5,5,4,4],
    "score": [50,55,65,70,75,85,90,95]
}
df = pd.DataFrame(data)

X = df.drop("score", axis=1)
Y = df["score"]
model = LinearRegression()
scores = cross_val_score(model, X, Y, cv=4)
print("Cross Validation Scores:", scores)
print("Average Cross Validation Score:", scores.mean())