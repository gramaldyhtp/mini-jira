from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
db = client["mini_jira"]
inventory_collection = db["inventory"]
