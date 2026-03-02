from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from db import Base
import uuid


class Customer(Base):
    __tablename__ = "customer"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    customer_name = Column(String(150), nullable=False)
    customer_number = Column(String(20), unique=True, nullable=True)

    email = Column(String(255), unique=True, nullable=False)



class Product(Base):
    __tablename__ = "product"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    product_name = Column(String(150), nullable=False, unique=True)
    product_brand = Column(String(50), nullable=True)
    product_category = Column(String(50), nullable=True)




class Orders(Base):
    __tablename__ = "orders"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)

    customer_id = Column(UNIQUEIDENTIFIER, nullable=False)
    product_id = Column(UNIQUEIDENTIFIER, nullable=False)
    order_id = Column(UNIQUEIDENTIFIER, nullable=False)

    quantity = Column(String(50), nullable=False)
    price = Column(String(50), nullable=False)

    date = Column(DateTime, nullable=True)
