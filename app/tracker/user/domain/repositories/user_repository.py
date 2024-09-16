from abc import abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.tracker.user.domain.entities.user_entity import UserEntity


class UserRepository(BaseRepository):
    @abstractmethod
    def find_by_email(self, email: str) -> UserEntity | None:
        raise NotImplementedError
