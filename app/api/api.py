from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas import schema
from app.crud import crud

router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{task_id}", response_model=schema.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/", response_model=schema.Task)
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task_id)
    return {"message": "Task deleted succesfully"}

@router.put("/{task_id}", response_model=schema.Task)
def update_task(task_id: int, task: schema.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)