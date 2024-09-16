from pydantic import Field, BaseModel

from app.tracker.user.domain.entities.user_common_model import UserBaseModel


class UserCreateModel(UserBaseModel):
    password: str = Field()


class UserUpdateModel(UserBaseModel):
    email: str | None
    password: str | None = Field()
    is_active: bool | None = Field()
    is_deleted: bool | None = Field()
