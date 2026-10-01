from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.user.dto import UserRequest
from src.user.models import User

from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def register(request:UserRequest, db:Session):
    exists_user = (db.query(User)
               .filter(User.username == request.username)
               .first())
    if exists_user :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exist")

    exists_email = (db.query(User)
               .filter(User.email == request.email)
               .first())
    if exists_email :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exist")


    new_user = User(
        name = request.name,
        username = request.username,
        hash_password = get_password_hash(request.password),
        email = request.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user