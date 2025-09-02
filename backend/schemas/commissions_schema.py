from pydantic import BaseModel
from datetime import date

class CommissionBase(BaseModel):
    agent: str
    policy: str
    amount: float
    rate: float
    payment_date: date
    status: str

class CommissionCreate(CommissionBase):
    pass

class CommissionUpdate(CommissionBase):
    pass

class CommissionOut(CommissionBase):
    id: int

    class Config:
        orm_mode = True