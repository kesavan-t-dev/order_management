from .validation import *
from .models import Customer
from fastapi import  status, Response
import uuid
from app.customer_worker import insert_customer_to_sql,update_customer_to_sql
def customer_list(db):
    try:
        customers = db.query(Customer).filter_by(is_active = True).all()
        if len(customers) > 0:
            
            return {
                "message": "list of customers",
                "properties": customers,
                "status_code" : 200
            }
            
        return Response(content = 'No Customer exists', status_code = status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response(content= e, status_code = status.HTTP_400_BAD_REQUEST)
    
def new_customer(db, customer):
    try:
        number = customer.number
        zip_code = customer.zip

        if not number.isnumeric():
            return  Response(content="Special characters / Alphabets not allowed for mobile number", status_code=status.HTTP_400_BAD_REQUEST)
        
        if not zip_code.isnumeric():
            return  Response(content="Special characters / Alphabets not allowed for zipcode", status_code=status.HTTP_400_BAD_REQUEST)
        
        existing_customer = db.query(Customer).filter_by(email = customer.email, number = customer.number).first()
        if existing_customer:
            return Response(content="Customer already exists", status_code=status.HTTP_400_BAD_REQUEST)
        
        new_customer = Customer(
            name = customer.name,
            email = customer.email,
            number = customer.number,
            address = customer.address,
            city = customer.city,
            zip = customer.zip
        )
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        db.close()
       
        data = {
            'id': new_customer.id,
            'name': new_customer.name,
            'email': new_customer.email,
            'number': new_customer.number,
            'address': new_customer.address,
            'city': new_customer.city,
            'zip': new_customer.zip,
        }
        insert_customer_to_sql.delay(new_customer.id, new_customer.name, new_customer.number,new_customer.email)
        
        return {"message": "customer created successfully", "properties": data, "status_code" : 201}
    except Exception as e:
        return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

def update_customer(id: uuid, payload: dict, db):
    try:
        if not payload.name  and not payload.email  and not payload.number  and not payload.address  and not payload.city  and not payload.zip :
            return Response(content= 'Enter values to update', status_code = status.HTTP_400_BAD_REQUEST)
        
        customer = db.query(Customer).filter_by(id = id).first()
        if customer:
            update_data = payload.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                print(key, value)
                setattr(customer, key, value)
            db.commit()
            db.refresh(customer)

            update_customer_to_sql.delay(id, update_data)             
            return {
                "message": "customer updated successfully",
                "properties": update_data,
                "status_code" : 201
            }
        return Response(content= 'customer not found', status_code = status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print('ERROR OCCURED :',e)
        return Response(content= str(e), status_code=status.HTTP_400_BAD_REQUEST)

def remove_customer(id: uuid, db):
    try: 
        if not id:
            return Response(content='Provide ID to delete', status_code= status.HTTP_400_BAD_REQUEST)
        
        customer = db.query(Customer).filter_by(id = id, is_active= True).first()
        print(customer)
        if customer:
            name = customer.name
            customer.is_active = False
            print(customer.is_active)
            db.commit()
            db.close()
            return {
                'message' : 'customer deleted successfully',
                'properties' : {'customer_name' : name},
                'status_code': 200 
            }
        return Response(content='customer not found', status_code= status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(content= e, status_code = status.HTTP_400_BAD_REQUEST)