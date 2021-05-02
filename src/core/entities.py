from abc import ABCMeta
from datetime import datetime
from typing import Dict
from typing import Optional


class AbstractBaseEntity(metaclass=ABCMeta):

    def __init__(
            self,
            uuid: Optional[int] = None,
            date: Optional[datetime] = None
    ):
        self._uuid = uuid
        self._date = date or datetime.now()

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: int):
        self._uuid = uuid

    @property
    def date(self):
        return datetime.strftime(self._date, "%Y-%m-%d, %H:%M:%S")


class AnnouncementEntity(AbstractBaseEntity):
    def __init__(
            self,
            title: str,
            description: str,
            uuid: Optional[int] = None,
            date: Optional[datetime] = None
    ):
        super().__init__(uuid, date)
        self._title = title
        self._description = description

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    def serialize(self) -> Dict:
        return {
            "uuid": self.uuid,
            "title": self.title,
            "description": self.description,
            "date": self.date,
        }
