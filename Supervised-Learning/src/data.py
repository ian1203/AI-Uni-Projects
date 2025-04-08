import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess(csv_path):
    df = pd.read_csv(csv_path)
    df['Return'] = df.groupby('Stock')['Close'].pct_change()
    df['MA_5'] = df.groupby('Stock')['Close'].transform(lambda x: x.rolling(window=5).mean())
    df['MA_20'] = df.groupby('Stock')['Close'].transform(lambda x: x.rolling(window=20).mean())
    return df.dropna()

def create_sequences(data, sequence_length, pred_horizon, warmup_length=0):
    X_warm, X_seq, y, base_prices = [], [], [], []
    for i in range(len(data) - warmup_length - sequence_length - pred_horizon):
        warm = data[i:i + warmup_length] if warmup_length > 0 else None
        seq = data[i + warmup_length:i + warmup_length + sequence_length]
        target = data[i + warmup_length + sequence_length:i + warmup_length + sequence_length + pred_horizon, 0]
        base_price = data[i + warmup_length + sequence_length, -1]  # Close price
        if warmup_length > 0:
            X_warm.append(warm)
        X_seq.append(seq)
        y.append(target)
        base_prices.append(base_price)
    return np.array(X_warm) if X_warm else None, np.array(X_seq), np.array(y), np.array(base_prices)

def scale_features(train_data, test_data):
    scaler = MinMaxScaler()
    scaler.fit(train_data)
    return scaler.transform(train_data), scaler.transform(test_data), scaler
