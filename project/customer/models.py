from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from db import Base
from project.orders.models import ist_now
import uuid

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4)
    name = Column(String(256), nullable= False)
    email = Column(String(100), unique= True)
    number = Column(String(10), unique= True)
    address = Column(String(256), nullable = False)
    city = Column(String(50), nullable = False)
    zip = Column(String(6), nullable = False)
    created_at = Column(DateTime(timezone=False), default=ist_now)
    updated_at = Column(DateTime(timezone=False), default=ist_now, onupdate=ist_now)
    is_active = Column(Boolean, default = True)
