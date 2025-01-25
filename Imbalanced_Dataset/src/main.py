import os
from dataset_visualization import load_and_visualize_data
from train_without_balance import train_without_balance
from train_with_smote import train_with_smote

if __name__ == "__main__":
    # Construct relative path to the dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(os.path.dirname(script_dir), "creditcard.csv")

    # Verify if the dataset exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        # Visualization of data
        data = load_and_visualize_data(file_path)

        # Training without balancing data
        print("\nTraining without balancing data:\n")
        train_without_balance(data)

        # Training with SMOTE
        print("\nTraining model with SMOTE:\n")
        train_with_smote(data)
