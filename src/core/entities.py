from abc import ABCMeta
from datetime import datetime
from typing import Dict
from typing import Optional
from uuid import uuid4


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
        if isinstance(self._date, str):
            return self._date
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
    def uuid(self):
        if self._uuid is None:
            return str(uuid4())
        return self._uuid

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
