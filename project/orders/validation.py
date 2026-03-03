from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.dialects.postgresql import UUID
from typing import List, Optional
import uuid

class Order_serializer(BaseModel):
    
    id : UUID = uuid.uuid4
    order_id : UUID
    product_id : UUID
    quantity : str
    total : str

    model_config = ConfigDict(arbitrary_types_allowed=True)

class Order_update_serializer(BaseModel):

    order_id : UUID | None = None
    product_id : UUID | None = None
    quantity : str | None = None
    total : str | None = None
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class Order_response(BaseModel):
 
    message: str 
    properties: List[Order_serializer] | None
    status_code: int

    model_config = ConfigDict(arbitrary_types_allowed=True)

class Create_Order(BaseModel):
    
    id : UUID = uuid.uuid4
    order_id : UUID
    product_id : UUID
    quantity : str
    total : str
   
    model_config = ConfigDict(arbitrary_types_allowed=True)