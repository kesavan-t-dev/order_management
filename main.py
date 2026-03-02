 # main.py
from fastapi import FastAPI
from project.customer.api import * 

<<<<<<< HEAD
app = FastAPI()
=======
# Create a FastAPI "instance"
# app = FastAPI()
app = FastAPI(debug=True)

# app.include_router(customer_route)
# app.include_router(product_route)
# app.include_router(order_route)
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531


    
@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
<<<<<<< HEAD
    return {"Hello": "DATABASE_URL"}
=======
    return {"Hello": "World"}

# @app.get('/customer')
# def customer():
#     return get_customer()
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531
