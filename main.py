from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Fraud Detection System")


class Transaction(BaseModel):
    transaction_id: int
    amount: float
    location: str
    payment_method: str


@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}


@app.post("/predict")
def predict_fraud(transaction: Transaction):
    if transaction.amount > 1000:
        risk_score = 0.85
        fraud_flag = True
    else:
        risk_score = 0.15
        fraud_flag = False

    conn = sqlite3.connect("fraud_detection.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (transaction_id, amount, location, payment_method, risk_score, fraud_flag)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        transaction.transaction_id,
        transaction.amount,
        transaction.location,
        transaction.payment_method,
        risk_score,
        fraud_flag
    ))

    conn.commit()
    conn.close()

    return {
        "transaction_id": transaction.transaction_id,
        "amount": transaction.amount,
        "risk_score": risk_score,
        "fraud_flag": fraud_flag
    }