from sqlalchemy import Column, Integer, String, Float, Date
from ..database import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String, unique=True, index=True)
    client_id = Column(Integer, index=True)
    product_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    premium_amount = Column(Float)
    status = Column(String, default="active")