from pydantic import BaseModel, EmailStr

class ClientBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    address: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    status: str

class ClientResponse(ClientBase):
    id: int
    status: str

    class Config:
        orm_mode = True