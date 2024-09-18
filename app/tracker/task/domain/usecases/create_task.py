from typing import Tuple
from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.tracker.task.domain.entities.task_entity import TaskEntity
from app.tracker.task.domain.entities.task_query_model import TaskReadModel
from app.tracker.task.domain.entities.task_command_model import TaskCreateModel
from app.tracker.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class CreateTaskCase(BaseUseCase[Tuple[TaskCreateModel], TaskReadModel]):
    unit_of_work: TaskUnitOfWork

    @abstractmethod
    def __call__(self, command: TaskCreateModel) -> TaskReadModel:
        raise NotImplementedError


class CreateTaskUseCaseImpl(CreateTaskCase):
    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[TaskCreateModel]) -> TaskReadModel:
        (data,) = args
        task = TaskEntity(
            id=None,
            **data.dict(),
        )

        try:
            self.unit_of_work.task_repo.create(task)
        except Exception as ex:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_task = self.unit_of_work.task_repo.find_by_owner_id(task.owner_id)[0]

        return TaskReadModel.from_entity(created_task)
