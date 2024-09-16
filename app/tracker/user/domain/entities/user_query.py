from datetime import datetime

from pydantic import Field

from app.tracker.user.domain.entities.user_entity import UserEntity
from app.tracker.user.domain.entities.user_common_model import UserBaseModel


class UserReadModel(UserBaseModel):
    id: int = Field()
    email: str = Field()
    password: str = Field()
    is_active: bool = Field()
    is_deleted: bool = Field()
    created_at: datetime
    updated_at: datetime
    tasks: list[int]

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(user: UserEntity) -> "UserReadModel":
        return UserReadModel(**user.dict())
