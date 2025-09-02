from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import policy_schema
from ..services import policy_service
from ..database import get_db

router = APIRouter(prefix="/policies", tags=["Policies"])

@router.post("/", response_model=policy_schema.PolicyResponse)
def create_policy(policy: policy_schema.PolicyCreate, db: Session = Depends(get_db)):
    return policy_service.create_policy(db, policy)

@router.get("/", response_model=list[policy_schema.PolicyResponse])
def read_policies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return policy_service.get_policies(db, skip, limit)

@router.get("/{policy_id}", response_model=policy_schema.PolicyResponse)
def read_policy(policy_id: int, db: Session = Depends(get_db)):
    db_policy = policy_service.get_policy(db, policy_id)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy

@router.put("/{policy_id}", response_model=policy_schema.PolicyResponse)
def update_policy(policy_id: int, policy: policy_schema.PolicyUpdate, db: Session = Depends(get_db)):
    return policy_service.update_policy(db, policy_id, policy)

@router.delete("/{policy_id}", response_model=policy_schema.PolicyResponse)
def delete_policy(policy_id: int, db: Session = Depends(get_db)):
    return policy_service.delete_policy(db, policy_id)