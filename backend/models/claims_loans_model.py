from sqlalchemy import Column, Integer, String, Float, Date
from ..database import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, index=True)
    claim_type = Column(String)
    claim_amount = Column(Float)
    claim_date = Column(Date)
    status = Column(String, default="pending")

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, index=True)
    loan_amount = Column(Float)
    loan_date = Column(Date)
    repayment_status = Column(String, default="unpaid")

