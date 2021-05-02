from typing import List
from typing import Tuple

from src.core.entities import AnnouncementEntity
from src.core.repositories import BaseManageableRepository
from src.core.repositories import DEFAULT_LIMIT
from src.infrastructure.databases import DynamoDBClient


class AnnouncementRepository(BaseManageableRepository):

    def __init__(self, db: DynamoDBClient):
        self._db = db
        self._table = "announcements"

    @property
    def table(self):
        return self._table

    @property
    def db(self):
        return self._db

    def get_all(self, after=0, limit=DEFAULT_LIMIT, order=None) -> Tuple[List[AnnouncementEntity], str]:
        data, next_page = self.db.select_all(self.table, limit, after, order)
        return [AnnouncementEntity(**item) for item in data], next_page

    def insert(self, data: dict):
        self.db.insert(self.table, data)
