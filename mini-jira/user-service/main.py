from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

users_db = {}

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    user_id = str(uuid4())
    users_db[user_id] = {**user.dict(), "id": user_id}
    return users_db[user_id]

@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
