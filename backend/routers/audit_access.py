from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.audit_access_schema import AuditLogCreate, AuditLogOut, UserAccessCreate, UserAccessOut
from services.audit_access_service import create_audit_log, get_audit_logs, create_user_access, get_user_access
from dependencies.access_control import get_denied_access_logs_filtered
from typing import List
from fastapi import Query
from datetime import datetime
from fastapi.responses import FileResponse
import pandas as pd

router = APIRouter()

@router.post("/audit-logs", response_model=AuditLogOut)
def add_audit_log(log: AuditLogCreate, db: Session = Depends(get_db)):
    return create_audit_log(db, log)

@router.get("/audit-logs", response_model=List[AuditLogOut])
def list_audit_logs(db: Session = Depends(get_db)):
    return get_audit_logs(db)

@router.post("/user-access", response_model=UserAccessOut)
def add_user_access(access: UserAccessCreate, db: Session = Depends(get_db)):
    return create_user_access(db, access)

@router.get("/user-access", response_model=List[UserAccessOut])
def list_user_access(db: Session = Depends(get_db)):
    return get_user_access(db)

@router.get("/audit-logs/denied", response_model=List[AuditLogOut])
def list_denied_logs(
    username: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    return get_denied_access_logs_filtered(db, username, start_date, end_date)


@router.get("/audit-logs/denied/export/csv")
def export_denied_logs_csv(
    username: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    logs = get_denied_access_logs_filtered(db, username, start_date, end_date)
    data = [{
        "ID": log.id,
        "Entity Type": log.entity_type,
        "Entity ID": log.entity_id,
        "Action": log.action,
        "Performed By": log.performed_by,
        "Timestamp": log.timestamp,
        "Details": log.details
    } for log in logs]
    df = pd.DataFrame(data)
    file_path = "filtered_denied_access_logs.csv"
    df.to_csv(file_path, index=False)
    return FileResponse(file_path, media_type="text/csv", filename=file_path)

@router.get("/audit-logs/denied/export/excel")
def export_denied_logs_excel(
    username: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    logs = get_denied_access_logs_filtered(db, username, start_date, end_date)
    data = [{
        "ID": log.id,
        "Entity Type": log.entity_type,
        "Entity ID": log.entity_id,
        "Action": log.action,
        "Performed By": log.performed_by,
        "Timestamp": log.timestamp,
        "Details": log.details
    } for log in logs]
    df = pd.DataFrame(data)
    file_path = "filtered_denied_access_logs.xlsx"
    df.to_excel(file_path, index=False, engine="openpyxl")
    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=file_path)