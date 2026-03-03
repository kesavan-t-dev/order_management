from os import error

from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Order, Order_items
from project.olap.dim_order.service import sync_to_ssms


def create_order(db, data):
    try:
        new_order = Order(
            customer_id=data.customer_id,
            order_status="Order placed"
        )
        db.add(new_order)
        db.flush() 
        new_item = Order_items(
            order_id=new_order.id, 
            product_id=data.product_id,
            quantity=int(data.quantity), 
            total=data.total
        )
        db.add(new_item)
        db.commit() 
        db.refresh(new_order) 
        sync_to_ssms(new_item, data.customer_id)
        
        return {
            "message": "Order created successfully",
            "status_code": 201,
            "data": {
                "customer_id": new_order.customer_id,
                "order_status": new_order.order_status,
                "product_id": new_item.product_id,
                "quantity": new_item.quantity,
                "total": new_item.total
            }
        }
    except Exception as e:
        db.rollback() 
        raise e
