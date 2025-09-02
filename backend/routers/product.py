from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import product_schema
from ..services import product_service
from ..database import get_db
router = APIRouter(prefix="/products", tags=["Products"])
@router.post("/", response_model=product_schema.ProductResponse)
def create_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)
@router.get("/", response_model=list[product_schema.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return product_service.get_products(db, skip, limit)
@router.get("/{product_id}", response_model=product_schema.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
@router.put("/{product_id}", response_model=product_schema.ProductResponse)
def update_product(product_id: int, product: product_schema.ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, product)
@router.delete("/{product_id}", response_model=product_schema.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)
