from typing import Annotated

from sqlalchemy.orm import Session
from src.user import controller
from src.utils.db import get_db
from fastapi import APIRouter, Depends, status
from src.user.dto import UserRequest, UserResponse

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(request: UserRequest, db:db_dependency):
    return controller.register(request, db)