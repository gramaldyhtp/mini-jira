from pymongo import MongoClient

client = MongoClient("mongodb://mongo-payment:27017")
db = client["payment_db"]
collection = db["payments"]

def save_payment_log(payment_data):
    result = collection.insert_one(payment_data)
    print(f"Saved payment log with id: {result.inserted_id}")
