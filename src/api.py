from src.infrastructure.requests import LambdaRequest
from src.infrastructure.responses import LambdaResponse
from src.infrastructure.controllers import AnnouncementController


def list_view(event: dict, context: dict):
    request = LambdaRequest(event, context)
    controller = AnnouncementController(request, LambdaResponse())

    controller.list()
    return controller.response


def create_view(event: dict, context: dict):
    request = LambdaRequest(event, context)
    controller = AnnouncementController(request, LambdaResponse())

    controller.create()
    return controller.response