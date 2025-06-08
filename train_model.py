import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

df = pd.read_csv("sample_data.csv")
X = df[["amount"]]
y = df["is_fraud"]

model = RandomForestClassifier()
model.fit(X, y)

# Save the model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/fraud_model.pkl")
