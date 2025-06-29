from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fraud_app_controller import FraudDetectionController

# Initialize FastAPI app
app = FastAPI(title="Fraud Detection API", description="API for detecting fraudulent transactions", version="1.0.0")

# Initialize the fraud detection controller
controller = FraudDetectionController()

# Define input model for request validation
class TransactionInput(BaseModel):
    amount: float

# Define response model
class TransactionResponse(BaseModel):
    is_fraudulent: bool
    fraud_probability: float
    status: str

@app.post("/predict", response_model=TransactionResponse)
async def predict_fraud(transaction: TransactionInput):
    try:
        # Validate amount
        if transaction.amount < 0:
            raise HTTPException(status_code=400, detail="Amount must be non-negative")

        # Get prediction from controller
        result = controller.predict(transaction.amount)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}