from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URI)
db = client["mini_jira"]
logs_collection = db["activity_logs"]

def save_log(log_data):
    logs_collection.insert_one(log_data)
