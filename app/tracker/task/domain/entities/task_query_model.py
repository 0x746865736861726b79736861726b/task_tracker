from datetime import datetime

from pydantic import Field

from app.tracker.task.domain.entities.task_entity import TaskEntity
from app.tracker.task.domain.entities.common_model import TaskBaseModel


class TaskReadModel(TaskBaseModel):
    id: int = Field()
    is_completed: bool = Field()
    is_deleted: bool = Field()
    create_at: datetime
    update_at: datetime

    class Config(object):
        orm_mode = True

    @classmethod
    def from_entity(cls, task: TaskEntity) -> "TaskReadModel":
        return cls(
            id=task.id,
            title=task.title,
            is_completed=task.is_completed,
            is_deleted=task.is_deleted,
            create_at=task.created_at,
            update_at=task.updated_at,
        )
