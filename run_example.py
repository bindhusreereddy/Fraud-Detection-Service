from fraud_app_controller import FraudDetectionController

def main():
    try:
        # Instantiate the controller
        controller = FraudDetectionController()

        # Example transaction amount
        amount = 100.50

        # Make a prediction
        result = controller.predict(amount)

        # Print results
        print(f"Transaction Amount: ${amount:.2f}")
        print(f"Status: {result['status']}")
        print(f"Fraud Probability: {result['fraud_probability']:.2%}")
        print(f"Is Fraudulent: {result['is_fraudulent']}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()