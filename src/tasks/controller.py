from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.tasks.dto import TaskRequest
from src.tasks.models import Task


def create_task(request:TaskRequest, db:Session):
    new_task = Task()
    new_task.title = request.title
    new_task.description = request.description
    new_task.is_completed = request.is_completed

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db:Session):
    tasks = db.query(Task).all()

    return tasks

def get_one_task(task_id:int, db:Session):
    task = db.query(Task).get(task_id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The task with ID={task_id} not found")

    return task


def update_task(request:TaskRequest, task_id:int, db:Session):
    exists_task = db.query(Task).get(task_id)

    if not exists_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The task with ID={task_id} not found")

    exists_task.title = request.title
    exists_task.description = request.description
    exists_task.is_completed = request.is_completed

    db.add(exists_task)
    db.commit()
    db.refresh(exists_task)

    return exists_task


def delete_task(task_id:int, db:Session):
    exist_task = db.query(Task).get(task_id)

    if not exist_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found with ID={task_id}")

    db.delete(exist_task)
    db.commit()

    return None