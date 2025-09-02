from pydantic import BaseModel
from datetime import date

class PolicyBase(BaseModel):
    policy_number: str
    client_id: int
    product_type: str
    start_date: date
    end_date: date
    premium_amount: float

class PolicyCreate(PolicyBase):
    pass

class PolicyUpdate(PolicyBase):
    status: str

class PolicyResponse(PolicyBase):
    id: int
    status: str

    class Config:
        orm_mode = True