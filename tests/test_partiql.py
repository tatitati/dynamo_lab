import os

import boto3

def test_partiql_query():
    os.environ['AWS_PROFILE'] = 'dev-legacy'
    client = boto3.client("dynamodb")

    response = client.execute_statement(
        Statement="SELECT * FROM mydynamotable WHERE email = 'newemail@company.org'"
    )

    for item in response["Items"]:
        print(item) # {'email': {'S': 'newemail@company.org'}, 'id': {'S': 'John'}}


def test_partiql_insert():
    os.environ['AWS_PROFILE'] = 'dev-legacy'
    client = boto3.client("dynamodb")

    client.execute_statement(
        Statement=f"INSERT INTO \"mydynamotable\" VALUE {{'id': ?, 'email': ?, 'age': ?}}",
        Parameters=[
            {'S': 'julius2'},
            {'S': 'secondemail@whatever.es'},
            {'N': '24'},
        ]
    )

def test_partiql_update():
    os.environ['AWS_PROFILE'] = 'dev-legacy'
    client = boto3.client("dynamodb")

    result = client.execute_statement(

        Statement=f'UPDATE \"mydynamotable\" SET email=? WHERE id=? AND age=?',
        Parameters=[
            {'S': 'updated_email@update.es'},
            {'S': 'julius2'},
            {'N': '24'},
        ]
    )

