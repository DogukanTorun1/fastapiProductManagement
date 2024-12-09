from .. import oauth2
from .. import schemas, models, utils
from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Create a Product
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product_type = db.query(models.ProductType).filter(models.ProductType.id == product.product_type_id).first()
    if not product_type:
        raise HTTPException(status_code=404, detail="Product type not found")
    new_product = models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Get All Products
@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), 
    current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

# Get a Single Product by ID
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Update a Product
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product_update: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

# Delete a Product
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}