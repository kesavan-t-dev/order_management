from fastapi.responses import JSONResponse
from .models import Product
from fastapi import  HTTPException, status
import pymssql
import uuid


def custom_response(message: str, status_code: int, properties: any):
    return {
        "status_code": status_code,
        "message": message,
        "properties": properties
    }

def create_products(post,db):
    existing_post = db.query(Product).filter(Product.name == post.name).first()
    if existing_post:
        return JSONResponse(
            content={
                "status_code": 400,
                "message": f"Product '{post.name}' already exists.",
            },
            status_code=400
        )

    new_post = Product(**post.dict())    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    response_data = {
        "status_code": 200,
        "message": "Product Created successfully",
        "data": {
           "name":new_post.name

        }
    }

    product_name = new_post.name
    product_brand = new_post.brand
    product_category = new_post.category
    product_id = new_post.id

    new_id = str(uuid.uuid4()) 
    conn = pymssql.connect(server="host.docker.internal",
         user='user2025',
         password='2025',
         database='order_management'
      )
    conn_str = conn.cursor()
    query = "insert into product (id,product_name, product_brand,product_category,external_id) values(%s,%s,%s,%s,%s)"

    conn_str.execute(query,(new_id, product_name, product_brand, product_category, product_id))
    conn.commit()
    conn_str.close()
    conn.close()

    return JSONResponse(content=response_data, status_code=200)


def read_products(db):
    posts = db.query(Product).filter(Product.is_active == True).all()

    if len(posts) <= 0:
        raise HTTPException(status_code=404, detail="No product exists")
    
    users_data = []
    for u in posts:
        users_data.append({
            "name": u.name,
            "brand": u.brand,
            "category":u.category,
            "price" : u.price
        })
    
    return custom_response("Products retrieved successfully", 200, users_data)


def update_products(item_id,update,db):
    updated = {}
    db_item = db.query(Product).filter(Product.id == item_id).first()
    
    if update.name == None and update.brand == None and update.category == None and update.price == None:
        raise HTTPException(status_code=404, detail="Enter values to update")
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in update.dict(exclude_unset=True).items():
        updated[key] = value
        setattr(db_item, key, value)


    db.commit()
    db.refresh(db_item)
    response_data = {
        "status_code": 200,
        "message": "Product Updated successfully",
        "data": updated
    }
    update_data = update.dict(exclude_unset=True)
    fields = []
    values = []

    if "name" in update_data:
        db_item.name = update_data["name"]
        fields.append("product_name=%s")
        values.append(db_item.name)

    if "brand" in update_data:
        db_item.brand = update_data["brand"]
        fields.append("product_brand=%s")
        values.append(db_item.brand)

    if "category" in update_data:
        db_item.category = update_data["category"]
        fields.append("product_category=%s")
        values.append(db_item.category)

    if fields:  
        values.append(str(item_id))
        sql_query = f"UPDATE product SET {', '.join(fields)} WHERE external_id=%s"

        conn = pymssql.connect(
            server="host.docker.internal",
            user="user2025",
            password="2025",
            database="order_management"
        )
        cursor = conn.cursor()
        cursor.execute(sql_query, tuple(values))
        conn.commit()
        cursor.close()
        conn.close()

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