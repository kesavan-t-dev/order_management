# main.py
from fastapi import FastAPI
from project.customer.api import * 

# Create a FastAPI "instance"
# app = FastAPI()
app = FastAPI(debug=True)

# app.include_router(customer_route)
# app.include_router(product_route)
# app.include_router(order_route)

# Define a path operation decorator
@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}

# @app.get('/customer')
# def customer():
#     return get_customer()