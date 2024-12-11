from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from .. import oauth2
from ..database import get_db

router = APIRouter(
    prefix="/product-types",
    tags=["Product Types"]
)

# Create a Product Type
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProductTypeResponse)
def create_product_type(product_type: schemas.ProductTypeCreate, db: Session = Depends(get_db)):
    # Check if product type already exists
    existing_type = db.query(models.ProductType).filter(models.ProductType.type_name == product_type.type_name).first()
    if existing_type:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product type already exists")

    new_product_type = models.ProductType(**product_type.model_dump())
    db.add(new_product_type)
    db.commit()
    db.refresh(new_product_type)
    return new_product_type

# Get All Product Types
@router.get("/", response_model=list[schemas.ProductTypeResponse])
def get_product_types(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    product_types = db.query(models.ProductType).offset(skip).limit(limit).all()
    return product_types

# Get a Single Product Type by ID
@router.get("/{type_id}", response_model=schemas.ProductTypeResponse)
def get_product_type(type_id: int, db: Session = Depends(get_db)):
    product_type = db.query(models.ProductType).filter(models.ProductType.id == type_id).first()
    if not product_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product type not found")
    return product_type

# Update a Product Type
@router.put("/{type_id}", response_model=schemas.ProductTypeResponse)
def update_product_type(type_id: int, updated_type: schemas.ProductTypeCreate, db: Session = Depends(get_db)):
    product_type = db.query(models.ProductType).filter(models.ProductType.id == type_id).first()
    if not product_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product type not found")

    product_type.type_name = updated_type.type_name
    db.commit()
    db.refresh(product_type)
    return product_type

# Delete a Product Type
@router.delete("/{type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_type(type_id: int, db: Session = Depends(get_db)):
    product_type = db.query(models.ProductType).filter(models.ProductType.id == type_id).first()
    if not product_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product type not found")

    db.delete(product_type)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
