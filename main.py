# main.py
from fastapi import FastAPI
from project.customer.api import * 
from project.product.api import router as product_route

app = FastAPI(debug=True)

app.include_router(customer_route)
# app.include_router(report_route)
app.include_router(product_route)
