from typing import cast, Tuple
from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.task_exception import TaskNotFoundError
from app.tracker.task.domain.entities.task_entity import TaskEntity
from app.tracker.task.domain.entities.task_query_model import TaskReadModel
from app.tracker.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class DeleteTaskUseCase(BaseUseCase):
    unit_of_work: TaskUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[TaskEntity]) -> TaskReadModel:
        raise NotImplementedError


class DeleteTaskUseCaseImpl(DeleteTaskUseCase):
    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work: TaskUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[TaskEntity]) -> TaskReadModel:
        (id,) = args

        existing_user = self.unit_of_work.task_repo.find_by_id(id)

        if existing_user is None:
            raise TaskNotFoundError()

        marked_user = existing_user.mark_entity_as_deleted()

        try:
            deleted_user = self.unit_of_work.task_repo.update(marked_user)
            self.unit_of_work.commit()
        except Exception as e:
            self.unit_of_work.rollback()
            raise

        return TaskReadModel.from_entity(cast(TaskEntity, deleted_user))
