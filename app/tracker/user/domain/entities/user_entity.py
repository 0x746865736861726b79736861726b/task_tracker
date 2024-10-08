import copy
from datetime import datetime
from typing import Any, Callable

from app.core.error.invalid_exception import InvalidOperationError
from app.tracker.user.domain.entities.user_model import UserUpdateModel


class UserEntity(object):
    def __init__(
        self,
        id: int,
        email: str,
        password: str,
        is_active: bool | None = True,
        is_deleted: bool | None = False,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        tasks: list[int] = [],
    ):
        self.id = id
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_deleted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at
        self.tasks: list[int] = [] if tasks is None else tasks

    def update_entity(
        self,
        entity_update_model: "UserUpdateModel",
        get_update_data_fn: Callable[["UserUpdateModel"], dict[str, Any]],
    ) -> "UserEntity":
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, attr_value in update_data.items():
            setattr(update_entity, attr_name, attr_value)

        return update_entity

    def mark_entity_as_deleted(self) -> "UserEntity":
        if self.is_deleted:
            raise InvalidOperationError("User is already marked as deleted")

        mark_entity = copy.deepcopy(self)
        mark_entity.is_deleted = True

        return mark_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UserEntity):
            return self.id == other.id

        return False

    def to_pop(self) -> object:
        return self.__dict__
