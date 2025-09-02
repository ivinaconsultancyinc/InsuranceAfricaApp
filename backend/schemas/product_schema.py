from pydantic import BaseModel
class ProductBase(BaseModel):
    name: str
    description: str
    category: str
    premium_rate: float
    currency: str
class ProductCreate(ProductBase):
    pass
class ProductUpdate(ProductBase):
    pass
class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True








