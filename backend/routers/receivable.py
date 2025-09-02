from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.receivable_schema import ReceivableCreate, ReceivableUpdate, ReceivableOut
from services import receivable_service

router = APIRouter(prefix="/receivables", tags=["Receivables"])

@router.post("/", response_model=ReceivableOut)
def create_receivable(receivable: ReceivableCreate, db: Session = Depends(get_db)):
    return receivable_service.create_receivable(db, receivable)

@router.get("/{receivable_id}", response_model=ReceivableOut)
def read_receivable(receivable_id: int, db: Session = Depends(get_db)):
    db_receivable = receivable_service.get_receivable(db, receivable_id)
    if not db_receivable:
        raise HTTPException(status_code=404, detail="Receivable not found")
    return db_receivable

@router.get("/", response_model=list[ReceivableOut])
def read_receivables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return receivable_service.get_receivables(db, skip, limit)

@router.put("/{receivable_id}", response_model=ReceivableOut)
def update_receivable(receivable_id: int, receivable: ReceivableUpdate, db: Session = Depends(get_db)):
    return receivable_service.update_receivable(db, receivable_id, receivable)

@router.delete("/{receivable_id}", response_model=ReceivableOut)
def delete_receivable(receivable_id: int, db: Session = Depends(get_db)):
    return receivable_service.delete_receivable(db, receivable_id)




