# main.py
from fastapi import FastAPI
from project.customer.api import * 
from project.product.api import * 
from project.olap.dim_customer.api import *
# Create a FastAPI "instance"
# app = FastAPI()
from project.product.api import router as product_route

app = FastAPI(debug=True)

app.include_router(customer_route)
app.include_router(router)
# app.include_router(product_route)
# app.include_router(order_route)
from project.orders.api import router as order_router


app = FastAPI()

app.include_router(order_router, prefix="/order", tags=["Order"])

@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}

@customer_route.get('/customer')
def customer():
    print('customer')
    return get_customer()
# app.include_router(report_route)
app.include_router(product_route)
