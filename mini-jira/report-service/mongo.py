from pymongo import MongoClient

client = MongoClient("mongodb://mongo-report:27017")
db = client["report_db"]
collection = db["task_reports"]

def save_report_log(report):
    result = collection.insert_one(report)
    print(f"Report log saved with id: {result.inserted_id}")
