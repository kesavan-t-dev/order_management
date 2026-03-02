from .validation import *
from .models import Customer
from fastapi import  status, Response
import uuid


def customer_list(db):
    print(db)