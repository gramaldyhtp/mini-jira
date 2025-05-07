from pymongo import MongoClient

client = MongoClient("mongodb://mongo-audit:27017")
db = client["audit_db"]
collection = db["audit_logs"]

def save_audit_log(audit_data):
    result = collection.insert_one(audit_data)
    print(f"Audit log saved with id: {result.inserted_id}")
