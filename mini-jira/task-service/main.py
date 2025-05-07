from fastapi import FastAPI, HTTPException
from uuid import uuid4
from models import Task
from mongo import task_collection
from kafka_producer import producer

app = FastAPI()

@app.post("/tasks")
def create_task(task: Task):
    task_id = str(uuid4())
    task_dict = task.dict()
    task_dict["_id"] = task_id

    task_collection.insert_one(task_dict)
    producer.send("task_created", task_dict)

    return {"message": "Task created", "task_id": task_id}

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = task_collection.find_one({"_id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["_id"] = str(task["_id"])
    return task

