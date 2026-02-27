# main.py
from fastapi import FastAPI
from db import database_url

# Create a FastAPI "instance"
app = FastAPI()

print(database_url)
# Define a path operation decorator
@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": database_url}