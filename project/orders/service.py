from .models import Order, Order_items
from app.order_worker import insert_order_to_sql
from fastapi import status

def create_order(db, data):
    try:
        new_order = Order(
            customer_id = data.customer_id,
            order_status = "Order placed"
        )
        db.add(new_order)
        db.flush() 
        new_item = Order_items(
            order_id = new_order.id, 
            product_id = data.product_id,
            quantity = int(data.quantity), 
            total = int(data.total)
        )
        db.add(new_item)
        db.commit() 
        db.refresh(new_order) 
     
        insert_order_to_sql.delay(
            customer_id = data.customer_id,
            product_id = data.product_id,
            order_id = new_order.id,
            quantity = data.quantity,
            total = data.total
        )
        return {
            "message": "Order created successfully",
            "status_code": status.HTTP_201_CREATED,
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
