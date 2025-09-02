from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.premium_schema import PremiumCreate, PremiumUpdate, PremiumOut
from services import premium_service

router = APIRouter(prefix="/premiums", tags=["Premiums"])

@router.post("/", response_model=PremiumOut)
def create_premium(premium: PremiumCreate, db: Session = Depends(get_db)):
    return premium_service.create_premium(db, premium)

@router.get("/{premium_id}", response_model=PremiumOut)
def read_premium(premium_id: int, db: Session = Depends(get_db)):
    db_premium = premium_service.get_premium(db, premium_id)
    if not db_premium:
        raise HTTPException(status_code=404, detail="Premium not found")
    return db_premium

@router.get("/", response_model=list[PremiumOut])
def read_premiums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return premium_service.get_premiums(db, skip, limit)

@router.put("/{premium_id}", response_model=PremiumOut)
def update_premium(premium_id: int, premium: PremiumUpdate, db: Session = Depends(get_db)):
    return premium_service.update_premium(db, premium_id, premium)

@router.delete("/{premium_id}", response_model=PremiumOut)
def delete_premium(premium_id: int, db: Session = Depends(get_db)):
    return premium_service.delete_premium(db, premium_id)



