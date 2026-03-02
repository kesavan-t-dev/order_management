from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductUpdate
from uuid import UUID

def get_all_products(db: Session):
    return db.query(Product).filter(Product.is_active == True).all()

    
def delete_product(db: Session, product_id: UUID):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        product.is_active = False 
        db.commit()
        return True
    return False