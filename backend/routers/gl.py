from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.gl_schema import GLAccountCreate, GLAccountOut, GLTransactionCreate, GLTransactionOut
from services.gl_service import create_account, get_accounts, create_transaction, get_transactions
from database import get_db

router = APIRouter(prefix="/gl", tags=["general_ledger"])

@router.post("/accounts", response_model=GLAccountOut)
def create_gl_account(account: GLAccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)

@router.get("/accounts", response_model=list[GLAccountOut])
def read_gl_accounts(db: Session = Depends(get_db)):
    return get_accounts(db)

@router.post("/transactions", response_model=GLTransactionOut)
def create_gl_transaction(transaction: GLTransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, transaction)

@router.get("/transactions", response_model=list[GLTransactionOut])
def read_gl_transactions(db: Session = Depends(get_db)):
    return get_transactions(db)



