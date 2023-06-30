import boto3
import json
import os

from base64 import b64decode

DECRYPTED_KEYS = {}


def decrypt(encrypted_key):
    decrypted_key = DECRYPTED_KEYS.get(encrypted_key)
    if decrypted_key:
        print("Found decrypted key in cache. Fetching decrypted key from cache")
        return decrypted_key

    print("decrypting key......")
    decrypted_key = boto3.client('kms').decrypt(
        CiphertextBlob=b64decode(encrypted_key),
        EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
    )['Plaintext'].decode('utf-8')
    DECRYPTED_KEYS[encrypted_key] = decrypted_key

    return decrypted_key


def lambda_handler(event, context):
    # TODO implement
    username = decrypt(os.environ.get('username'))
    password = decrypt(os.environ.get('password'))
    database = decrypt(os.environ.get('database'))
    host = decrypt(os.environ.get('host'))
    conn = f"Connecting to db: {database} on host:{host} with user:{username} and password:{password}"

    return {
        'statusCode': 200,
        'body': json.dumps(conn)
    }
