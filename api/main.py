from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.models.Task import Task
from app.models.task_pydantic import TaskResponse,TaskCreate

app = FastAPI()
session = SessionLocal()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(name=task.name, description=task.description, deadline=task.deadline, is_completed=task.is_completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.get("/all_tasks", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks