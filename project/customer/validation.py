from pydantic import BaseModel, ConfigDict
from sqlalchemy.dialects.postgresql import UUID
from typing import List
import uuid

class Customer_serializer(BaseModel):
    
    name : str
    email : str
    number : str
    address : str
    city : str
    zip : str

    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    
class Customer_update_serializer(BaseModel):

    name : str | None = None
    email : str | None = None
    number : str | None = None
    address : str | None = None
    city : str | None = None
    zip : str | None = None
    model_config = ConfigDict(arbitrary_types_allowed=True)
    

class Customer_response(BaseModel):
 
    message: str 
    properties: List[Customer_serializer] | None
    status_code: int
    model_config = ConfigDict(arbitrary_types_allowed=True)
    

class Create_Customer(BaseModel):
    
    id : UUID = uuid.uuid4
    name : str
    email : str
    number : str
    address : str
    city : str
    zip : str 
    model_config = ConfigDict(arbitrary_types_allowed=True)
    