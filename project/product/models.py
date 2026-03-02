from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from db import Base
import uuid



class Product(Base):
    __tablename__ = 'product'

    id = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4())
    name = Column(String(256), nullable= False)
    brand = Column(String(100))
    category = Column(String(100))
    price = Column(String(5), nullable= False)
    created_at = Column(DateTime, default = datetime.now())
    update_at = Column(DateTime, default = datetime.now(), onupdate= datetime.now())
    is_active = Column(Boolean, default = True)