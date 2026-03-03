import pandas as pd
import pymssql
import os
import pytz
from datetime import datetime, timedelta
from pytz import timezone
from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

load_dotenv()

def get_kolkata_time():
    local_tz = timezone('Asia/Kolkata')
    return datetime.now(local_tz)

def export_job():
    conn = None
    try:
        now_kolkata = datetime.now(timezone('Asia/Kolkata'))
        now_utc = datetime.now(pytz.utc)
        
        lookback_utc = now_utc - timedelta(minutes=3)
        
        file_ts = now_kolkata.strftime("%Y-%m-%d_%H-%M-%S")
        sql_ts = lookback_utc.strftime("%Y-%m-%d %H:%M:%S")

        print(f"Searching DB for records since {file_ts}")

        conn = pymssql.connect(
            server="host.docker.internal",
            port=1433,
            user="sa2026",
            password="2026",
            database="order_management",
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
        WHERE o.[date] >= %s
        """

        cursor.execute(query, (sql_ts,))
        rows = cursor.fetchall()

        if not rows:
            print(f"No records found in DB after{file_ts}")
            return

        columns = [col[0] for col in cursor.description]
        output_folder = Path('CSV_Exports')
        output_folder.mkdir(parents=True, exist_ok=True)
        
        output_filename = f'orders_{file_ts}_data.csv'
        output_path = output_folder / output_filename

        df = pd.DataFrame([list(r) for r in rows], columns=columns)
        df.to_csv(output_path, index=False, encoding='utf-8')
        
        print(f"Successfully saved {len(df)} records to {output_path}")

    except Exception as e:
        print(f"Scheduler Error: {e}")
    finally:
        if conn:
            conn.close()

scheduler = BlockingScheduler()
scheduler.add_job(export_job, 'cron', minute='*/3')

print(f"Scheduler started")
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass