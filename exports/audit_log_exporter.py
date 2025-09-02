import pandas as pd
from sqlalchemy.orm import Session
from models.audit_access_model import AuditLog

def export_denied_logs_to_csv(db: Session, path: str = "denied_access_logs.csv"):
    logs = db.query(AuditLog).filter(AuditLog.action.like("DENIED:%")).all()
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
    df.to_csv(path, index=False)

def export_denied_logs_to_excel(db: Session, path: str = "denied_access_logs.xlsx"):
    logs = db.query(AuditLog).filter(AuditLog.action.like("DENIED:%")).all()
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
    df.to_excel(path, index=False, engine="openpyxl")
