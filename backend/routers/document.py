from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.document_schema import DocumentCreate, DocumentUpdate, DocumentOut
from services import document_service

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentOut)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    return document_service.create_document(db, document)

@router.get("/{document_id}", response_model=DocumentOut)
def read_document(document_id: int, db: Session = Depends(get_db)):
    db_document = document_service.get_document(db, document_id)
    if not db_document:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

@router.get("/", response_model=list[DocumentOut])
def read_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return document_service.get_documents(db, skip, limit)

@router.put("/{document_id}", response_model=DocumentOut)
def update_document(document_id: int, document: DocumentUpdate, db: Session = Depends(get_db)):
    return document_service.update_document(db, document_id, document)

@router.delete("/{document_id}", response_model=DocumentOut)
def delete_document(document_id: int, db: Session = Depends(get_db)):
    return document_service.delete_document(db, document_id)







