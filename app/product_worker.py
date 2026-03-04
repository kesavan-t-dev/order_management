import pymssql
from app.celery_worker import celery_app
import pymssql
import uuid

@celery_app.task(name="product_worker.insert_product_to_sql")
def insert_product_to_sql(name, brand, category, id):
    print("hi")
    try:
        conn = pymssql.connect(
            server='host.docker.internal', 
            port=1433,
            user='sa2026',
            password='2026',   
            database='order_management'
        )
        cursor = conn.cursor()
        new_id = str(uuid.uuid4())
        query = """
            insert into product (id,product_name, product_brand,product_category,external_id) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_id, name, brand, category, id))
        conn.commit()
    except Exception as e:
        print(f"[Product Task] Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@celery_app.task(name="product_worker.update_order_to_sql")
def update_product_to_sql(update_data,item_id):
    try:
        fields = []
        values = []

        if "name" in update_data:
            name = update_data["name"]
            fields.append("product_name=%s")
            values.append(name)

        if "brand" in update_data:
            brand = update_data["brand"]
            fields.append("product_brand=%s")
            values.append(brand)

        if "category" in update_data:
            category = update_data["category"]
            fields.append("product_category=%s")
            values.append(category)

        if fields:  
            values.append(str(item_id))
            sql_query = f"UPDATE product SET {', '.join(fields)} WHERE external_id=%s"

            conn = pymssql.connect(
            server='host.docker.internal', 
            port=1433,
            user='sa2026',
            password='2026',   
            database='order_management'
            )
            cursor = conn.cursor()
            cursor.execute(sql_query, tuple(values))
            conn.commit()
            cursor.close()
            conn.close()

    except Exception as e:
        print(f"[Product Task] Error: {e}")
