from fastapi import APIRouter, HTTPException, Form, File, UploadFile
from .service import *
from .validation import *



# customer_route = APIRouter(
#     prefix= '/user',
#     tags= ['user'],
#     responses={404: {"description": "Not found"}}
# )


# @customer_route.get('/user_list', response_model= None)
# def get_customer(db: Session = Depends(get_db)):
#     return customer_list(db, )