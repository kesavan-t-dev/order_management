from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from typing import List, Optional
import uuid

class Product_serializer(BaseModel):
    
    id : UUID = uuid.uuid4
    name : str
    brand : str
    category : str
    price : str
    
    class Config:
        from_attributes = True

class Product_update_serializer(BaseModel):

    name : str | None = None
    brand : str | None = None
    category : str | None = None
    price : str | None = None
    
    class Config:
        from_attributes = True

class Product_response(BaseModel):
 
    message: str 
    properties: List[Product_serializer] | None
    status_code: int

    class Config:
        from_attributes = True

class Create_Product(BaseModel):
    
    id : UUID = uuid.uuid4
    name : str
    brand : str
    category : str
    price : str
   
    class Config:
        from_attributes = True