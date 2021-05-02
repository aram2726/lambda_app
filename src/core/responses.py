from abc import ABCMeta, abstractmethod
from typing import Dict

CODE_OK = 200
CODE_DELETED = 204
CODE_CREATED = 201
CODE_BAD_REQUEST = 400
CODE_UNAUTHORIZED = 401
CODE_PERMISSION_DENIED = 403
CODE_NOT_FOUND = 404


class AbstractBaseResponse(metaclass=ABCMeta):
    """
    Response class abstraction.
    """

    def __init__(self):
        self._data = {}
        self._headers = {}
        self._status = CODE_OK

    @property
    @abstractmethod
    def data(self) -> Dict:
        raise NotImplementedError

    @data.setter
    @abstractmethod
    def data(self, data: Dict):
        raise NotImplementedError

    @property
    @abstractmethod
    def headers(self) -> Dict:
        raise NotImplementedError

    @headers.setter
    @abstractmethod
    def headers(self, headers: Dict):
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self) -> int:
        raise NotImplementedError

    @status.setter
    @abstractmethod
    def status(self, status: int):
        raise NotImplementedError
