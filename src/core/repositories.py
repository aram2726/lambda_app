from abc import ABCMeta
from abc import abstractmethod

DEFAULT_LIMIT = 10


class BaseReadOnlyRepository(metaclass=ABCMeta):

    @abstractmethod
    def get_one(self, pk_val: str):
        raise NotImplementedError

    @abstractmethod
    def get_all(self, after: str = "", limit: int = DEFAULT_LIMIT, order: str = None):
        raise NotImplementedError


class BaseManageableRepository(BaseReadOnlyRepository, metaclass=ABCMeta):

    @abstractmethod
    def insert(self, data: dict):
        raise NotImplementedError
