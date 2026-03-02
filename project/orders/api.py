from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db 
from schemas import OrderCreate, OrderResponse
from service import create_full_order

app = FastAPI()

@app.post("orders/", response_model=OrderResponse)
def place_order(request: OrderCreateRequest, db: Session = Depends(get_db)):
    try:
        result = create_full_order(db, request)

        
        return {
            "message": "Order created successfully",
            "order_id": result.id,
            "status_code": 201
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
