from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fraud Detection API is running"}


def test_predict_high_risk():
    response = client.post("/predict", json={
        "transaction_id": 10,
        "amount": 2000,
        "location": "New York",
        "payment_method": "Credit Card"
    })
    assert response.status_code == 200
    assert response.json()["fraud_flag"] is True


def test_predict_low_risk():
    response = client.post("/predict", json={
        "transaction_id": 11,
        "amount": 100,
        "location": "Boston",
        "payment_method": "Debit Card"
    })
    assert response.status_code == 200
    assert response.json()["fraud_flag"] is False