from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime

import uuid


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(UUID, primary_key= True, default= uuid.uuid4)
    name = Column(String(256), nullable= False)
    email = Column(String(100), unique= True)
    number = Column(String(10), unique= True)
    address = Column(String(256), nullable = False)
    city = Column(String(50), nullable = False)
    zip = Column(String(6), nullable = False)
    created_at = Column(DateTime, default = datetime.now())
    update_at = Column(DateTime, default = datetime.now(), onupdate= datetime.now())
    is_active = Column(Boolean, default = True)