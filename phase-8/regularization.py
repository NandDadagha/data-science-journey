# Regularization is a technique used to prevent overfitting in machine learning models by adding a penalty term to the loss function. This penalty discourages the model from fitting the noise in the training data, leading to better generalization on unseen data. Common types of regularization include L1 (Lasso) and L2 (Ridge) regularization.

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
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
model.fit(X, Y)
print("Linear Regression Coefficients:", model.coef_)

# Ridge Regression (L2 Regularization)
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X, Y)
print("Ridge Regression Coefficients:", ridge_model.coef_)