import sys
sys.path.append(".")


from flask import Flask, Response
from flask import request

from infrastructure.controllers import AnnouncementController
from infrastructure.requests import LambdaRequest
from infrastructure.responses import LambdaResponse


app = Flask("Announcements")


@app.route("/account/<uuid>")
def get_announcements(uuid: str):
    lambda_request = LambdaRequest(dict(request.args, uuid=uuid), {"identity": None})
    controller = AnnouncementController(lambda_request, LambdaResponse())
    controller.list()
    data = controller.response.data
    status = controller.response.status
    return Response(response=data, status=status)


@app.route("/list")
def list_announcements():
    lambda_request = LambdaRequest(dict(request.args), {"identity": None})
    controller = AnnouncementController(lambda_request, LambdaResponse())
    controller.list()
    data = controller.response.data
    status = controller.response.status
    return Response(response=data, status=status)


@app.route("/create", methods=("POST",))
def create_announcements():
    lambda_request = LambdaRequest(request.form, {"identity": None})
    controller = AnnouncementController(lambda_request, LambdaResponse())
    controller.create()
    data = controller.response.data
    status = controller.response.status
    return Response(response=data, status=status)


if __name__ == '__main__':
    app.run(debug=True)
