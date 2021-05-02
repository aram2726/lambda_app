from abc import ABCMeta
from abc import abstractmethod

from src.infrastructure.requests import LambdaRequest


class AbstractBasePermission(metaclass=ABCMeta):

    @abstractmethod
    def has_perm(self, request: LambdaRequest) -> bool:
        raise NotImplementedError
