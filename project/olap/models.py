import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from db import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    customer_name = Column(String(150), nullable=False)
    customer_number = Column(String(20), unique=True, nullable=True)

    email = Column(String(255), unique=True, nullable=False)

    orders = relationship("Orders", back_populates="customer")


class Product(Base):
    __tablename__ = "product"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    product_name = Column(String(150), nullable=False, unique=True)
    product_brand = Column(String(50), nullable=True)

    orders = relationship("Orders", back_populates="product")


class Type(Base):
    __tablename__ = "task"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    type_name = Column(String(100), nullable=False, unique=True)

    orders = relationship("Orders", back_populates="type")


class Orders(Base):
    __tablename__ = "orders"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    customer_id = Column(UNIQUEIDENTIFIER, ForeignKey("customer.id"), nullable=False)
    product_id = Column(UNIQUEIDENTIFIER, ForeignKey("product.id"), nullable=False)
    type_id = Column(UNIQUEIDENTIFIER, ForeignKey("task.id"), nullable=False)

    order_id = Column(UNIQUEIDENTIFIER, nullable=False)

    quantity = Column(String(50), nullable=False)
    price = Column(String(50), nullable=False)

    date = Column(DateTime, nullable=True)

    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    type = relationship("Type", back_populates="orders")