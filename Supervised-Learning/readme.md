# 📈 Supervised Learning - Stock Price Prediction with LSTM
A Deep Learning Time Series Model using PyTorch

## 🧠 Overview

This project implements a multi-step stock price forecasting model using a deep learning architecture (Seq2Seq LSTM) trained on historical price data with technical indicators. The model uses a warm-up sequence to prime memory and features learnable initial hidden states to improve long-term pattern recognition.

---

## ✅ Features

- Supervised learning approach for time series forecasting  
- Predicts 15-day price movements from past stock behavior  
- Built with PyTorch and modularized for clarity and extensibility  
- Supports warm-up (priming) sequences for improved memory context  
- Optional learnable hidden/cell states for personalized sequence memory  
- Feature engineering includes returns and moving averages  
- Evaluation with MAE and RMSE  
- Visual plots of actual vs predicted stock price trajectories

---

## 📁 Project Structure

```text
src/
├── data.py → Data loading, feature engineering, and sequence generation
├── model.py → Seq2Seq LSTM model with optional learnable initial states
├── train.py → Training and evaluation logic (MAE, RMSE, forward passes)
├── utils.py → Plotting utility
├── main.py → Main training script looping over stocks
└── stock_data.csv → Dataset with historical stock prices
```

---

## 🧬 Model Architecture

- Input: [Return, MA_5, MA_20, Close] over a 30-day window  
- Warm-up: 15-day optional historical context to prime the LSTM  
- Model: 2-layer LSTM → Fully connected → 15-day return forecast  
- Output: Sequence of daily returns → Reconstructed into predicted prices  
- Training Objective: Minimize MSE over predicted vs actual future returns

---

## ⚙️ How It Works

1. Each stock’s data is preprocessed to compute daily return, 5-day and 20-day moving averages.  
2. Sequences are created with optional warm-up context to improve temporal memory.  
3. The LSTM model is trained to predict a sequence of future returns.  
4. Predictions are reconstructed into real price trajectories using the last known close price.  
5. Performance is evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

---

## 📊 Sample Results

| Stock | MAE    | RMSE   |
|-------|--------|--------|
| TSLA  | 9.03   | 21.02  |
| AAPL  | 23.00  | 58.94  |
| MSFT  | 23.69  | 69.83  |

MAE = average deviation from actual price  
RMSE = penalizes large deviations more strongly  

---

## 🚀 Getting Started

1. Clone this repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
3. Place your stock_data.csv in the /src folder
4. Run the project:
   ```bash
   python main.py

## 📦 Requirements

- Python 3.8+

- PyTorch

- NumPy

- pandas

- scikit-learn

- matplotlib