from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey,Integer
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, DateTime
from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

def ist_now():
    return datetime.now(IST).replace(tzinfo=None)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id", ondelete="CASCADE"))
    order_date = Column(DateTime(timezone=False), default=ist_now)
    order_status = Column(String(50), nullable=False, default='Order placed')
    created_at = Column(DateTime(timezone=False), default=ist_now)
    updated_at = Column(DateTime(timezone=False), default=ist_now, onupdate=ist_now)

class Order_items(Base):
    __tablename__ = 'order_items'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, default=1) 
    total = Column(String) 
    created_at = Column(DateTime(timezone=False), default=ist_now)
    updated_at = Column(DateTime(timezone=False), default=ist_now, onupdate=ist_now)
    is_active = Column(Boolean, default=True)