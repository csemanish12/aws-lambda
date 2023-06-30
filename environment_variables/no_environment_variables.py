import json


def lambda_handler(event, context):
    # TODO implement
    username = 'my-username'
    password = 'password'
    database = 'database'
    host = 'host'
    conn = f"Connecting to db: {database} on host:{host} with user:{username} and password:{password}"

    return {
        'statusCode': 200,
        'body': json.dumps(conn)
    }