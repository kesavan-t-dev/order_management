import pandas as pd
import pymssql
import os
import io
import pytz
from datetime import datetime
from pytz import timezone
from pathlib import Path
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()

def get_local_time():
    utc_time = datetime.now(pytz.utc)
    local_tz = timezone('Asia/Kolkata')  
    local_time = utc_time.astimezone(local_tz)
    return local_time.strftime("%Y-%m-%d_%H-%M-%S")
timestamp = get_local_time()

@router.get("/export_orders")
def export_orders_to_csv():
    conn = None
    try:
        TABLE_NAME = "orders"
        conn = pymssql.connect(
            server='host.docker.internal',
            port=1433,
            user='sa2026',
            password='2026',
            database='order_management',
            timeout=10  
        )
        cursor = conn.cursor()

        query = """
        SELECT 
            p.product_name,
            c.customer_name,
            o.quantity,
            o.price,
            o.[date]
        FROM orders o
        JOIN product p ON o.product_id = p.external_id
        JOIN customer c ON o.customer_id = c.external_id
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No orders found to export")

        columns = [col[0] for col in cursor.description]

        output_folder = 'CSV_Exports'
        output_filename = f'{TABLE_NAME}_{timestamp}_data.csv'
        output_path = Path(output_folder) / output_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(rows, columns=columns)
        df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Successfully exported joined data to {output_path}")
        return {"message": f"Orders exported successfully to {output_path}"}
    
    except pymssql.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot reach SSMS. Check TCP/IP and Firewall.")
    except Exception as e:
        print(f"Export Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if conn:
            conn.close()

                                                                                                                                                                           
