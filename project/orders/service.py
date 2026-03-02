from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Order, Order_items
from .validation import OrderCreate
from project.olap.dim_order.service import sync_to_ssms


def create_order(db: Session, order_data: OrderCreate):
    try:
        

        new_order = Order(
            customer_id=order_data.customer_id,
            order_status="Order placed"
        )
        db.add(new_order)
        db.flush() 
        
        for item in order_data.items:
            new_item = Order_items(
                order_id=new_order.id, 
                product_id=item.product_id,
                quantity=int(item.quantity), 
                total=item.total
            )
            db.add(new_item)

        db.commit() 
        db.refresh(new_order) 
        sync_to_ssms(new_order)
        return {
            "message": "Order created successfully",
            "status_code": 201,
            "data": new_order  
        }
    except Exception as e:
        db.rollback() 
        raise e
    
