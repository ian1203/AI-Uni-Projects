from dataset_visualization import load_and_visualize_data
from train_without_balance import train_without_balance
from train_with_smote import train_with_smote

if __name__ == "__main__":
    # Ruta al archivo del dataset
    file_path = "/Users/ianvicente/Desktop/Pycharm Projects/AI-Uni-Projects/Imbalanced_Dataset/creditcard.csv"

    # Cargar y visualizar los datos
    data = load_and_visualize_data(file_path)

    # Entrenamiento sin balancear los datos
    print("\nEntrenando modelo sin balance de datos:\n")
    train_without_balance(data)

    # Entrenamiento con SMOTE
    print("\nEntrenando modelo con SMOTE:\n")
    train_with_smote(data)
