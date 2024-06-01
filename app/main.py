from fastapi import FastAPI
from app.routers import department
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(department.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
