from src.utils.db import get_db
from src.tasks import controller
from typing import Annotated,List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.tasks.dto import TaskRequest, TaskResponse
from src.utils.helpers import is_authenticated
from src.user.models import User

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(request:TaskRequest, db:db_dependency, user:User=Depends(is_authenticated)):
    return controller.create_task(request, db, user)

@router.get("/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
async def get_all_tasks(db:db_dependency, user:User=Depends(is_authenticated)):
    return controller.get_tasks(db, user)

@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK )
async def get_one_task(task_id:int, db:db_dependency, user:User=Depends(is_authenticated)):
    return controller.get_one_task(task_id, db)


@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def update_task(request:TaskRequest, task_id:int, db:db_dependency, user:User=Depends(is_authenticated)):
    return controller.update_task(request, task_id, db)

@router.delete("/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id:int, db:db_dependency, user:User=Depends(is_authenticated)):
    return controller.delete_task(task_id, db)