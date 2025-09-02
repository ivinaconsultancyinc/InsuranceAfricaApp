from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Commission(Base):
    __tablename__ = "commissions"

    id = Column(Integer, primary_key=True, index=True)
    agent = Column(String, index=True)
    policy = Column(String, index=True)
    amount = Column(Float)
    rate = Column(Float)
    payment_date = Column(Date)
    status = Column(String)