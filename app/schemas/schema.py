from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class Task(TaskBase):
    id: int
    completed: bool

    model_config = {
        "from_attributes": True
    } 