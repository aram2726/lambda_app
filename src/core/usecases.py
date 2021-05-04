from abc import ABCMeta
from abc import abstractmethod
from typing import Optional

from src.core.entities import AnnouncementEntity
from src.core.repositories import BaseManageableRepository
from src.core.responses import AbstractBaseResponse


class AbstractBaseUseCase(metaclass=ABCMeta):
    def __init__(self, response: AbstractBaseResponse, repo: BaseManageableRepository):
        self._response = response
        self._repo = repo

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class ListAnnouncementUseCase(AbstractBaseUseCase):

    def __init__(
            self,
            response: AbstractBaseResponse,
            repo: BaseManageableRepository,
            after: Optional[int] = None,
            limit: Optional[int] = None,
            order: Optional[str] = None
    ):
        super().__init__(response, repo)
        self._after = after
        self._limit = limit
        self._order = order

    def execute(self):
        data, next_page = self._repo.get_all(self._after, self._limit, self._order)
        response = {
            "data": data,
            "next": next_page,
        }
        self._response.data = response


class CreateAnnouncementUseCase(AbstractBaseUseCase):

    def __init__(self, response: AbstractBaseResponse, repo: BaseManageableRepository, data: AnnouncementEntity):
        super().__init__(response, repo)
        self._data = data

    def execute(self):
        self._repo.insert(self._data.serialize())
        self._response.data["data"] = self._data
