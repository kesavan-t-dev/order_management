from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from .service import create_order
from .validation import OrderCreate, OrderResponse
router = APIRouter()


@router.post("/create", response_model=OrderResponse)
def add_order(data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, data)