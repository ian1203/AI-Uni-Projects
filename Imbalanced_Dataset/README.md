
# Credit Card Fraud Detection using SMOTE

This project focuses on detecting fraudulent credit card transactions in an imbalanced dataset using machine learning techniques. The dataset is highly imbalanced, with the majority of transactions being legitimate. The project explores two approaches for training a classification model: without balancing the dataset and by applying SMOTE (Synthetic Minority Oversampling Technique).

## Methodology

1. **Data Visualization**:
   The dataset is visualized to understand the distribution of legitimate and fraudulent transactions.

2. **Training without Balancing**:
   A logistic regression model is trained on the raw, imbalanced dataset. Metrics such as precision, recall, and F1-score are evaluated.

3. **Training with SMOTE**:
   SMOTE is applied to balance the dataset by generating synthetic samples for the minority class. The model is trained on the balanced dataset, and its performance is compared to the model trained without balancing.
## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/Imbalanced_Dataset.git
   cd Imbalanced_Dataset
2. **Install Dependencies**
pip install -r requirements.txt
3. **Run the main script**
python src/main.py

## Files
**dataset_visualization.py**: Contains functions for visualizing the dataset.

**train_without_balance.py**: Trains a logistic regression model on the imbalanced dataset.

**train_with_smote.py**: Trains a logistic regression model using SMOTE to balance the dataset.

**main.py**: The entry point for the project. Executes data visualization and model training.

## Dataset

The dataset (**creditcard.csv**) contains transactions made by credit cards in September 2013 by European cardholders. It is highly imbalanced, with only 0.172% of transactions being fraudulent. The dataset was obtained from Kaggle, the owner of the dataset is the Machine Learning Group - ULB. For more context visit the following link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data

## Technologies used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Imbalanced learn (SMOTE)

