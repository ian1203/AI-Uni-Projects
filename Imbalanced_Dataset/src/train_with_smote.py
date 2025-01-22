from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_with_smote(data):
    # Separar características y la variable objetivo
    X = data.drop(columns=["Class"])
    y = data["Class"]

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Aplicar SMOTE para balancear los datos
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    # Entrenar el modelo con datos balanceados
    model = LogisticRegression()
    model.fit(X_resampled, y_resampled)

    # Predicción y evaluación
    y_pred = model.predict(X_test)
    print("Reporte de clasificación (modelo balanceado):")
    print(classification_report(y_test, y_pred))

    return model
