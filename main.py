 # main.py
from fastapi import FastAPI

app = FastAPI()


    
@app.get("/")
def read_root():
    """
    Handles GET requests to the root URL (/).
    """
    return {"Hello": "DATABASE_URL"}