from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from database import Base  # Assuming you have a Base from your database setup
class Ledger(Base):
    __tablename__ = "ledgers"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(String, unique=True, index=True, nullable=False)
    account_name = Column(String, nullable=False)
    account_type = Column(Enum("Asset", "Liability", "Equity", "Revenue", "Expense", name="account_type_enum"), nullable=False)
    currency = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    status = Column(Enum("Active", "Inactive", name="status_enum"), default="Active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
