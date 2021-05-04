from unittest import TestCase
from unittest.mock import Mock

from src.infrastructure.databases import DynamoDBClient


class TestDynamoDBClient(TestCase):

    def setUp(self) -> None:
        self.db = DynamoDBClient()
        self.table = "announcements"
        self.db._client = Mock()
        self.announcements = {
            "Items": [
                {"uuid": 1, "title": "title1", "description": "description1"},
                {"uuid": 2, "title": "title2", "description": "description2"}
            ],
        }

    def test_select_all(self):
        table = Mock(scan=Mock(return_value=self.announcements,))
        self.db._client.Table.return_value = table

        data = self.db.select_all(self.table)

        assert len(data) == len(self.announcements["Items"])
        assert data[0] == self.announcements["Items"]

    def test_insert(self):
        table = Mock(put_item=Mock())
        item = self.announcements["Items"][0]
        self.db._client.Table.return_value = table
        self.db.insert(self.table, item)

        table.put_item.assert_called_once()
