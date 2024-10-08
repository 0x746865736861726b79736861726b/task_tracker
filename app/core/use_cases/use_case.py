from abc import ABC, abstractmethod


class BaseUseCase(ABC):
    @abstractmethod
    def __call__(self, *args):
        raise NotImplementedError
