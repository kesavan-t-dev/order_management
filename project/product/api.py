from fastapi import APIRouter,  Depends,Body
from sqlalchemy.orm import Session
from db import get_db
from .service import create_products,read_products,update_products,delete_products
from .validation import Product_serializer,Product_response,Product_update_serializer
import uuid

router = APIRouter(prefix="/product")


@router.get("/list",response_model=Product_response)
def read_product(db: Session = Depends(get_db)):
    return read_products(db)

@router.post("/create")
def create_product(post: Product_serializer, db: Session = Depends(get_db)):
    return create_products(post, db)

@router.patch("/update/{item_id}", response_model=Product_response)
def update_product(
    item_id: uuid.UUID,
    update: Product_update_serializer = Body(...),
    db: Session = Depends(get_db)
):
    return update_products(item_id, update,db)

@router.delete("/delete/{item_id}")
def delete_product(
    item_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    return delete_products(item_id, db)