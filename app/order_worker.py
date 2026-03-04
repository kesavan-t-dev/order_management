import pymssql
from app.celery_worker import celery_app
import pymssql
import uuid


@celery_app.task(name = "order_worker.insert_order_to_sql")
def insert_order_to_sql(customer_id, product_id, order_id, quantity, total):

    try:
        conn = pymssql.connect(
            server = "host.docker.internal\\SQLEXPRESS",
            user = "Mssql_db",
            password = "2025",
            database = "orders"
        )
        cursor = conn.cursor()
        new_id = str(uuid.uuid4())
        query = """
            insert into orders (id, customer_id, product_id, order_id, quantity, price, date)
            VALUES (%s, %s, %s, %s, %s, %s, GETDATE())
        """
        cursor.execute(query, (new_id, customer_id, product_id, order_id, quantity, total))
        conn.commit()
    except Exception as e:
        print(f"[Order Task] Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
