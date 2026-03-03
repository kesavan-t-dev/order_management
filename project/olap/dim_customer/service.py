# from .models import *

# def create():
    
#     # cur.execute('select * from customer')
#     create = '''create table customer(
#                     id UNIQUEIDENTIFIER DEFAULT NEWID(),
#                     customer_id UNIQUEIDENTIFIER,
#                     name varchar(max),
#                     number varchar(10));
#             '''
#     cur.execute(create)
#     db.commit()
#     # print(cur)
#     # db.commit()

# def dim_create(cus_id, name, number):
#     cur.execute('insert into dbo.customer (customer_id, name, number) values (%s, %s, %s)', (cus_id, name, number))
#     db.commit()

# def dim_update(id, name, number):
#     cur.execute('update dbo.customer set name = %s, number = %s where customer_id = %s',(name, number, id))
#     db.commit()
