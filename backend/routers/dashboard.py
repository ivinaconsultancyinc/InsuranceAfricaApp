from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.dashboard_service import get_dashboard_metrics
from database import get_db
from fastapi.security import OAuth2PasswordBearer
from auth.auth_handler import decode_access_token

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/metrics")
def dashboard_metrics(db: Session = Depends(get_db)):
    return get_dashboard_metrics(db)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.get("/metrics")
def dashboard_metrics(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return get_dashboard_metrics(db)


