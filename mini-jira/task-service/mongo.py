from pymongo import MongoClient

client = MongoClient("mongodb://mongo1:27017")
db = client["mini_jira"]
task_collection = db["tasks"]
