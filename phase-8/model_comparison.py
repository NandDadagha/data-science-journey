# Model Comparison is the process of evaluating and comparing the performance of different machine learning models on a given dataset. This can be done using various metrics such as accuracy, precision, recall, F1 score, or mean squared error, depending on the type of problem (classification or regression). By comparing models, you can identify which one performs best for your specific use case and make informed decisions about which model to deploy in production.

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import pandas as pd

data = {
    "hours": [1,2,3,4,5,6,7,8],
    "sleep": [8,7,6,6,5,5,4,4],
    "score": [50,55,65,70,75,85,90,95]
}
df = pd.DataFrame(data)

X = df.drop("score", axis=1)
Y = df["score"]

# Linear Regression
model = LinearRegression()
lr_scores = cross_val_score(model, X, Y, cv=4)
print("average score for linear regression:", lr_scores.mean())

# Ridge Regression (L2 Regularization)
ridge_model = Ridge(alpha=1.0)
ridge_scores = cross_val_score(ridge_model, X, Y, cv=4)
print("average score for ridge regression:", ridge_scores.mean())