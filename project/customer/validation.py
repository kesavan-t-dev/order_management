from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from typing import List, Optional
import uuid

class Customer_serializer(BaseModel):
    
    id : UUID = uuid.uuid4
    name : str
    email : str
    number : str
    address : str
    city : str
    zip : str

    class Config:
        from_attributes = True

class Customer_update_serializer(BaseModel):

    name : str | None = None
    email : str | None = None
    number : str | None = None
    address : str | None = None
    city : str | None = None
    zip : str | None = None
    
    class Config:
        from_attributes = True

class Customer_response(BaseModel):
 
    message: str 
    properties: List[Customer_serializer] | None
    status_code: int

    class Config:
        from_attributes = True

class Create_Customer(BaseModel):
    
    id : UUID = uuid.uuid4
    name : str
    email : str
    number : str
    address : str
    city : str
    zip : str 
   
    class Config:
        from_attributes = True