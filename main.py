# main.py
from fastapi import FastAPI
from project.customer.api import * 
from project.product.api import * 
from project.olap.dim_customer.api import *
from project.orders.api import router as order_router
from project.product.api import router as product_route
from project.olap.dim_order.export_csv import router as olap_router
from project.customer.models import Customer
from project.product.models import Product
from project.orders.models import Order, Order_items
# Create a FastAPI "instance"
# app = FastAPI()

app = FastAPI(debug=True)

app.include_router(customer_route)
app.include_router(router)
app.include_router(product_route)
# app.include_router(order_route)

app.include_router(order_router, prefix="/order", tags=["Order"])
app.include_router(olap_router, prefix="/olap", tags=["OLAP"])

@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}


