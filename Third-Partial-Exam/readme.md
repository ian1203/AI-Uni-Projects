# 🧠 Third Partial Exam – AI & Machine Learning

This project contains the solutions for all three exercises of the third partial exam. Each section includes a machine learning or deep learning model built using PyTorch and standard libraries like pandas, scikit-learn, and matplotlib.

---

## 📁 Contents

- **Exercise 1: Decision Tree on Iris Dataset**
- **Exercise 2: CNN on CIFAR-10 (PyTorch)**
- **Exercise 3: RNN on IMDB Movie Reviews (PyTorch)**

---

## ✅ Exercise 1: Decision Tree (Iris Dataset)

### 🔍 Objective:
- Train a decision tree classifier on the Iris dataset with a maximum depth of 3.
- Report the test accuracy and show the confusion matrix.

### 💡 Method:
- Data is split into training (80%) and testing (20%).
- A `DecisionTreeClassifier` with `max_depth=3` is used.
- The model is evaluated using accuracy and a confusion matrix.
- The decision tree is also visualized for interpretability.

### 📊 Example Results:
- **Accuracy:** 100%
- **Confusion Matrix:** Perfect classification on test set

### How can we avoid overfitting in decision trees?

**Answer:**

To avoid overfitting in decision trees, you can:
- **Limit the maximum depth** of the tree (as done in this exercise with `max_depth=3`).
- **Use pruning** techniques like `min_samples_split`, `min_samples_leaf`, or `max_leaf_nodes`.
- **Use cross-validation** instead of relying on a single train/test split to get a more reliable performance estimate.
- **Consider ensemble models** like Random Forests, which reduce variance and improve generalization.

---

## ✅ Exercise 2: CNN (CIFAR-10 Dataset)

### 🔍 Objective:
- Build a simple CNN using PyTorch to classify images from the CIFAR-10 dataset.
- Include 1 convolutional layer, 1 max pooling layer, 1 dense layer with dropout.
- Visualize the learned filters from the first convolutional layer.

### 💡 Model Architecture:
- Conv2D (32 filters, 3x3 kernel) + ReLU
- MaxPooling (2x2)
- Dense layer (128 units) + ReLU + Dropout (20%)
- Output layer (10 classes, softmax via `CrossEntropyLoss`)

### 🧪 Results:
- **Test Accuracy:** ~65% (can vary slightly by run)
- **Bonus:** Learned filters from the first conv layer were visualized using `matplotlib`.

---

## ✅ Exercise 3: RNN (IMDB Movie Reviews)

### 🔍 Objective:
- Train an RNN with an LSTM layer for binary sentiment classification.
- Dataset: IMDB (movie reviews labeled as positive/negative).
- Use an embedding layer, LSTM, and dense output.

### 💡 Model Architecture:
- Embedding Layer (vocab size = 10,000, embedding dim = 128)
- Bidirectional LSTM Layer (hidden size = 128)
- Fully Connected Layer (1 output neuron)
- Sigmoid activation for binary classification

### 🛠 Preprocessing:
- Reviews were cleaned, lowercased, and tokenized using Python's `.split()` (no NLTK).
- Tokens were converted into integer sequences using a vocabulary.
- Sequences were padded to a fixed length of 200.

### 🧪 Results:
- **Test Accuracy:** ~85–90%
- **Classification Report:** Includes precision, recall, and F1-score
- **Bonus:** A **bidirectional LSTM** was implemented to capture both forward and backward context.

---

## 🚀 How to Run

1. Make sure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install torch torchvision pandas matplotlib scikit-learn
   ```
3. Run each script individually:
   - `Decision Tree`: `python decision_tree.py`
   - `CNN`: `python cnn.py`
   - `RNN`: `python rnn.py`

---

## 📌 Notes

- All models were built using **PyTorch** (no TensorFlow required).
- The CNN and RNN are relatively simple to meet assignment requirements but can be extended easily.
- NLTK was removed in the final RNN version to avoid tokenizer issues.

---

## 📚 Author

**Ian Vicente**  
Third Partial Exam – Artificial Intelligence / Machine Learning  
2025  
