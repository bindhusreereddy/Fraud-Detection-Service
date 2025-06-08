# 💳 Fraud Detection Service (Streamlit + ML)

A simple Python-based microservice that uses a machine learning model to detect fraudulent transactions based on the transaction amount. Built using Streamlit for UI and scikit-learn for fraud prediction.

---

## 🚀 Features

- 🔍 Real-time fraud detection via a Streamlit web app
- 🤖 Machine learning model (Random Forest)
- 📈 Displays fraud probability
- 📝 Logs predictions with timestamp
- 📦 Lightweight and easy to run locally

---

## 🧱 Project Structure

```
fraud-detection-service/
├── fraud_app.py            # Streamlit app
├── train_model.py          # Script to train fraud detection model
├── sample_data.csv         # Example training data
├── model/
│   └── fraud_model.pkl     # Trained ML model (auto-generated)
├── prediction_log.csv      # Logs prediction results (auto-generated)
├── requirements.txt        # Required Python packages
└── .gitignore              # Git ignore settings
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd fraud-detection-service
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv myenv
source myenv/bin/activate     # Linux/macOS
myenv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the ML model

```bash
python train_model.py
```

This will generate a trained `fraud_model.pkl` inside the `model/` folder.

---

## 🖥️ Running the App

```bash
streamlit run fraud_app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧪 Sample Inputs

| Transaction Amount | Prediction  |
|--------------------|-------------|
| 500                | ✅ LEGITIMATE |
| 12000              | 🚨 FRAUDULENT |

---

## 📂 Prediction Log

Each prediction is saved to `prediction_log.csv` with timestamp, amount, label, and probability.

---

## 📌 Notes

- You can modify `sample_data.csv` to include more realistic or complex fraud criteria.
- Extend the model to use features like `user_id`, `sender_account`, `time_of_day`, etc.

---

## 🤖 Model Details

The machine learning model used in this project is a **Random Forest Classifier**, trained using `scikit-learn`.

### 🎯 Features Used:
- `amount`: Transaction amount (float)

### 📊 Model Info:
- Algorithm: RandomForestClassifier
- Training Data: `sample_data.csv` (manually labeled)
- Target: `is_fraud` (1 = Fraud, 0 = Legit)

### 🧠 Behavior:
- The model learns that **very large transactions** are more likely to be fraudulent.
- It outputs both a **binary prediction** (fraud/legit) and a **probability score**.

### 📂 Output:
- A file named `fraud_model.pkl` is generated and used by the Streamlit app for real-time predictions.

## Contact

Created by [Reetesh Nigam](https://github.com/nigamreetesh84)
