import pandas as pd
import pymssql
from datetime import datetime, timedelta
from pytz import timezone
from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

load_dotenv()

def export_job():
    conn = None
    try:
        now = datetime.now(timezone('Asia/Kolkata'))
        lookback = now - timedelta(minutes=3) 
        
        file_ts = now.strftime("%Y-%m-%d_%H-%M-%S")
        sql_ts = lookback.strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{file_ts}] Exporting records from {sql_ts} to {now.strftime('%H:%M:%S')}")
        file_ts = now.strftime("%Y-%m-%d_%H-%M-%S")
        sql_ts = lookback.strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{file_ts}] Exporting records from {sql_ts} to {now.strftime('%H:%M:%S')}")

        conn = pymssql.connect(
            server="host.docker.internal\\SQLEXPRESS",
            user="Mssql_db",
            password="2025",
            database="orders"
        )
        cursor = conn.cursor()

        query = """
        SELECT 
            o.order_id,
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
            print(f"No new records found since {sql_ts}.")

            return

        columns = [col[0] for col in cursor.description]
        output_folder = Path('CSV_Exports')
        output_folder.mkdir(parents=True, exist_ok=True)
        
        output_filename = f'orders_{file_ts}_data.csv'
        output_path = output_folder / output_filename

        df = pd.DataFrame([list(r) for r in rows], columns = columns)
        df.to_csv(output_path, index = False, encoding = 'utf-8')
        
        print(f"Successfully saved {len(df)} records to {output_path}")

    except Exception as e:
        print(f"Scheduler Error: {e}")
    finally:
        if conn:
            conn.close()

scheduler = BlockingScheduler()
scheduler.add_job(export_job, 'cron', minute='*/3')
print("Scheduler started. Running every 3 minutes...")

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass