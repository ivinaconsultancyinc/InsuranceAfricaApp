from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.statistical_reporting_schema import ReportCreate, ReportOut
from services.statistical_reporting_service import create_report, get_reports
from typing import List

router = APIRouter()

@router.post("/reports", response_model=ReportOut)
def add_report(report: ReportCreate, db: Session = Depends(get_db)):
    return create_report(db, report)

@router.get("/reports", response_model=List[ReportOut])
def list_reports(db: Session = Depends(get_db)):
    return get_reports(db)

