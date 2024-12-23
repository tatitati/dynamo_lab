import boto3
from pydantic import BaseModel
from typing import Optional

from pydantic_dynamo.v2.models import GetResponse
from pydantic_dynamo.v2.sync_repository import SyncDynamoRepository

# cons: this library is VERY CONFUSING

class MytableRecord(BaseModel):
    id: str
    email: str
    age: int

def test_mytest():
    from pydantic_dynamo.v2.repository import DynamoRepository

    resource = boto3.resource('dynamodb')
    repo = DynamoRepository[MytableRecord](
        item_class=MytableRecord,
        partition_prefix="id",
        partition_name="id",
        content_type="MytableRecord",
        table_name="mydynamotable",
        partition_key="id",
        sort_key=None,
        table=resource.Table("mydynamotable"),
        resource=resource,
        consistent_reads=False,  # default
    )

    sync_repo = SyncDynamoRepository[MytableRecord](async_repo=repo)
    response: GetResponse = sync_repo.get(partition_id='id', content_id=["John"])
    print(response)

