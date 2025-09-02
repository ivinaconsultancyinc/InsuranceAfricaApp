from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.ledger_schema import LedgerCreate, LedgerUpdate, LedgerOut
from services import ledger_service
router = APIRouter(prefix="/ledgers", tags=["Ledgers"])
@router.post("/", response_model=LedgerOut)
def create_ledger(ledger: LedgerCreate, db: Session = Depends(get_db)):
    return ledger_service.create_ledger(db, ledger)
@router.get("/{ledger_id}", response_model=LedgerOut)
def read_ledger(ledger_id: int, db: Session = Depends(get_db)):
    db_ledger = ledger_service.get_ledger(db, ledger_id)
    if not db_ledger:
        raise HTTPException(status_code=404, detail="Ledger not found")
    return db_ledger
@router.get("/", response_model=list[LedgerOut])
def read_ledgers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ledger_service.get_ledgers(db, skip, limit)
@router.put("/{ledger_id}", response_model=LedgerOut)
def update_ledger(ledger_id: int, ledger: LedgerUpdate, db: Session = Depends(get_db)):
    return ledger_service.update_ledger(db, ledger_id, ledger)
@router.delete("/{ledger_id}", response_model=LedgerOut)
def delete_ledger(ledger_id: int, db: Session = Depends(get_db)):
    return ledger_service.delete_ledger(db, ledger_id)






