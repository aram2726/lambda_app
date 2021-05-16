from abc import ABCMeta
from typing import Any
from typing import Optional

from src.core.entities import AnnouncementEntity
from src.core.responses import CODE_BAD_REQUEST
from src.core.responses import CODE_CREATED
from src.core.responses import CODE_OK
from src.core.usecases import GetAnnouncementUseCase
from src.core.usecases import CreateAnnouncementUseCase
from src.core.usecases import ListAnnouncementUseCase
from src.infrastructure.databases import DynamoDBClient
from src.infrastructure.validators import AbstractBaseValidator
from src.infrastructure.validators import AnnouncementValidator
from src.infrastructure.requests import LambdaRequest
from src.infrastructure.responses import LambdaResponse
from src.infrastructure.repositories import AnnouncementRepository


class AbstractBaseController(metaclass=ABCMeta):

    def __init__(self):
        self._db: Optional[DynamoDBClient] = None
        self._announcements_repo: Optional[AnnouncementRepository] = None
        self._validator: Optional[AbstractBaseValidator] = None

    @property
    def db(self):
        if self._db is None:
            self._db = DynamoDBClient()
        return self._db

    @property
    def announcements_repo(self):
        if self._announcements_repo is None:
            self._announcements_repo = AnnouncementRepository(self.db)
        return self._announcements_repo

    @property
    def validator(self) -> AbstractBaseValidator:
        return self._validator


class AbstractBaseHttpController(AbstractBaseController, metaclass=ABCMeta):
    def __init__(self, request: LambdaRequest, response: LambdaResponse):
        super().__init__()
        self._request = request
        self._response = response

    @property
    def request(self) -> LambdaRequest:
        return self._request

    @property
    def response(self) -> LambdaResponse:
        return self._response

    @response.setter
    def response(self, data: Any):
        self._response.data = data


class AnnouncementController(AbstractBaseHttpController):

    @property
    def validator(self):
        if self._validator is None:
            self._validator = AnnouncementValidator(**self.request.data)
        return self._validator

    def get(self):
        uc = GetAnnouncementUseCase(self.response, self.announcements_repo, self.request.args)

    def list(self):
        uc = ListAnnouncementUseCase(self.response, self.announcements_repo, **self.request.data)
        uc.execute()
        self.response.status = CODE_OK

    def create(self):
        if not self.validator.is_valid():
            self.response.status = CODE_BAD_REQUEST
            self.response.data = self.validator.errors
            return

        announcement = AnnouncementEntity(**self.request.data)
        uc = CreateAnnouncementUseCase(self.response, self.announcements_repo, announcement)
        uc.execute()
        self.response.status = CODE_CREATED


class CLIController(AbstractBaseController):

    def migrate(self):
        self.db.migrate()
