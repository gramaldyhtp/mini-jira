from pydantic import BaseModel

class Notification(BaseModel):
    user_id: str
    task_id: str
    message: str
    status: str
