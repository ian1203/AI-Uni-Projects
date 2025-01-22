from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_without_balance(data):
    # Separar características y la variable objetivo
    X = data.drop(columns=["Class"])
    y = data["Class"]

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Entrenar el modelo
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predicción y evaluación
    y_pred = model.predict(X_test)
    print("Reporte de clasificación (modelo desbalanceado):")
    print(classification_report(y_test, y_pred))

    return model