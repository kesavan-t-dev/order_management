from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from db import Base
from project.orders.models import ist_now
import uuid

class Product(Base):
    __tablename__ = 'product'

    id = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4)
    name = Column(String(256), nullable= False)
    brand = Column(String(100))
    category = Column(String(100))
    price = Column(String(10), nullable= False)
    created_at = Column(DateTime(timezone=False), default=ist_now)
    updated_at = Column(DateTime(timezone=False), default=ist_now, onupdate=ist_now)
    is_active = Column(Boolean, default = True)



