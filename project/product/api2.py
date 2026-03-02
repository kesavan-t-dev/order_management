
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db 
from service2 import ProductResponse, ProductRead
from service import ProductService
from uuid import UUID

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=ProductResponse)
def get_products(db: Session = Depends(get_db)):
    products = ProductService.get_all_products(db)
    return {
        "message": "Products retrieved successfully",
        "data": products,
        "status_code": 200
    }

@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product(product_id: UUID, db: Session = Depends(get_db)):
    success = ProductService.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
        
    return {
        "message": "Product deleted successfully",
        "data": [],
        "status_code": 200
    }