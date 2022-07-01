import tweepy
import os

def get_Twitter_Client():
    return tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"), consumer_secret=os.getenv("TWITTER_SECRET_KEY"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"), access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )