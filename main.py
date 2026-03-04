from fastapi import FastAPI
from project.customer.api import customer_route
from project.orders.api import router as order_route
from project.product.api import router as product_route
from project.customer.models import Customer
from project.product.models import Product
from project.orders.models import Order, Order_items

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


