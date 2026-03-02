import os
import uuid
import pyodbc
from dotenv import load_dotenv
from project.orders.models import Order

load_dotenv()

SSMS_CONN_STR = os.getenv("SSMS_CONNECTION_STRING")

def sync_to_ssms(order_obj: Order):

    conn = None
    try:
        conn = pyodbc.connect(SSMS_CONN_STR)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO orders (id, customer_id, product_id, order_id, quantity, price, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        for item in order_obj.items:
            cursor.execute(insert_query, (
                str(uuid.uuid4()),            
                str(order_obj.customer_id),   
                str(item.product_id),         
                str(order_obj.id),            
                str(item.quantity),           
                str(item.total),              
                order_obj.order_date          
            ))

        conn.commit()
        print("Successfully synced to SSMS")
        
    except Exception as e:
        print(f"Failed to sync to SSMS: {str(e)}")
    finally:
        if conn:
            conn.close()

