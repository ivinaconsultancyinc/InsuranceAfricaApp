from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None
    file_path: str
    uploaded_by: str
    upload_date: datetime
    status: Optional[str] = "Active"

class DocumentCreate(DocumentBase):
    pass

class DocumentUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    file_path: Optional[str]
    uploaded_by: Optional[str]
    upload_date: Optional[datetime]
    status: Optional[str]

class DocumentOut(DocumentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
