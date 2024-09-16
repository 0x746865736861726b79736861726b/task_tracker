class BaseError(Exception):
    message: str = "Internal error"

    def __str__(self):
        return self.message
