from pydantic import BaseModel

class Report(BaseModel):
    task_id: str
    title: str
    updated_by: str
    status: str
    timestamp: str
