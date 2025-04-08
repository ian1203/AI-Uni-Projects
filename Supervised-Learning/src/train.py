import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train(model, train_loader, criterion, optimizer, epochs=50):
    model.train()
    for epoch in range(epochs):
        for batch in train_loader:
            X, y, warm = batch
            optimizer.zero_grad()
            output = model(X, warm_up=warm if warm is not None else None)
            loss = criterion(output, y)
            loss.backward()
            optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

def evaluate(model, X_seq, y_true, base_prices, warm=None):
    model.eval()
    with torch.no_grad():
        predictions = model(X_seq, warm_up=warm if warm is not None else None).cpu().numpy()
    y_preds, y_actuals = [], []
    for i, base in enumerate(base_prices):
        y_preds.append(base * np.cumprod(1 + predictions[i]))
        y_actuals.append(base * np.cumprod(1 + y_true[i]))
    mae = mean_absolute_error(np.concatenate(y_actuals), np.concatenate(y_preds))
    rmse = np.sqrt(mean_squared_error(np.concatenate(y_actuals), np.concatenate(y_preds)))
    return mae, rmse, y_preds, y_actuals
