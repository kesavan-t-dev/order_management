# main.py
from fastapi import FastAPI
from project.product.api import router as product_route

app = FastAPI(debug=True)

app.include_router(product_route)
