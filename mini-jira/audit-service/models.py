from pydantic import BaseModel

class AuditLog(BaseModel):
    user_id: str
    action: str
    target: str
    timestamp: str
    metadata: dict
