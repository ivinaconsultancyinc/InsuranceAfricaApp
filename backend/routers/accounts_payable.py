from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db  # assuming you have a get_db dependency
from schemas.accounts_payable_schema import (
    VendorCreate, VendorOut,
    InvoiceCreate, InvoiceOut,
    PaymentCreate, PaymentOut
)
from services.accounts_payable_service import (
    create_vendor, get_vendors,
    create_invoice, get_invoices,
    create_payment, get_payments
)
from typing import List

router = APIRouter()

@router.post("/vendors", response_model=VendorOut)
def add_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    return create_vendor(db, vendor)

@router.get("/vendors", response_model=List[VendorOut])
def list_vendors(db: Session = Depends(get_db)):
    return get_vendors(db)

@router.post("/invoices", response_model=InvoiceOut)
def add_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db, invoice)

@router.get("/invoices", response_model=List[InvoiceOut])
def list_invoices(db: Session = Depends(get_db)):
    return get_invoices(db)

@router.post("/payments", response_model=PaymentOut)
def add_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db, payment)

@router.get("/payments", response_model=List[PaymentOut])
def list_payments(db: Session = Depends(get_db)):
    return get_payments(db)

