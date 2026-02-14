# Logistic Regression for Classification

from sklearn.linear_model import LogisticRegression

hours = [[1], [2], [3], [4], [5]]
passed = [0, 0, 1, 1, 1]
model = LogisticRegression()
model.fit(hours, passed)
prediction = model.predict([[6]])
status = "Passed" if prediction[0] == 1 else "Failed"
print("Predicted class for 6 hours of study:", status)

