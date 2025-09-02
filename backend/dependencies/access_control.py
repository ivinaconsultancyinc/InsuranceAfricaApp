from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import datetime
from models.audit_access_model import UserAccess, AuditLog
from utils.permissions import ROLE_PERMISSIONS
from database import get_db

# Get current user from database
def get_current_user(username: str, db: Session = Depends(get_db)):
    user = db.query(UserAccess).filter(UserAccess.username == username).first()
    if not user:
        raise HTTPException(status_code=403, detail="User not found or unauthorized")
    return user

# Permission checker with logging for denied access
def require_permission(action: str):
    def permission_checker(
        request: Request,
        db: Session = Depends(get_db),
        user: UserAccess = Depends(get_current_user)
    ):
        allowed = ROLE_PERMISSIONS.get(user.role, [])
        if action not in allowed:
            log = AuditLog(
                entity_type="AccessControl",
                entity_id=user.username,
                action=f"DENIED:{action}",
                performed_by=user.username,
                timestamp=datetime.utcnow(),
                details=f"User with role '{user.role}' attempted unauthorized '{action}'"
            )
            db.add(log)
            db.commit()
            raise HTTPException(status_code=403, detail="Permission denied")
        return user
    return permission_checker

# Filter denied access logs by username and date range
def get_denied_access_logs_filtered(
    db: Session,
    username: str = None,
    start_date: datetime = None,
    end_date: datetime = None
):
    query = db.query(AuditLog).filter(AuditLog.action.like("DENIED:%"))
    if username:
        query = query.filter(AuditLog.performed_by == username)
    if start_date:
        query = query.filter(AuditLog.timestamp >= start_date)
    if end_date:
        query = query.filter(AuditLog.timestamp <= end_date)
    return query.all()
