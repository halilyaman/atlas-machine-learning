import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading csv file
data = pd.read_csv("dataset/team.csv", encoding="ISO-8859-1")

# Converting predictor columns to numpy array
age = np.array(data["Age"])
experience = np.array(data["Experience"])
power = np.array(data["Power"])
ones = np.ones((1, 18))

# Forming a matrix
inputs = np.vstack((ones, age, experience, power)).T

# Output vector
outputs = np.array(data["Salary"])

# Calculating coefficients
coefficients = np.linalg.inv(inputs.T.dot(inputs)).dot(inputs.T.dot(outputs))

# Making a prediction using estimated coefficients
predictions = inputs.dot(coefficients)

# Calculating error margins
error_margins = np.abs(outputs - predictions)

# Plotting error margins vs predictions
plt.plot(predictions, error_margins, "go")
plt.show()

# Generating new column containing randomly between -500, 500
new_column = np.random.randint(-500, 500, 18)

# Calculating new coefficients and new predictions using new column
new_inputs = np.vstack((inputs.T, new_column)).T
new_coefficients = np.linalg.inv(new_inputs.T.dot(new_inputs)).dot(new_inputs.T.dot(outputs))
new_predictions = new_inputs.dot(new_coefficients)

def r_square(actual, estimated):
    rss = 0
    tss = 0
    actual_mean = np.average(actual)

    for i, v in enumerate(actual):
        rss += (actual[i] - estimated[i]) ** 2
        tss += (actual[i] - actual_mean) ** 2
    return 1 - (rss / tss)

print("Showing original results:")
print("R^2 Score:", r_square(outputs, predictions))
print("Showing results with an added random column:")
print("R^2 Score:", r_square(outputs, new_predictions))


