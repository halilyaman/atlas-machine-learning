"""
In statistical learning, there is no one specific method which is the
best fit for every data model. So we must decide which method produces
the best results. This can be the most challenging part of performing
statistical learning in practice.
"""

def mse(actual, predictions):
    """
    Mean Squared Error (MSE)

    We must measure how well the predictions match the observed data.
    In regression settings, the most commonly-used measure is the MSE.
    """
    sum = 0
    if len(actual) == len(predictions):
        for i in range(len(actual)):
            sum += (actual[i] - predictions[i]) ** 2
    return sum / len(actual)

def main():
    # dummy data
    actual_data = [15, 16, 21, 34, 45, 56]
    predictions = [15, 19, 23, 30, 49, 55]

    print(mse(actual_data, predictions))


if __name__ == "__main__":
    main()