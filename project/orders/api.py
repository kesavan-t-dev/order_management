from fastapi import APIRouter, Depends
from db import get_db
from service import create_order
from validation import CreateOrder
router = APIRouter()


@router.post("/create")
def add_order(data: CreateOrder,db: Session = Depends(get_db)):
    return create_order(db, data)