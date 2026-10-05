from pydantic import BaseModel


class TaskRequest(BaseModel):
    title:str
    description: str
    is_completed : bool = False


class TaskResponse(BaseModel):
    id: int
    title:str
    description: str
    is_completed : bool
    user_id: int | None = 0