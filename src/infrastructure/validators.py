from abc import ABCMeta
from abc import abstractmethod

from src.core.entities import AnnouncementEntity
from src.core.exceptions import AppException


class AbstractBaseValidator(metaclass=ABCMeta):
    errors = []

    @abstractmethod
    def is_valid(self):
        raise NotImplementedError


class AnnouncementValidator(AbstractBaseValidator):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def is_valid(self):
        try:
            AnnouncementEntity(**self.kwargs)
        except TypeError as exc:
            if isinstance(exc, AppException):
                self.errors.append(exc.args[0])
            else:
                self.errors.append({"message": "Invalid arguments."})
            return False
        return True
