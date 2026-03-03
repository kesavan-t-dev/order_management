import pandas as pd

from pathlib import Path

from datetime import datetime

import pymssql



# Table name and timestamp

TABLE_NAME = "orders"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")



# Database connection

conn = pymssql.connect(

    server='localhost\\SQLEXPRESS',

    user='Mssql_db',

    password='2025',

    database='orders'

)

conn_str = conn.cursor()



# SQL query with JOINs to get parent values

query = """

SELECT

    o.id AS order_id,

    c.customer_name,

    c.customer_number,

    c.email,

    p.product_name,

    t.type_name,

    o.quantity,

    o.price,

    o.date

FROM orders o

JOIN customer c ON o.customer_id = c.id

JOIN product p ON o.product_id = p.id



"""



# Fetch data

conn_str.execute(query)

rows = conn_str.fetchall()



# Get column names

columns = [col[0] for col in conn_str.description]



# Output file path

output_folder = 'CSV_Exports'

output_filename = f'{TABLE_NAME}_{timestamp}_data.csv'

output_path = Path(output_folder) / output_filename



# Ensure directory exists

output_path.parent.mkdir(parents=True, exist_ok=True)



# Export to CSV

df = pd.DataFrame(rows, columns=columns)

df.to_csv(output_path, index=False, encoding='utf-8')



print(f"Successfully exported joined data to {output_path}")



# Close connections

conn_str.close()

conn.close()





 