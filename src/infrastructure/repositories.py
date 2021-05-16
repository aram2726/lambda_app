from typing import Optional
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
        self._pk_field = "uuid"

    @property
    def table(self):
        return self._table

    @property
    def db(self):
        return self._db

    def get_one(self, pk_val: str) -> Optional[AnnouncementEntity]:
        item = self.db.select_one(self.table, self._pk_field, pk_val)

        if not item:
            return None

        return AnnouncementEntity(**item)

    def get_all(
            self, after: str = "", limit: int = DEFAULT_LIMIT, order: str = None
    ) -> Tuple[List[AnnouncementEntity], str]:
        data, next_page = self.db.select_all(self.table, limit, after, order)
        return [AnnouncementEntity(**item) for item in data], next_page

    def insert(self, data: dict):
        self.db.insert(self.table, data)
