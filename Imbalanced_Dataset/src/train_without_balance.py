from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_without_balance(data):
    # Separate features and target variable
    X = data.drop(columns=["Class"])
    y = data["Class"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Training the model
    model = LogisticRegression(max_iter=1500)
    model.fit(X_train, y_train)

    # Prediction and evaluation
    y_pred = model.predict(X_test)
    print("Report of classification (imbalanced model):")
    print(classification_report(y_test, y_pred))

    return model