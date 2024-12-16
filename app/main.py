from fastapi import FastAPI 
from . import models
from .routers import user, auth, product, producttype, admin
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(producttype.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"Hello": "World Actions Deneme 2"}


