import json
import os


def lambda_handler(event, context):
    # TODO implement
    username = os.environ.get('username')
    password = os.environ.get('password')
    database = os.environ.get('database')
    host = os.environ.get('host')
    conn = f"Connecting to db: {database} on host:{host} with user:{username} and password:{password}"

    return {
        'statusCode': 200,
        'body': json.dumps(conn)
    }
