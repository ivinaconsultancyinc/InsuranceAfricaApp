from pydantic import BaseModel
from datetime import date

class GLAccountBase(BaseModel):
    name: str
    type: str
    currency: str

class GLAccountCreate(GLAccountBase):
    pass

class GLAccountOut(GLAccountBase):
    id: int

    class Config:
        orm_mode = True

class GLTransactionBase(BaseModel):
    account_id: int
    amount: float
    currency: str
    debit_credit: str
    description: str
    reference: str
    transaction_date: date
    created_by: str
    created_at: date

class GLTransactionCreate(GLTransactionBase):
    pass

class GLTransactionOut(GLTransactionBase):
    id: int

    class Config:
        orm_mode = True

