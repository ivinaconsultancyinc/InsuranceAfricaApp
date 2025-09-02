from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AuditLogBase(BaseModel):
    entity_type: str
    entity_id: str
    action: str
    performed_by: str
    timestamp: Optional[datetime] = None
    details: Optional[str]

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogOut(AuditLogBase):
    id: int
    model_config = {"from_attributes": True}

class UserAccessBase(BaseModel):
    username: str
    role: str
    permissions: str
    last_login: Optional[datetime]

class UserAccessCreate(UserAccessBase):
    pass

class UserAccessOut(UserAccessBase):
    id: int
    model_config = {"from_attributes": True}

