from typing import Dict

from src.core.requests import AbstractBaseRequest


class LambdaRequest(AbstractBaseRequest):

    @property
    def data(self) -> Dict:
        return dict(self.event.items())

    @property
    def user(self):
        """
        returns aws CognitoIdentity class instance
        example:

        class CognitoIdentity:
            cognito_identity_id: str
            cognito_identity_pool_id: str
        """
        return self.context.identity

    @property
    def request_id(self) -> str:
        return self.context.aws_request_id
