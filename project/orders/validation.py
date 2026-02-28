from pydantic import BaseModel
from uuid import UUID
from typing import List

class ItemCreate(BaseModel):
    product_id: UUID
    quantity: str
    total: str

class OrderCreate(BaseModel):
    customer_id: UUID
    items: List[ItemCreate]


class OrderResponse(BaseModel):
    message: str
    order_id: UUID
    status_code: int
