# main.py
from fastapi import FastAPI
from project.customer.api import * 
from project.orders.api import router as order_route
from project.product.api import router as product_route

app = FastAPI(debug=True)

app.include_router(customer_route)
app.include_router(product_route)
app.include_router(order_route, prefix="/order", tags=["Order"])


@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}


