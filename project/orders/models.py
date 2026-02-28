from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from typing import List, Optional
import uuid

class Order_serializer(BaseModel):
    
    id : UUID = uuid.uuid4
    order_id : UUID
    product_id : UUID
    quantity : str
    total : str

    class Config:
        from_attributes = True

class Order_update_serializer(BaseModel):

    order_id : UUID | None = None
    product_id : UUID | None = None
    quantity : str | None = None
    total : str | None = None
    
    class Config:
        from_attributes = True

class Order_response(BaseModel):
 
    message: str 
    properties: List[Order_serializer] | None
    status_code: int

    class Config:
        from_attributes = True

class Create_Order(BaseModel):
    
    id : UUID = uuid.uuid4
    order_id : UUID
    product_id : UUID
    quantity : str
    total : str
   
    class Config:
        from_attributes = True
