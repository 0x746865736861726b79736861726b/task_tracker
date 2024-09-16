from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def create(self, entity):
        raise NotImplementedError

    @abstractmethod
    def findall(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
