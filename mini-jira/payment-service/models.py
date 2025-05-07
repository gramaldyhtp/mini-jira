from pydantic import BaseModel

class PaymentEvent(BaseModel):
    task_id: str
    user_id: str
    amount: float
    status: str
