import matplotlib.pyplot as plt

def plot_prediction(actual, predicted, title="Prediction vs Actual"):
    plt.figure(figsize=(10, 5))
    plt.plot(actual, label="Actual")
    plt.plot(predicted, label="Predicted")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
