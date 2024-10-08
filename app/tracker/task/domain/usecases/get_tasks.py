from typing import Sequence, Tuple
from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.tracker.task.domain.entities.task_query_model import TaskReadModel
from app.tracker.task.domain.services.task_query_service import TaskQueryService


class GetTasksUseCase(BaseUseCase):
    service: TaskQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        raise NotImplementedError


class GetTasksUseCaseImpl(GetTasksUseCase):

    def __init__(self, service: TaskQueryService):
        self.service: TaskQueryService = service

    def __call__(self, args: None) -> Sequence[TaskReadModel]:
        try:
            tasks = self.service.findall()
        except Exception:
            raise

        return tasks
