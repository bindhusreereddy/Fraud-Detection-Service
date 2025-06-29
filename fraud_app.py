import streamlit as st
import joblib
import os
import csv
import datetime

# Load model
MODEL_PATH = os.path.join("model", "fraud_model.pkl")
model = joblib.load(MODEL_PATH)

# Streamlit app settings
st.set_page_config(page_title="Fraud Detection App", layout="centered")
st.title("🔍 Transaction Fraud Detection")
st.markdown("Use this tool to detect potentially fraudulent transactions based on amount.")

# Input
amount = st.number_input("Enter Transaction Amount", min_value=0.0, step=0.01)

# Prediction model
if st.button("Check for Fraud"):
    prediction = model.predict([[amount]])[0]
    probability = model.predict_proba([[amount]])[0][1]  # probability of fraud

    st.subheader("Prediction Result:")
    if prediction == 0:
        st.success("✅ LEGITIMATE")
    else:
        st.error("🚨 FRAUDULENT")

    st.metric("Fraud Probability", f"{probability:.2%}")

    # Optional Logging
    with open("prediction_log.csv", "a", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow([datetime.datetime.now(), amount, prediction, f"{probability:.2%}"])
    st.info("Prediction logged successfully.")