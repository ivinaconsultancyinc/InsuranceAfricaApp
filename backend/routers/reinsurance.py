from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import reinsurance_schema
from ..services import reinsurance_service
from ..database import get_db

router = APIRouter(prefix="/reinsurance", tags=["Reinsurance"])

@router.post("/", response_model=reinsurance_schema.ReinsuranceResponse)
def create_treaty(treaty: reinsurance_schema.ReinsuranceCreate, db: Session = Depends(get_db)):
    return reinsurance_service.create_treaty(db, treaty)

@router.get("/", response_model=list[reinsurance_schema.ReinsuranceResponse])
def read_treaties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return reinsurance_service.get_treaties(db, skip, limit)

@router.get("/{treaty_id}", response_model=reinsurance_schema.ReinsuranceResponse)
def read_treaty(treaty_id: int, db: Session = Depends(get_db)):
    db_treaty = reinsurance_service.get_treaty(db, treaty_id)
    if db_treaty is None:
        raise HTTPException(status_code=404, detail="Treaty not found")
    return db_treaty

@router.put("/{treaty_id}", response_model=reinsurance_schema.ReinsuranceResponse)
def update_treaty(treaty_id: int, treaty: reinsurance_schema.ReinsuranceUpdate, db: Session = Depends(get_db)):
    return reinsurance_service.update_treaty(db, treaty_id, treaty)

@router.delete("/{treaty_id}", response_model=reinsurance_schema.ReinsuranceResponse)
def delete_treaty(treaty_id: int, db: Session = Depends(get_db)):
    return reinsurance_service.delete_treaty(db, treaty_id)