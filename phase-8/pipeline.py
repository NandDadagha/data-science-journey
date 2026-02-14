# Pipeline is a powerful tool in machine learning that allows you to chain together multiple steps of data processing and modeling into a single, cohesive workflow. This can include steps such as data preprocessing, feature selection, and model training. By using a pipeline, you can ensure that all the steps are executed in the correct order and that the same transformations are applied to both the training and testing data, which helps to prevent data leakage and improve the overall performance of the model.
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
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

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
pipeline.fit(X, Y)
prediction = pipeline.predict([[6, 5]])
print("Predicted Score for 6 hours of study and 5 hours of sleep:", prediction[0])