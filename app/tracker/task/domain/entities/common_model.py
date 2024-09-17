from pydantic import BaseModel, Field


class TaskBaseModel(BaseModel):
    title: str = Field()
    owner_id: int = Field()
