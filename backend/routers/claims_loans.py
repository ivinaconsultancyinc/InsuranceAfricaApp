from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import claims_loans_schema
from ..services import claims_loans_service
from ..database import get_db

router = APIRouter(prefix="/claims-loans", tags=["Claims & Loans"])

# Claims
@router.post("/claims", response_model=claims_loans_schema.ClaimResponse)
def create_claim(claim: claims_loans_schema.ClaimCreate, db: Session = Depends(get_db)):
    return claims_loans_service.create_claim(db, claim)

@router.get("/claims", response_model=list[claims_loans_schema.ClaimResponse])
def read_claims(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return claims_loans_service.get_claims(db, skip, limit)

@router.get("/claims/{claim_id}", response_model=claims_loans_schema.ClaimResponse)
def read_claim(claim_id: int, db: Session = Depends(get_db)):
    db_claim = claims_loans_service.get_claim(db, claim_id)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim

@router.put("/claims/{claim_id}", response_model=claims_loans_schema.ClaimResponse)
def update_claim(claim_id: int, claim: claims_loans_schema.ClaimUpdate, db: Session = Depends(get_db)):
    return claims_loans_service.update_claim(db, claim_id, claim)

@router.delete("/claims/{claim_id}", response_model=claims_loans_schema.ClaimResponse)
def delete_claim(claim_id: int, db: Session = Depends(get_db)):
    return claims_loans_service.delete_claim(db, claim_id)

# Loans
@router.post("/loans", response_model=claims_loans_schema.LoanResponse)
def create_loan(loan: claims_loans_schema.LoanCreate, db: Session = Depends(get_db)):
    return claims_loans_service.create_loan(db, loan)

@router.get("/loans", response_model=list[claims_loans_schema.LoanResponse])
def read_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return claims_loans_service.get_loans(db, skip, limit)

@router.get("/loans/{loan_id}", response_model=claims_loans_schema.LoanResponse)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = claims_loans_service.get_loan(db, loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

@router.put("/loans/{loan_id}", response_model=claims_loans_schema.LoanResponse)
def update_loan(loan_id: int, loan: claims_loans_schema.LoanUpdate, db: Session = Depends(get_db)):
    return claims_loans_service.update_loan(db, loan_id, loan)

@router.delete("/loans/{loan_id}", response_model=claims_loans_schema.LoanResponse)
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    return claims_loans_service.delete_loan(db, loan_id)