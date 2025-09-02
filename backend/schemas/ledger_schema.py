from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LedgerBase(BaseModel):
    account_id: str
    account_name: str
    account_type: str
    currency: str
    balance: float
    status: Optional[str] = "Active"

class LedgerCreate(LedgerBase):
    pass

class LedgerUpdate(BaseModel):
    account_name: Optional[str]
    account_type: Optional[str]
    currency: Optional[str]
    balance: Optional[float]
    status: Optional[str]

class LedgerOut(LedgerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
