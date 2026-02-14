# This code evaluates the performance of a logistic regression model using accuracy as the metric. It splits the dataset into training and testing sets, fits the model on the training data, makes predictions on the test set, and calculates the accuracy of those predictions.

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

hours = [[1], [2], [3], [4], [5]]
passed = [0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(hours, passed, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(hours, passed)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
