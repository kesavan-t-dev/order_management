# main.py
from fastapi import FastAPI
from project.customer.api import * 
from project.product.api import * 
from project.orders.api import router as order_router
from project.product.api import router as product_route

# Create a FastAPI "instance"
# app = FastAPI()

app = FastAPI(debug=True)

app.include_router(customer_route)
app.include_router(product_route)
app.include_router(order_router, prefix="/order", tags=["Order"])

# app.include_router(router)
# app.include_router(order_route)
# app.include_router(olap_router, prefix="/olap", tags=["OLAP"])

@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}


