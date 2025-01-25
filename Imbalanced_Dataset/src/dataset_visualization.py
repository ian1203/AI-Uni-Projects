import pandas as pd
import matplotlib.pyplot as plt

def load_and_visualize_data(file_path):
    # Reading dataset
    data = pd.read_csv(file_path)

    # Initial visualization
    print("Distribución de las clases:")
    print(data["Class"].value_counts())

    # Graph of distribution of classes
    data["Class"].value_counts().plot(kind="bar", color=["blue", "red"], alpha=0.7)
    plt.title("Distribution of classes")
    plt.xlabel("Class")
    plt.ylabel("Number of transactions")
    plt.xticks(ticks=[0, 1], labels=["Not Fraud", "Fraud"], rotation=0)
    plt.show()

    return data