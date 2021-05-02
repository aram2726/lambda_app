import sys
sys.path.append(".")

from flask import Flask, Response
from flask import request

from src.infrastructure.controllers import AnnouncementController
from src.infrastructure.requests import LambdaRequest
from src.infrastructure.responses import LambdaResponse


class CognitoIdentity:
    cognito_identity_id = "dummy"
    cognito_identity_pool_id = "dummy"


app = Flask("Announcements")


@app.route("/list")
def list_announcements():
    lambda_request = LambdaRequest(request.form, {"identity": CognitoIdentity()})
    controller = AnnouncementController(lambda_request, LambdaResponse())
    controller.list()
    data = controller.response.data
    status = controller.response.status
    return Response(response=data, status=status)


@app.route("/create", methods=("POST",))
def create_announcements():
    lambda_request = LambdaRequest(request.form, {"identity": CognitoIdentity()})
    controller = AnnouncementController(lambda_request, LambdaResponse())
    controller.create()
    data = controller.response.data
    status = controller.response.status
    return Response(response=data, status=status)


if __name__ == '__main__':
    app.run(debug=True)
