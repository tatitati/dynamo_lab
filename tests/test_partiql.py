import boto3

def test_partiql():
    client = boto3.client("dynamodb")

    response = client.execute_statement(
        Statement="SELECT * FROM my_table WHERE id = '123'"
    )

    for item in response["Items"]:
        print(item)