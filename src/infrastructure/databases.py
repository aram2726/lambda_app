from abc import ABCMeta
from abc import abstractmethod
from typing import Optional, Dict

import boto3


class AbstractBaseDBClient(metaclass=ABCMeta):

    def __init__(self):
        self._client = None

    @property
    def client(self):
        raise NotImplementedError

    @abstractmethod
    def select_all(
            self,
            table: str,
            limit: Optional[int] = None,
            after: Optional[int] = None,
            order: Optional[str] = None
    ):
        raise NotImplementedError

    @abstractmethod
    def insert(self, table: str, data: dict):
        raise NotImplementedError


class DynamoDBClient(AbstractBaseDBClient):

    @property
    def client(self):
        if self._client is None:
            self._client = boto3.resource(
                'dynamodb',
                endpoint_url='http://localhost:8000/',
                region_name='us-east-1',
                aws_access_key_id='dummy_access_key',
                aws_secret_access_key='dummy_secret_key',
                verify=False
            )
        return self._client

    def migrate(self):
        self.client.create_table(
            TableName='announcements',
            KeySchema=[
                {
                    'AttributeName': 'uuid',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'uuid',
                    'AttributeType': 'N'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

    def select_all(
            self,
            table_name: str,
            limit: Optional[int] = None,
            after: Optional[int] = None,
            order: Optional[str] = None
    ):
        kwargs = {
            "TableName": table_name
        }
        # if limit:
        #     kwargs["Limit"] = limit

        # if after:
        #     kwargs["ExclusiveStartKey"] = after

        if order:
            kwargs["ScanIndexForward"] = True if order == "asc" else False

        table = self.client.Table(table_name)
        response = table.scan(**kwargs)
        return response['Items'], response.get("LastEvaluatedKey")

    def insert(self, table_name: str, data: Dict):
        content = {key: {"S": data[key]} for key in data if data.get(key)}
        table = self.client.Table(table_name)
        item = {key: data[key] for key in data if data.get(key)}
        print(item)
        print(content)
        table.put_item(
            Item={
                "title": {"S": item["title"]},
                "description": {"S": item["description"]},
                "data": {"S": item["date"]}
            },
            TableName=table_name
        )
