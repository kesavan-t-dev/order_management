from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .service import customer_list, new_customer, update_customer, remove_customer
from .validation import Customer_response, Create_Customer, Customer_update_serializer
from db import get_db

customer_route = APIRouter(
    prefix= '/customer',
    tags= ['customer'],
    responses={404: {"description": "Not found"}}
)

@customer_route.get('/customer_list', response_model= Customer_response)
def get_customer(db: Session = Depends(get_db)):
    return customer_list(db)

@customer_route.post('/new_customer')
def add_customer(customer: Create_Customer, db : Session = Depends(get_db)):
    return new_customer(db, customer)

@customer_route.patch('/update_customer/{id}/')
def change_customer(id, data: Customer_update_serializer, db: Session = Depends(get_db)):
    return update_customer(id, data, db)

@customer_route.delete('/delete_customer/{id}/')
def delete_customer(id, db: Session = Depends(get_db)):
    return remove_customer(id, db)