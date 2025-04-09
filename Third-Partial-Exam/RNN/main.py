import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from collections import Counter

#Load and clean the IMDB dataset
df = pd.read_csv('IMDB Dataset.csv')

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<br />", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

df['review'] = df['review'].apply(clean_text)
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

# ✅ Tokenize using .split() (no NLTK)
df['tokens'] = df['review'].apply(lambda x: x.split())

# ✅ Build vocabulary (keep top 10,000 words)
all_words = [word for tokens in df['tokens'] for word in tokens]
vocab = Counter(all_words)
vocab = {word: i + 2 for i, (word, _) in enumerate(vocab.most_common(10000))}
vocab['<PAD>'] = 0
vocab['<UNK>'] = 1

# ✅ Encode tokens into integers
def encode_tokens(tokens):
    return [vocab.get(word, vocab['<UNK>']) for word in tokens]

df['encoded'] = df['tokens'].apply(encode_tokens)

# ✅ Pad sequences
MAX_LEN = 200
def pad_sequence(seq):
    if len(seq) > MAX_LEN:
        return seq[:MAX_LEN]
    return seq + [vocab['<PAD>']] * (MAX_LEN - len(seq))

df['padded'] = df['encoded'].apply(pad_sequence)

# ✅ Split data
X = np.array(df['padded'].tolist())
y = df['sentiment'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Custom Dataset class
class IMDBDataset(Dataset):
    def __init__(self, reviews, labels):
        self.reviews = torch.LongTensor(reviews)
        self.labels = torch.FloatTensor(labels)

    def __len__(self):
        return len(self.reviews)

    def __getitem__(self, idx):
        return self.reviews[idx], self.labels[idx]

# ✅ Dataloaders
train_data = IMDBDataset(X_train, y_train)
test_data = IMDBDataset(X_test, y_test)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64)

# ✅ RNN model with bidirectional LSTM
class SentimentRNN(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(SentimentRNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.embedding(x)
        lstm_out, _ = self.lstm(x)
        out = lstm_out[:, -1, :]  # last time step
        out = self.fc(out)
        return self.sigmoid(out).squeeze()

# ✅ Initialize model, loss, and optimizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vocab_size = len(vocab)
model = SentimentRNN(vocab_size, embedding_dim=128, hidden_dim=128, output_dim=1)
model.to(device)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ✅ Training loop
epochs = 5
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch + 1}/{epochs} - Loss: {total_loss:.3f}")

# ✅ Evaluation
model.eval()
all_preds = []
all_labels = []

with torch.no_grad():
    for inputs, labels in test_loader:
        inputs = inputs.to(device)
        outputs = model(inputs)
        preds = (outputs.cpu().numpy() > 0.5).astype(int)
        all_preds.extend(preds)
        all_labels.extend(labels.numpy())

# ✅ Results
acc = accuracy_score(all_labels, all_preds)
print(f"\nTest Accuracy: {acc * 100:.2f}%")
print(classification_report(all_labels, all_preds, target_names=['negative', 'positive']))
