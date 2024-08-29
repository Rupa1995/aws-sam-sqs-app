import logging
from datetime import datetime
import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def handler(event, context):
    no_of_msg = str(len(event['Records']))
    print("Found " +no_of_msg +" messages to process.")
    print(event['Records'])
    for rec in event['Records']:
        data = json.loads(rec['body'])
        print(data)
        table = dynamodb.Table('SqsLambdaMsg')
        response = table.put_item(
            Item={
            'messageId': rec['messageId'],
            'Name': data['Name'],
            'Msg': data['Msg'],
            'PhoneNo': data['PhoneNo'],
            'Timestamp': datetime.now().isoformat()
            }
        )
    print("Wrote message to DynamoDB:", json.dumps(response))