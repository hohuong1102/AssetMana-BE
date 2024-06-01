from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)

@router.post("/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = models.Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

@router.get("/", response_model=List[schemas.Department])
def read_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    departments = db.query(models.Department).offset(skip).limit(limit).all()
    return departments
