import boto3

def test_partiql():
    client = boto3.client("dynamodb")

    response = client.execute_statement(
        Statement="SELECT * FROM mydynamotable WHERE id = 'John'"
    )

    for item in response["Items"]:
        print(item) # {'email': {'S': 'newemail@company.org'}, 'id': {'S': 'John'}}