from src.infrastructure.requests import LambdaRequest
from src.infrastructure.responses import LambdaResponse
from src.infrastructure.controllers import AnnouncementController


class View:

    def __init__(self, event: dict, context: dict):
        request = LambdaRequest(event, context)
        self.controller = AnnouncementController(request, LambdaResponse())

    def list(self):
        self.controller.list()
        return self.controller.response

    def create(self):
        self.controller.create()
        return self.controller.response
