 from pydantic import BaseModel
from datetime import date

class ClaimBase(BaseModel):
    policy_id: int
    claim_type: str
    claim_amount: float
    claim_date: date

class ClaimCreate(ClaimBase):
    pass

class ClaimUpdate(ClaimBase):
    status: str

class ClaimResponse(ClaimBase):
    id: int
    status: str

    class Config:
        orm_mode = True

class LoanBase(BaseModel):
    policy_id: int
    loan_amount: float
    loan_date: date

class LoanCreate(LoanBase):
    pass

class LoanUpdate(LoanBase):
    repayment_status: str

class LoanResponse(LoanBase):
    id: int
    repayment_status: str

    class Config:
        orm_mode = True
