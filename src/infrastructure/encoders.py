import json

from src.core.entities import AbstractBaseEntity
from src.infrastructure.exceptions import APIException


class ResponseEncoder(json.JSONEncoder):
    def default(self, instance):
        if issubclass(instance.__class__, AbstractBaseEntity):
            data = instance.serialize()
            return {**data}
        if issubclass(instance.__class__, APIException):
            return instance.args[0]
        return super().default(instance)
