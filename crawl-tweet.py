#!python3.6.x
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Twitter App access keys for @user
## Consume
COMSUMER_KEY = ''
COMSUMER_SECRET = ''
## Access
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

# API setup
def twitter_setup():
    """
    Twitter's API with access keys.
    """
    # Authentication & Access keys
    auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Atuthentication Return
    api = tweepy.API(auth)
    return api

extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()
