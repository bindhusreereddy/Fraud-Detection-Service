import joblib
import os
import csv
import datetime

class FraudDetectionController:
    def __init__(self, model_path=os.path.join("model", "fraud_model.pkl")):
        """Initialize the controller with the fraud detection model."""
        self.model = self._load_model(model_path)
        self.log_file = "prediction_log.csv"

    def _load_model(self, model_path):
        """Load the fraud detection model."""
        try:
            return joblib.load(model_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Model file not found at {model_path}")
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

    def predict(self, amount):
        """Predict if a transaction is fraudulent based on the amount."""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number")

        # Make prediction
        prediction = self.model.predict([[amount]])[0]
        probability = self.model.predict_proba([[amount]])[0][1]  # Probability of fraud

        # Log prediction
        self._log_prediction(amount, prediction, probability)

        return {
            "is_fraudulent": bool(prediction),
            "fraud_probability": probability,
            "status": "LEGITIMATE" if prediction == 0 else "FRAUDULENT"
        }

    def _log_prediction(self, amount, prediction, probability):
        """Log prediction details to a CSV file."""
        try:
            with open(self.log_file, "a", newline="") as log_file:
                writer = csv.writer(log_file)
                writer.writerow([datetime.datetime.now(), amount, prediction, f"{probability:.2%}"])
        except Exception as e:
            raise Exception(f"Error logging prediction: {str(e)}")