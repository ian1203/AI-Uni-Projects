import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from model import Seq2SeqLSTM
from data import load_and_preprocess, create_sequences, scale_features
from train import train, evaluate
from utils import plot_prediction
import numpy as np

CSV_PATH = "stock_data.csv"
STOCKS = ['AAPL', 'TSLA', 'MSFT']
SEQUENCE_LENGTH = 30
PREDICTION_HORIZON = 15
WARMUP_LENGTH = 15
EPOCHS = 100
BATCH_SIZE = 64
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


df = load_and_preprocess(CSV_PATH)
features = ['Return', 'MA_5', 'MA_20', 'Close']

for stock in STOCKS:
    print(f"\nTraining on {stock}...")
    df_stock = df[df['Stock'] == stock]
    data = df_stock[features].values.astype(np.float32)
    train_size = int(len(data) * 0.8)
    train_data, test_data = data[:train_size], data[train_size - WARMUP_LENGTH - SEQUENCE_LENGTH - PREDICTION_HORIZON:]
    scaled_train, scaled_test, scaler = scale_features(train_data, test_data)

    warm_train, X_train, y_train, _ = create_sequences(scaled_train, SEQUENCE_LENGTH, PREDICTION_HORIZON, WARMUP_LENGTH)
    warm_test, X_test, y_test, base_prices = create_sequences(scaled_test, SEQUENCE_LENGTH, PREDICTION_HORIZON, WARMUP_LENGTH)

    X_train_tensor = torch.tensor(X_train, dtype=torch.float32).to(DEVICE)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).to(DEVICE)
    warm_train_tensor = torch.tensor(warm_train, dtype=torch.float32).to(DEVICE) if warm_train is not None else None

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor, warm_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

    model = Seq2SeqLSTM(input_size=len(features), output_len=PREDICTION_HORIZON, learn_init_state=True).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    train(model, train_loader, criterion, optimizer, epochs=EPOCHS)

    X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(DEVICE)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).to(DEVICE)
    warm_test_tensor = torch.tensor(warm_test, dtype=torch.float32).to(DEVICE) if warm_test is not None else None

    mae, rmse, preds, actuals = evaluate(model, X_test_tensor, y_test_tensor, base_prices, warm=warm_test_tensor)
    print(f"{stock} - MAE: {mae:.2f}, RMSE: {rmse:.2f}")
    plot_prediction(actuals[0], preds[0], title=f"{stock} Prediction vs Actual")
