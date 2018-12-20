import json
import os
import boto3
import twitter
from boto3.dynamodb.conditions import Key
from slackclient import SlackClient

# super secrets
BOT_TOKEN = os.environ['BOT_TOKEN']
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET_TOKEN = os.environ['TWITTER_ACCESS_SECRET_TOKEN']

# dynamo table stuff
TWEET_TRACKING_TABLE = os.environ['TWEET_TRACKING_TABLE']

# twitter api object
api = twitter.Api(consumer_key="{}".format(TWITTER_CONSUMER_KEY),
    consumer_secret="{}".format(TWITTER_CONSUMER_SECRET),
    access_token_key="{}".format(TWITTER_ACCESS_TOKEN),
    access_token_secret="{}".format(TWITTER_ACCESS_SECRET_TOKEN)
)
def receive(event, context):
    print("Got data: {}".format(event))
    print(api.VerifyCredentials())