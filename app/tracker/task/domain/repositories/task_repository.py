from typing import Sequence
from abc import abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.tracker.task.domain.entities.task_entity import TaskEntity


class TaskRepository(BaseRepository):
    @abstractmethod
    def find_by_owner_id(self, owner_id: int) -> Sequence[TaskEntity]:
        raise NotImplementedError
