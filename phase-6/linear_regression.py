# Linear Regression Example

from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5]]
scores = [50, 60, 70, 80, 90]

model = LinearRegression()
model.fit(hours, scores)
predicted_score = model.predict([[6]])
print("Predicted score for 6 hours of study:", predicted_score[0])

