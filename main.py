# main.py
from fastapi import FastAPI
from project.orders.api import router as order_router


app = FastAPI()

app.include_router(order_router, prefix="/order", tags=["Order"])

@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}