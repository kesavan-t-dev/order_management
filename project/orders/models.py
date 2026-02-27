from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Order_items(Base):
    __tablename__ = 'order_items'

    id = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("order.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    quantity = Column(String)
    total = Column(String)
    created_at = Column(DateTime, default = datetime.now())
    update_at = Column(DateTime, default = datetime.now(), onupdate= datetime.now())
    is_active = Column(Boolean, default = True)

class Order(Base):
    __tablename__ = 'order'

    id = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"))
    order_date = Column(DateTime, default = datetime.now())
    order_status = Column(String(50), nullable= False, default= 'Order placed')
    created_at = Column(DateTime, default = datetime.now())
    update_at = Column(DateTime, default = datetime.now(), onupdate= datetime.now())
