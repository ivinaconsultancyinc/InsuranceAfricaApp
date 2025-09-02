from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # assuming you have a shared Base from your DB setup

class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_info = Column(String)
    bank_details = Column(String)
    tax_id = Column(String)
    currency = Column(String)
    category = Column(String)

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    invoice_number = Column(String)
    invoice_date = Column(Date)
    due_date = Column(Date)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String)
    attachment_url = Column(String)
    created_by = Column(String)
    approved_by = Column(String)

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    payment_date = Column(Date)
    amount_paid = Column(Float)
    payment_method = Column(String)
    bank_transaction_id = Column(String)
    status = Column(String)
