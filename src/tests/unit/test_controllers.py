from unittest import TestCase
from unittest.mock import Mock

from src.infrastructure.controllers import AnnouncementController


class TestAnnouncementController(TestCase):
    announcements = {"Items": [{"uuid": 1, "title": "title1", "description": "description1"}]}

    def setUp(self) -> None:
        self.repo = Mock()

        self.request = Mock()
        self.response = Mock()
        self.controller = AnnouncementController(self.request, self.response)
        self.controller._announcements_repo = self.repo

    def test_list(self):
        self.repo.get_all = Mock(return_value=(self.announcements["Items"], None))
        self.controller.list()
        assert self.response.data["data"] == self.announcements["Items"]
        assert self.response.status == 200

    def test_insert(self):
        self.request.data = self.announcements["Items"][0]
        self.controller.create()
        assert self.controller.announcements_repo.insert.called_once()
        assert self.response.status == 201
