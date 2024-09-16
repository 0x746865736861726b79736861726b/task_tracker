from pydantic import Field, BaseModel


class UserBaseModel(BaseModel):
    email: str = Field(default="ex13@example.com")
