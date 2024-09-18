from typing import Sequence

from app.core.services.base_query_service import BaseQueryService
from app.tracker.task.domain.entities.task_query_model import TaskReadModel


class TaskQueryService(BaseQueryService[TaskReadModel]):
    def find_by_owner_id(self, owner_id: int) -> Sequence[TaskReadModel]:
        raise NotImplementedError
