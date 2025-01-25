import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def train_with_smote(data):
    # Separate features and target variable
    X = data.drop(columns=["Class"])
    y = data["Class"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Scale the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Apply SMOTE to balance the data
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    # Train the model with balanced data
    model = LogisticRegression(max_iter=1500)
    model.fit(X_resampled, y_resampled)

    # Prediction and evaluation
    y_pred = model.predict(X_test)
    print("Classification report (balanced model):")
    print(classification_report(y_test, y_pred))

    # Generate and display the confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()

    return model
