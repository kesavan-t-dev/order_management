from fastapi.responses import JSONResponse
from .models import Product
from fastapi import  HTTPException
from app.product_worker import insert_product_to_sql, update_product_to_sql


def custom_response(message: str, status_code: int, properties: any):
    return {
        "status_code": status_code,
        "message": message,
        "properties": properties
    }

def create_products(post, db):
    existing_post = db.query(Product).filter(Product.name == post.name).first()
    if existing_post:
        return JSONResponse(
            content={
                "status_code": 400,
                "message": f"Product '{post.name}' already exists.",
            },
            status_code = 400
        )

    new_post = Product(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    response_data = {
        "status_code": 201,
        "message": "Product Created successfully",
        "data": {"name": new_post.name}
    }

    insert_product_to_sql.delay(
        new_post.name,
        new_post.brand,
        new_post.category,
        new_post.id
    )
    return JSONResponse(content = response_data, status_code = 200)

def read_products(db):
    posts = db.query(Product).filter(Product.is_active == True).all()

    if len(posts) <= 0:
        raise HTTPException(status_code = 400, detail = "No product exists")
    
    if len(posts) <= 0:
        raise HTTPException(status_code = 400, detail = "No product exists")
    
    users_data = []
    for u in posts:
        users_data.append({
            "name": u.name,
            "brand": u.brand,
            "category":u.category,
            "price" : u.price,
            "category":u.category

        })
    return custom_response("Products retrieved successfully", 200, users_data)

def update_products(item_id, update, db):

    db_item = db.query(Product).filter(Product.id == item_id).first()
    
    if update.name == None and update.brand == None and update.category == None and update.price == None:
        raise HTTPException(status_code = 400, detail = "Enter values to update")
    
    if not db_item:
        raise HTTPException(status_code = 400, detail = "Product not found")
        
    try:
        update_data = update.dict(exclude_unset = True) if hasattr(update, "dict") else dict(update)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = f"Invalid update data: {str(e)}")
    updated = {}
    for key, value in update_data.items():
        if hasattr(db_item, key):
            updated[key] = value
            setattr(db_item, key, value)
    try:
        db.commit()
        db.refresh(db_item)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code = 500, detail = f"Database update failed: {str(e)}")

    response_data = {
        "status_code": 201,
        "message": "Product updated successfully",
        "data": updated
    }

    try:
        
        update_product_to_sql.delay(update_data, item_id)
    except Exception as e:
        print(f"Async task failed: {e}")
    return JSONResponse(content = response_data, status_code = 200)


def delete_products(item_id,db):
    db_item = db.query(Product).filter(Product.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code = 400, detail="Product not found")
    
    if not db_item.is_active:
        raise HTTPException(status_code = 400, detail="Product already deleted")
    
    db_item.is_active = False
    db.commit()
    db.refresh(db_item)
    return {"message": f"{db_item.name} Deleted Successfully"}


