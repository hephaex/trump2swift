#!python3.6.x
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Twitter App access keys for @user
# edit credentials.py for @user consums & secretes
# This will allow us to use the keys as variables
from credentials import *

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

# Pandas Dataframe
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns = ['Tweets'])
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])

print(data.head(10))
