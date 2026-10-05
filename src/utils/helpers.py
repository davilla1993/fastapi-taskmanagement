from fastapi import HTTPException, status, Request, Depends
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from src.user.models import User
from src.utils.db import get_db
from src.utils.settings import settings
from datetime import datetime
import jwt

def is_authenticated(request:Request, db:Session = Depends(get_db)):
    try:
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")
        exp_time = int(data.get("exp"))

        current_time = datetime.now().timestamp()
        if current_time > exp_time:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized")

        user = (db.query(User)
                .filter(User.id == user_id)
                .first())
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized")