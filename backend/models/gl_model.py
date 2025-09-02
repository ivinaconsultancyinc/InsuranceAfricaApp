from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class GLAccount(Base):
    __tablename__ = "gl_accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)  # e.g., Asset, Liability, Equity, Revenue, Expense
    currency = Column(String)  # e.g., USD, EUR, GHS
class GLTransaction(Base):
    __tablename__ = "gl_transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("gl_accounts.id"))
    amount = Column(Float)
    currency = Column(String)
    debit_credit = Column(String)  # 'debit' or 'credit'
    description = Column(String)
    reference = Column(String)
    transaction_date = Column(Date)
    created_by = Column(String)
    created_at = Column(Date)
    account = relationship("GLAccount")

