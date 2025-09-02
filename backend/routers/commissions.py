from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.commissions_schema import CommissionCreate, CommissionUpdate, CommissionOut
from services.commissions_service import (
    create_commission, get_commissions, get_commission,
    update_commission, delete_commission
)
from database import get_db

router = APIRouter(prefix="/commissions", tags=["commissions"])

@router.post("/", response_model=CommissionOut)
def create(commission: CommissionCreate, db: Session = Depends(get_db)):
    return create_commission(db, commission)

@router.get("/", response_model=list[CommissionOut])
def read_all(db: Session = Depends(get_db)):
    return get_commissions(db)

@router.get("/{commission_id}", response_model=CommissionOut)
def read_one(commission_id: int, db: Session = Depends(get_db)):
    commission = get_commission(db, commission_id)
    if not commission:
        raise HTTPException(status_code=404, detail="Commission not found")
    return commission

@router.put("/{commission_id}", response_model=CommissionOut)
def update(commission_id: int, commission: CommissionUpdate, db: Session = Depends(get_db)):
    updated = update_commission(db, commission_id, commission)
    if not updated:
        raise HTTPException(status_code=404, detail="Commission not found")
    return updated

@router.delete("/{commission_id}", response_model=CommissionOut)
def delete(commission_id: int, db: Session = Depends(get_db)):
    deleted = delete_commission(db, commission_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Commission not found")
    return deleted