from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.tracker.task.domain.repositories.task_repository import TaskRepository


class TaskUnitOfWork(AbstractUnitOfWork):
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def commit(self):
        self.task_repo.commit()

    def rollback(self):
        self.task_repo.rollback()

    def begin(self):
        pass
