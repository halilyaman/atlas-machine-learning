"""
In statistical learning, there is no one specific method which is the
best fit for every data model. So we must decide which method produces
the best results. This can be the most challenging part of performing
statistical learning in practice.

The Bias-Variance Trade-Off
E(y0 - f^(x0))^2 = Var(f^(x0)) + [Bias(f(x0))]^2 + Var(e)

Goal is to find low bias and low variance.
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

def training_error(actual, prediction):
    """
    Quantifying the accuracy in classification settings.

    Average(I(y_pred != y_true))

    Compare estimated and true values. If y_pred == y_true,
    then it is equal to 0, otherwise it is 1.
    """
    sum = 0
    if len(actual) == len(prediction):
        for i, v in enumerate(actual):
            if v != prediction[i]:
                sum += 1
    return sum / len(actual)

def main():
    # dummy data for calculating MSE
    actual_data = [15, 16, 21, 34, 45, 56]
    predictions = [15, 19, 23, 30, 49, 55]
    print("MSE:", mse(actual_data, predictions))

    # dummy data for classification setting
    cls_actual = ["Left", "Right", "Up", "Down"]
    cls_pred = ["Left", "Down", "Up", "Down"]
    print("Classification Error:", training_error(cls_actual, cls_pred))



if __name__ == "__main__":
    main()