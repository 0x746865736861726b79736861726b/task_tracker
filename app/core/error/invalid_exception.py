from app.core.error.base_exception import BaseError


class InvalidOperationError(BaseError):
    message = "Invalid operation"
