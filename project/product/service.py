from fastapi.responses import JSONResponse
from .models import Product
from fastapi import  HTTPException, status
import pymssql
import uuid
from app.product_worker import insert_product_to_sql,update_product_to_sql


def custom_response(message: str, status_code: int, properties: any):
    return {
        "status_code": status_code,
        "message": message,
        "properties": properties
    }

# def create_products(post,db):
#     existing_post = db.query(Product).filter(Product.name == post.name).first()
#     if existing_post:
#         return JSONResponse(
#             content={
#                 "status_code": 400,
#                 "message": f"Product '{post.name}' already exists.",
#             },
#             status_code=400
#         )

#     new_post = Product(**post.dict())    
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     response_data = {
#         "status_code": 200,
#         "message": "Product Created successfully",
#         "data": {
#            "name":new_post.name

#         }
#     }

#     product_name = new_post.name
#     product_brand = new_post.brand
#     product_category = new_post.category
#     product_id = new_post.id

#     new_id = str(uuid.uuid4()) 
#     conn = pymssql.connect(server="host.docker.internal\\SQLEXPRESS",
#          user='Mssql_db',
#          password='2025',
#          database='orders'
#       )
#     conn_str = conn.cursor()
#     query = "insert into product (id,product_name, product_brand,product_category,external_id) values(%s,%s,%s,%s,%s)"

#     conn_str.execute(query,(new_id,product_name,product_brand,product_category,product_id))
#     conn.commit()
#     conn_str.close()
#     conn.close()

#     return JSONResponse(content=response_data, status_code=200)

def create_products(post, db):
    existing_post = db.query(Product).filter(Product.name == post.name).first()
    if existing_post:
        return JSONResponse(
            content={
                "status_code": 400,
                "message": f"Product '{post.name}' already exists.",
            },
            status_code=400
        )

    # Create product in main DB
    new_post = Product(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    # Prepare response
    response_data = {
        "status_code": 200,
        "message": "Product Created successfully",
        "data": {"name": new_post.name}
    }

    # Send SQL Server insert to Celery background task
    insert_product_to_sql.delay(
        new_post.name,
        new_post.brand,
        new_post.category,
        new_post.id
    )

    return JSONResponse(content=response_data, status_code=200)


def read_products(db):
    posts = db.query(Product).filter(Product.is_active == True).all()

    if len(posts) <= 0:
        raise HTTPException(status_code=404, detail="No product exists")
    

    if len(posts) <= 0:
        raise HTTPException(status_code=404, detail="No product exists")
    
    users_data = []
    for u in posts:
        users_data.append({
            "name": u.name,
            "brand": u.brand,
            "category":u.category,
            "price" : u.price
            "category":u.category,
            "price" : u.price
        })
    
    return custom_response("Products retrieved successfully", 200, users_data)


# def update_products(item_id,update,db):
#     db_item = db.query(Product).filter(Product.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="User not found")

#     for key, value in update.dict(exclude_unset=True).items():
#         setattr(db_item, key, value)


#     db.commit()
#     db.refresh(db_item)
#     response_data = {
#         "status_code": 200,
#         "message": "Product Updated successfully",
#         "data": {
#            "name":db_item.name,
#            "brand":db_item.brand,
#            "category":db_item.category
#         }
#     }
#     update_data = update.dict(exclude_unset=True)

#     update_product_to_sql.delay(update_data,db_item,item_id)
#     return JSONResponse(content=response_data, status_code=200)
def update_products(item_id, update, db):

    # Fetch the product
    db_item = db.query(Product).filter(Product.id == item_id).first()
    
    if update.name == None and update.brand == None and update.category == None and update.price == None:
        raise HTTPException(status_code=404, detail="Enter values to update")
    
    
    if update.name == None and update.brand == None and update.category == None and update.price == None:
        raise HTTPException(status_code=404, detail="Enter values to update")
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Product not found")
        raise HTTPException(status_code=404, detail="Product not found")

    # Apply updates only for provided fields
    try:
        update_data = update.dict(exclude_unset=True) if hasattr(update, "dict") else dict(update)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid update data: {str(e)}")
    updated = {}
    for key, value in update_data.items():
        if hasattr(db_item, key):
            updated[key] = value
            setattr(db_item, key, value)

    # Commit changes
    try:
        db.commit()
        db.refresh(db_item)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database update failed: {str(e)}")

    # Prepare response
    response_data = {
        "status_code": 200,
        "message": "Product updated successfully",
        "data": updated
    }

    # Trigger async task safely
    try:
        
        update_product_to_sql.delay(update_data, item_id)
    except Exception as e:
        # Log the error but don't block the API response
        print(f"Async task failed: {e}")

    return JSONResponse(content=response_data, status_code=200)


def delete_products(item_id,db):
    db_item = db.query(Product).filter(Product.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if not db_item.is_active:
        raise HTTPException(status_code=404, detail="Product already deleted")
    
    db_item.is_active =False
    db.commit()
    db.refresh(db_item)
    return {"message": f"{db_item.name} Deleted Successfully"}





