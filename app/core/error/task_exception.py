from app.core.error.base_exception import BaseError


class TaskNotFoundError(BaseError):
    message = "Task not found"


class TasksNotFoundError(BaseError):
    message = "Tasks not found"


class TaskAlreadyExistsError(BaseError):
    message = "Task already exists"
