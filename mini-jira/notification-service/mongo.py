from pymongo import MongoClient

client = MongoClient("mongodb://mongo-notification:27017")
db = client["notification_db"]
collection = db["notifications"]

def save_notification_log(notification):
    result = collection.insert_one(notification)
    print(f"Notification log saved with id: {result.inserted_id}")
