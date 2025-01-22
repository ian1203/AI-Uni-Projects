import pandas as pd
import matplotlib.pyplot as plt

def load_and_visualize_data(file_path):
    # Cargar el dataset
    data = pd.read_csv(file_path)

    # Visualización inicial
    print("Distribución de las clases:")
    print(data["Class"].value_counts())

    # Graficar la distribución de las clases
    data["Class"].value_counts().plot(kind="bar", color=["blue", "red"], alpha=0.7)
    plt.title("Distribución de las clases")
    plt.xlabel("Clase")
    plt.ylabel("Número de Transacciones")
    plt.xticks(ticks=[0, 1], labels=["No Fraude", "Fraude"], rotation=0)
    plt.show()

    return data