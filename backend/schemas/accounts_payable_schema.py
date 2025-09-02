from pydantic import BaseModel
from typing import Optional
from datetime import date

class VendorBase(BaseModel):
    name: str
    contact_info: Optional[str]
    bank_details: Optional[str]
    tax_id: Optional[str]
    currency: Optional[str]
    category: Optional[str]

class VendorCreate(VendorBase):
    pass

class VendorOut(VendorBase):
    id: int
    model_config = {"from_attributes": True}

class InvoiceBase(BaseModel):
    vendor_id: int
    invoice_number: str
    invoice_date: date
    due_date: date
    amount: float
    currency: str
    status: str
    attachment_url: Optional[str]
    created_by: Optional[str]
    approved_by: Optional[str]

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceOut(InvoiceBase):
    id: int
    model_config = {"from_attributes": True}

class PaymentBase(BaseModel):
    invoice_id: int
    payment_date: date
    amount_paid: float
    payment_method: str
    bank_transaction_id: Optional[str]
    status: str

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int
    model_config = {"from_attributes": True}
