import pymssql
import os
import uuid
from dotenv import load_dotenv
from project.orders.models import Order

load_dotenv()

def sync_to_ssms(new_item, customer_id):
    conn = None
    try:
        conn = pymssql.connect(
            server='host.docker.internal', 
            port=1433,
            user='sa2026',
            password='2026',   
            database='order_management',
            timeout=5
        )
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO orders (id, customer_id, product_id, order_id, quantity, price, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        customer = str(customer_id)
        
        row = (
            str(uuid.uuid4()),            
            customer, 
            str(new_item.product_id),     
            str(new_item.order_id),      
            str(new_item.quantity),       
            str(new_item.total)          
        )
        cursor.execute(insert_query, row)
        conn.commit()
        print("Successfully synced to SSMS manually!")
    except Exception as e:
        print(f"SSMS Error: {e}")
    finally:
        if conn:
            conn.close()

