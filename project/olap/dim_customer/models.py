import pymssql

db = pymssql.connect(host='host.docker.internal', user='user2025', password='2025', database='order_management')
cur = db.cursor()