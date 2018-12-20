import json
import os
import boto3
from boto3.dynamodb.conditions import Key
from slackclient import SlackClient

def receive(event, context):
    data = json.loads(event['body'])
    print("Got data: {}".format(data))