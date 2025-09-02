# Placeholder for auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from auth.auth_utils import verify_password, create_access_token
from database import get_db
from models.audit_access_model import UserAccess

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(login_data: LoginData, db: Session = Depends(get_db)):
    user = db.query(UserAccess).filter(UserAccess.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.permissions)auth_router:  # assuming 'permissions' stores hashed password
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}






