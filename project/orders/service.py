from sqlalchemy.orm import Session
from models import Order, Order_items
import uuid

def create_full_order(db: Session, order_data: OrderCreateRequest):
    
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
            quantity=item.quantity,
            total=item.total
        )
        db.add(new_item)

    db.commit() 
    db.refresh(new_order)
    return new_order
