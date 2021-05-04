import json
from unittest import TestCase
from unittest.mock import Mock

from src.core.entities import AnnouncementEntity
from src.core.usecases import ListAnnouncementUseCase
from src.core.usecases import CreateAnnouncementUseCase
from src.infrastructure.responses import LambdaResponse


class BaseTestUseCase(TestCase):
    announcements = [{"uuid": 1, "title": "title1", "description": "description1"},
                     {"uuid": 2, "title": "title2", "description": "description2"}]

    def setUp(self) -> None:
        self.repo = Mock()
        self.response = LambdaResponse()


class TestListAnnouncementUseCase(BaseTestUseCase):
    def setUp(self) -> None:
        super().setUp()
        self.repo.get_all = Mock(return_value=(self.announcements, None))
        self.use_case = ListAnnouncementUseCase(self.response, self.repo)

    def test_execute(self):
        self.use_case.execute()
        assert self.response.data == bytes(json.dumps({"data": self.announcements, "next": None}), encoding="UTF-8")


class TestCreateAnnouncementUseCase(BaseTestUseCase):
    def setUp(self) -> None:
        super().setUp()
        entity = AnnouncementEntity(**self.announcements[0])
        self.use_case = CreateAnnouncementUseCase(self.response, self.repo, entity)

    def test_execute(self):
        self.use_case.execute()
        self.repo.insert.assert_called_once()
