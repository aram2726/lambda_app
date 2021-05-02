import json
from typing import AnyStr
from typing import Dict

from src.core.responses import AbstractBaseResponse
from src.infrastructure.encoders import ResponseEncoder


class LambdaResponse(AbstractBaseResponse):

    @property
    def data(self) -> AnyStr:
        return bytes(json.dumps(self._data, cls=ResponseEncoder), encoding="UTF-8")

    @data.setter
    def data(self, data: Dict):
        self._data = data

    @property
    def headers(self) -> Dict:
        return self._headers

    @headers.setter
    def headers(self, headers: Dict):
        self._headers.update(headers)

    @property
    def status(self) -> int:
        return self._status

    @status.setter
    def status(self, status: int):
        self._status = status
