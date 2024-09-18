from typing import Tuple
from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.task_exception import TaskNotFoundError
from app.tracker.task.domain.entities.task_query_model import TaskReadModel
from app.tracker.task.domain.services.task_query_service import TaskQueryService
from app.tracker.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class GetTaskUseCase(BaseUseCase):
    unit_of_work: TaskUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        raise NotImplementedError


class GetTaskUseCaseImpl(GetTaskUseCase):

    def __init__(self, service: TaskQueryService):
        self.service: TaskQueryService = service

    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        (id,) = args
        try:
            task = self.service.find_by_id(id)
            if task is None:
                raise TaskNotFoundError()
        except Exception:
            raise

        return task
