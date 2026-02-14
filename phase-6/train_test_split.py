# This code demonstrates how to use the train_test_split function from scikit-learn to split a dataset into training and testing sets, and then fit a linear regression model to the training data and make predictions on the test data.

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

hours = [[1], [2], [3], [4], [5]]
scores = [50, 60, 70, 80, 90]

X_train, X_test, y_train, y_test = train_test_split(hours, scores, test_size=0.2, random_state=42)
model = LinearRegression()  
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Test Features (Hours):", X_test)
print("Actual Scores:", y_test)
print("Predicted Scores:", predictions)