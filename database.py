import sqlite3

conn = sqlite3.connect("fraud_detection.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id INTEGER,
    amount REAL,
    location TEXT,
    payment_method TEXT,
    risk_score REAL,
    fraud_flag BOOLEAN
)
""")

conn.commit()
conn.close()

print("Database and table created successfully.")