# AI-Powered Fraud Detection System for Financial Transactions

## Project Overview
This project is a simple fraud detection prototype built for CS 620 Software System Design. It accepts transaction data through a FastAPI endpoint, assigns a fraud risk score, flags suspicious transactions, and stores results in a SQLite database.

## Features
- Accepts transaction data through API
- Predicts fraud risk using rule-based logic
- Flags high-risk transactions
- Stores transaction records in a database
- Includes automated tests

## Technologies Used
- Python
- FastAPI
- SQLite
- Pytest
- Uvicorn

## Files
- `main.py` - main API
- `database.py` - database setup
- `test_app.py` - automated tests
- `fraud_detection.db` - SQLite database
- `requirements.txt` - project dependencies

## How to Run
1. Install dependencies:
   `pip install -r requirements.txt`

2. Create the database:
   `python database.py`

3. Start the API:
   `uvicorn main:app --reload`

4. Open API docs in browser:
   `http://127.0.0.1:8000/docs`

## How to Run Tests
`pytest`

## Sample Prediction Rule
- Amount above 1000 = high risk
- Amount 1000 or below = low risk   