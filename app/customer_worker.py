import pymssql
from app.celery_worker import celery_app
import pymssql
import uuid

@celery_app.task(name="customer_worker.insert_customer_to_sql")
def insert_customer_to_sql(id, name, number, email):
    try:
        conn = pymssql.connect(
            server = "host.docker.internal",
            user = "user2025",
            password = "2025",
            database = "order_management"
        )
        cursor = conn.cursor()
        new_id = str(uuid.uuid4())
        query = """
            insert into customer (id, customer_name, customer_number, email, external_id) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_id,  name, number,email,id))
        conn.commit()
    except Exception as e:
        print(f"[Customer Task] Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@celery_app.task(name = "customer_worker.update_customer_to_sql")
def update_customer_to_sql(id,update_data):
    try:
        fields = []
        values = []

        if "name" in update_data:
            name = update_data["name"]
            fields.append("customer_name = %s")
            values.append(name)

        if "number" in update_data:
            brand = update_data["number"]
            fields.append("customer_number = %s")
            values.append(brand)

        if "email" in update_data:
            category = update_data["email"]
            fields.append("email = %s")
            values.append(category)

        if fields:  
            values.append(str(id))
            sql_query = f"UPDATE customer SET {', '.join(fields)} WHERE external_id = %s"

            conn = pymssql.connect(
                server = "host.docker.internal",
                user = "user2025",
                password = "2025",
                database = "order_management"
            )
            cursor = conn.cursor()
            cursor.execute(sql_query, tuple(values))
            conn.commit()
            cursor.close()
            conn.close()

    except Exception as e:
        print(f"[Customer Task] Error: {e}")