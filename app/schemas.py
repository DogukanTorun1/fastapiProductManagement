from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# users schema
class UserBase(BaseModel):
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        form_attributes = True

# auth schema

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# products schema

class ProductBase(BaseModel):
    name: str
    quantity: int
    product_type_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    product_type_id: Optional[int] = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        form_attributes = True

# product types schema

class ProductTypeBase(BaseModel):
    type_name: str

class ProductTypeCreate(ProductTypeBase):
    type_name: str

class ProductTypeResponse(ProductTypeBase):
    id: int
    class Config:
        form_attributes = True