from abc import ABC, abstractmethod


class QueryService(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def findall(self) -> None:
        raise NotImplementedError
