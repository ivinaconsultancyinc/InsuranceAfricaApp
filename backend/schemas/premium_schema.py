from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PremiumBase(BaseModel):
    policy_id: str
    customer_id: int
    amount: float
    currency: str
    due_date: datetime
    payment_date: Optional[datetime] = None
    status: Optional[str] = "Pending"

class PremiumCreate(PremiumBase):
    pass

class PremiumUpdate(BaseModel):
    policy_id: Optional[str]
    customer_id: Optional[int]
    amount: Optional[float]
    currency: Optional[str]
    due_date: Optional[datetime]
    payment_date: Optional[datetime]
    status: Optional[str]

class PremiumOut(PremiumBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
