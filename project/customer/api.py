from fastapi import APIRouter, HTTPException, Form, File, UploadFile, Depends
from sqlalchemy.orm import Session
from .service import *
from .validation import *
from db import get_db


customer_route = APIRouter(
    prefix= '/user',
    tags= ['user'],
    responses={404: {"description": "Not found"}}
)


@customer_route.get('/user_list', response_model= None)
def get_customer(db: Session = Depends(get_db)):
    return customer_list(db)