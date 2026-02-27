# main.py
from fastapi import FastAPI

# Create a FastAPI "instance"
app = FastAPI()

# Define a path operation decorator
@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "World"}