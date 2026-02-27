from sqlalchemy import Column,  String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID 
import uuid
from datetime import datetime
from ...db import Base


class Customer(Base):
    __tablename__ = "customer"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    customer_id = Column(UUID(as_uuid=True),nullable=False)
    customer_name = Column(String, nullable=False)
    customer_number = Column(String(20), unique=True, nullable=True)
    email = Column(String, unique=True, nullable=False)
    customer_address = Column(String(20), unique=True, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)


class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    product_id = Column(UUID(as_uuid=True),nullable=False)
    product_name = Column(String, nullable=False)
    product_brand = Column(String(20), unique=True, nullable=True)
    product_type = Column(String(20), unique=True, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)


class Orders(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    customer_id = Column(UUID(as_uuid=True),nullable=False)
    product_id = Column(UUID(as_uuid=True),nullable=False)
    order_id = Column(UUID(as_uuid=True),nullable=False)
    quantity = Column(String, nullable=False)
    price = Column(String, nullable=False)
    exported_at = Column(DateTime, default=None)
    
