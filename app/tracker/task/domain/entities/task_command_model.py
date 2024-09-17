from pydantic import Field

from app.tracker.task.domain.entities.common_model import TaskBaseModel


class TaskCreateModel(TaskBaseModel):
    pass


class TaskUpdateModel(TaskBaseModel):
    is_completed: bool = Field()
    is_deleted: bool = Field()
