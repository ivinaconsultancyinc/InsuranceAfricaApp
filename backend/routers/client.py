from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import client_schema
from ..services import client_service
from ..database import get_db

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=client_schema.ClientResponse)
def create_client(client: client_schema.ClientCreate, db: Session = Depends(get_db)):
    return client_service.create_client(db, client)

@router.get("/", response_model=list[client_schema.ClientResponse])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return client_service.get_clients(db, skip, limit)

@router.get("/{client_id}", response_model=client_schema.ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = client_service.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.put("/{client_id}", response_model=client_schema.ClientResponse)
def update_client(client_id: int, client: client_schema.ClientUpdate, db: Session = Depends(get_db)):
    return client_service.update_client(db, client_id, client)

@router.delete("/{client_id}", response_model=client_schema.ClientResponse)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return client_service.delete_client(db, client_id)