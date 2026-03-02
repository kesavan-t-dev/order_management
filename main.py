# main.py
from fastapi import FastAPI
from project.customer.api import * 
from project.orders.api import router as order_router
from project.customer.models import Customer
from project.product.models import Product
from project.orders.models import Order, Order_items

app = FastAPI(debug=True)

app.include_router(order_router, prefix="/order", tags=["Order"])

@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}