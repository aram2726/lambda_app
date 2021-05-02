from unittest import TestCase
from unittest.mock import Mock

from src.infrastructure.repositories import AnnouncementRepository


class TestAnnouncementRepository(TestCase):
    announcements = [{"uuid": 1, "title": "title1", "description": "description1"},
                     {"uuid": 2, "title": "title2", "description": "description2"}]

    def setUp(self) -> None:
        db = Mock(select_all=Mock(return_value=self.announcements))
        self.repo = AnnouncementRepository(db=db)

    def test_get_all_should_return_list_with_same_entities(self):
        member_entities = self.repo.get_all()

        self.repo.db.select_all.assert_called_once()
        assert len(member_entities) == 2
        self.assertEqual(self.announcements[0]["title"], member_entities[0].title)

    def test_insert(self):
        data = self.announcements[0]
        self.repo.insert(data)
        self.repo.db.insert.assert_called_once()
