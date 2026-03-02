from .models import *

def export():
    name = 'hello'
    print(name)
    # cur.execute('select * from customer')
    create = '''CREATE TABLE dim_Customer(
        id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
        CustomerID INT UNIQUEIDENTIFIER,
        Name VARCHAR(50) NOT NULL
    );'''
    cur.execute(create)
    db.commit()
    print(cur)
    db.commit()
    print("Connection successful!")

def dim_create(cus_id, name, number):
    cur.execute('insert into dbo.customer (customer_id, name, number) values (%s, %s, %s)', (cus_id, name, number))
    db.commit()

def dim_update(id, name, number):
    cur.execute('update dbo.customer set name = %s, number = %s where customer_id = %s',(name, number, id))
    db.commit()


