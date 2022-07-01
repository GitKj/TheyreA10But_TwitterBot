import tweepy
import os
import config

def get_Twitter_Client():
    return tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"), consumer_secret=os.getenv("TWITTER_SECRET_KEY"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"), access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )

def get_temp_client():
    return tweepy.Client(
        consumer_key=config.TWITTER_API_KEY, consumer_secret=config.TWITTER_API_SECRET_KEY,
        access_token=config.TWITTER_ACCESS_TOKEN, access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET
    )