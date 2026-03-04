from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List, Optional
from datetime import datetime

class ItemCreate(BaseModel):
    product_id: UUID
    quantity: str
    total: str

class OrderData(BaseModel):
    customer_id: UUID
    order_status: Optional[str] = "Order placed"
    product_id: UUID
    quantity: int  
    total: str

    model_config = ConfigDict(from_attributes=True) 

class OrderResponse(BaseModel):
    message: str
    data: OrderData
    status_code: int


