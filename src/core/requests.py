from abc import ABCMeta, abstractmethod
from typing import Dict


class AbstractBaseRequest(metaclass=ABCMeta):
    """
    Lambda request abstract parser class.
    """

    def __init__(self, event, context):
        self.event = event
        self.context = context

    @property
    @abstractmethod
    def data(self) -> Dict:
        raise NotImplementedError

    @property
    @abstractmethod
    def user(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def request_id(self) -> str:
        raise NotImplementedError
