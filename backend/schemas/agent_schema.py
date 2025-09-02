from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class AgentBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = "Active"
class AgentCreate(AgentBase):
    pass
class AgentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    status: Optional[str]
class AgentOut(AgentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    class Config:
        orm_mode = True