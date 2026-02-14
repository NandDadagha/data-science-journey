# This code evaluates a linear regression model using mean squared error (MSE) as the metric. It splits the dataset into training and testing sets, fits the model on the training data, makes predictions on the test set, and calculates the MSE to assess the model's performance.

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

hours = [[1], [2], [3], [4], [5]]
scores = [50, 60, 70, 80, 90]

X_train, X_test, y_train, y_test = train_test_split(hours, scores, test_size=0.2, random_state=42)
model = LinearRegression()  
model.fit(X_train, y_train)
predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)