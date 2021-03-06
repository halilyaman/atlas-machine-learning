"""
Simple Linear Regression

Least square line: (Y = B0 + B1*X)
Population regression line: (Y = B0 + B1*X + e)
In real data, population regression line is not known because of error term.

B0 and B1 are coefficients or parameters of the model.
Training data is used to estimate B0 and B1

In terms of linear model:
B0 => intercept
B1 => slope

============================================
Residual Sum of Squares (RSS)

e = y_actual - y_pred
RSS = square(e1) + square(e2) + .... + square(e_n)
RSS = (y1 - B0 - B1*x1)^2 + (y2 - B0 - B1*x2)^2 + (y3 - B0 - B1*x3)^2 + ...

--> MSE = RSS / n
============================================

The least squares approach is used for choosing B0 and B1 to minimize the RSS.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def standard_deviation(data):
    """
    Standard deviation is a measure of how spread out values are.
    It is the square root of variance.

    Variance is calculated by subtracting each values from mean of all values
    and divide the result by total number of values.

    :param data: data that will be observed
    :return: standard deviation value
    """
    mean = np.average(data)
    diff_square = 0

    for i, v in enumerate(data):
        diff_square += (v - mean) ** 2

    variance = diff_square / len(data)
    return np.sqrt(variance)

def rss(data):
    """
    Residual Sum Of Squares

    RSS = sum(square(Y_actual - Y_mean))
    :return: RSS value
    """
    mean = np.average(data)
    rss = 0
    for _, v in enumerate(data):
        rss += (v - mean) ** 2
    return rss



def rse(data):
    """
    Residual Standard Error
    Estimation of square of standard deviation is called as standard error.

    RSE = sqrt(RSS/(n-2))
    :return: RSE value
    """
    return np.sqrt(rss(data) / (len(data) - 2))


def sim_lin_coefficients(input_data, output_data):
    """
    Calculate B0 and B1 based on given dataset.

    :param input_data: predictors
    :param output_data: observed data
    :return: B0 and B1
    """
    if len(input_data) == len(output_data):
        input_average = np.average(input_data)
        output_average = np.average(output_data)
        b1_numerator = 0
        b1_denominator = 0

        for i, _ in enumerate(input_data):
            b1_numerator += (input_data[i] - input_average) * (output_data[i] - output_average)
            b1_denominator += (input_data[i] - input_average) ** 2

        b1 = b1_numerator / b1_denominator
        b0 = output_average - b1 * input_average

        return b0, b1


def data_processing():
    """
    Read data from file and divide it as inputs and outputs

    :return: input and output data
    """
    data = pd.read_csv("dataset/StudentsPerformance.csv")
    input_data = data["math score"]
    output_data = data["reading score"]

    return input_data, output_data

def plot(x, y, b0, b1):
    """
    Plot data points and draw the linear regression line.

    :param x: input data
    :param y: output data
    :param b0: intercept
    :param b1: slope
    """
    plt.plot(x, y, "go")
    plt.plot(x, b0 + x*b1, "r")
    plt.show()

def main():
    # data pre processing
    input_data, output_data = data_processing()
    # calculating coefficients
    b0, b1 = sim_lin_coefficients(input_data, output_data)
    # plotting our results
    plot(input_data, output_data, b0, b1)


if __name__ == "__main__":
    main()