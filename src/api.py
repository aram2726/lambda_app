from src.infrastructure.requests import LambdaRequest
from src.infrastructure.responses import LambdaResponse
from src.infrastructure.controllers import AnnouncementController


def get_view(event: dict, context: dict):
    request = LambdaRequest(event, context)
    controller = AnnouncementController(request, LambdaResponse())

    controller.get()
    return controller.response.data


def list_view(event: dict, context: dict):
    request = LambdaRequest(event, context)
    controller = AnnouncementController(request, LambdaResponse())

    controller.list()
    return controller.response.data


def create_view(event: dict, context: dict):
    request = LambdaRequest(event, context)
    controller = AnnouncementController(request, LambdaResponse())

    controller.create()
    return controller.response.data


def main(event: dict, context: dict):
    handlers = {
        "list": list_view,
        "create": create_view
    }
    route = event.pop("route")
    handler = handlers.get(route)
    if handler:
        return handler(event, context)
    return "Not Found"


if __name__ == '__main__':
    main(event, context)
