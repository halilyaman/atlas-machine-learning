import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the csv file
data = pd.read_csv("dataset/teams_comb.csv", encoding="ISO-8859-1")
# size of the data
size = len(data)
# k value
k = 10
# estimations stored
cv_hat = np.array([])

# Splitting the columns
age = np.array(data["Age"])
experience = np.array(data["Experience"])
power = np.array(data["Power"])
salary = np.array(data["Salary"])
ones = np.ones((1, size))

# Forming an input matrix
input_data = np.vstack((ones, age, experience, power)).T

# Finding the coefficients
def cal_coef(train_input, train_output):
    coefficients = np.linalg.inv(train_input.T.dot(train_input)).dot(train_input.T).dot(train_output)
    return coefficients

# Making an estimation
def estimate(coefficients, input_data):
    return input_data.dot(coefficients)

# MSE calculation
def mse(estimated_values, actual_values):
    sum = 0
    for i, _ in enumerate(actual_values):
        sum += (estimated_values[i] - actual_values[i]) ** 2
    return sum / len(actual_values) 

# loop for cross validation
current_index = 0
step = int(size / k)
for i in range(k):
    # split train and test data
    train_input = np.delete(input_data, np.s_[current_index: current_index+step], 0)
    train_output = np.delete(salary, np.s_[current_index: current_index+step], 0)
    test_input = input_data[current_index: current_index+step]
    # calculate coefficients and make an estimation
    coefficients = cal_coef(train_input, train_output)
    estimation = estimate(coefficients, test_input)
    # store the estimation
    cv_hat = np.append(cv_hat, estimation)
    # next fold
    current_index += step

# estimation without cross-validation
y_hat = estimate(cal_coef(input_data, salary), input_data)

print("MSE with cross-validation:", mse(cv_hat, salary))
print("MSE without cross-validation:", mse(y_hat, salary))
# calculate errors for each prediction
cv_errors = np.abs(cv_hat - salary)
y_errors = np.abs(y_hat - salary)

# plotting errors for with-cv and without-cv
plt.figure()
plt.xlabel("Predictions")
plt.ylabel("Errors for predictions")
plt.scatter(x=y_hat, y=y_errors, c="b", label="Without CV")
plt.scatter(x=cv_hat, y=cv_errors, c="r", label="With CV")
plt.legend(loc="upper right")

# plotting cv_hat VS y_hat
plt.figure()
plt.xlabel("Prediction without cross-validation")
plt.ylabel("Prediction with cross-validation")
plt.scatter(x=y_hat, y=cv_hat, c="g")
# drawing y=x line
plt.plot(salary, salary)
plt.show()
