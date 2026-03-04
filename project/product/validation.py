from pydantic import BaseModel, ConfigDict
from sqlalchemy.dialects.postgresql import UUID
from typing import List, Optional, Any
import uuid

class Product_serializer(BaseModel):
    
    id : UUID = uuid.uuid4()
    name : str
    brand : str
    category : str
    price : str
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class Product_update_serializer(BaseModel):

    name : str | None = None
    brand : str | None = None
    category : str | None = None
    price : str | None = None
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class Product_response(BaseModel):
 
    message: str 
    properties: Any
    status_code: int

    model_config = ConfigDict(arbitrary_types_allowed=True)

class Create_Product(BaseModel):
    
    id : UUID = uuid.uuid4()
    name : str
    brand : str
    category : str
    price : str
   
    model_config = ConfigDict(arbitrary_types_allowed=True)


