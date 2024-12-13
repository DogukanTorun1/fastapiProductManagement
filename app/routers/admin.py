from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, utils

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)

@router.post("/create-admin", status_code=status.HTTP_201_CREATED)
def create_admin_user(db: Session = Depends(get_db)):
    # Check if an admin already exists
    existing_admin = db.query(models.User).filter(models.User.email == "admin@admin.com").first()
    if existing_admin:
        raise HTTPException(status_code=400, detail="Admin user already exists")

    # Create the admin user
    hashed_password = utils.hash("admin")  # Replace this with a more secure password if needed
    admin_user = models.User(
        full_name="admin",
        email="admin@admin.com",
        password=hashed_password,
        role="admin"
    )
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)

    return {"message": "Admin user created successfully", "user": admin_user}
