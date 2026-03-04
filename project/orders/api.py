from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from .service import create_order
from .validation import OrderResponse,OrderData
router = APIRouter()


@router.post("/create", response_model=OrderResponse)
def add_order(data: OrderData, db: Session = Depends(get_db)):
    return create_order(db, data)

