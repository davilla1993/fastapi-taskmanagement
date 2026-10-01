from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    username: str
    password: str
    email: str

class UserResponse(BaseModel):
    name: str
    username: str
    email: str