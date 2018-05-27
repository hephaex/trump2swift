#!python3.6.x
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Twitter App access keys for @user
## Consume
COMSUMER_KEY = 'CRIsRvcTg3zvnNGGSN1lCAEvl'
COMSUMER_SECRET = 'KIGmWSM6lpCYQ2pobFOL5ici0MBXMQVERhmw0OshrrY9pMqUz6'
## Access
ACCESS_TOKEN = '2933051780-xDFiCL2PFdF6lHFcJbLWTX1ZP9t1VUNCvEhZczl'
ACCESS_SECRET = '1Fa0RJAkQnDvrBY4CdrdcRC9FsCa09XcMjb9wPIg7E9ib'

# This will allow us to use the keys as variables
#from credentials import *

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
#print(data.head(10))
#print("\n\n")
#print(dir(tweets[0]))

#print(tweets[0].id)
#print(tweets[0].created_at)
#print(tweets[0].source)
#print(tweets[0].favorite_count)
#print(tweets[0].retweet_count)
#print(tweets[0].geo)
#print(tweets[0].coordinates)
#print(tweets[0].entities)

data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])

print(data.head(10))

mean = np.mean(data['len'])
print("The Length's average in tweets: {}".format(mean))

like_max = np.max(data['Likes'])
rt_max = np.max(data['RTs'])

like = data[data.Likes == like_max].index[0]
rt = data[data.RTs == rt_max].index[0]

# Max FAVs:
print("The tweet with more likes is: \n{}".format(data['Tweets'][like]))
print("Number of likes: {}".format(like_max))
print("{} characters.\n".format(data['len'][like]))

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['Tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))

# We create time series for data:

tlen = pd.Series(data=data['len'].values, index=data['Date'])
tlike = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Lenghts along time:
tlen.plot(figsize=(16,4), color='r');

# Likes vs retweets visualization:
tlike.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True);

# We obtain all possible sources:
sources = []
for source in data['Source']:
    if source not in sources:
        sources.append(source)

# We print sources list:
print("Creation of content sources:")
for source in sources:
    print("* {}".format(source))

# We create a numpy vector mapped to labels:
percent = np.zeros(len(sources))

for source in data['Source']:
    for index in range(len(sources)):
        if source == sources[index]:
            percent[index] += 1
            pass

percent /= 100

# Pie chart:
pie_chart = pd.Series(percent, index=sources, name='Sources')
pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6));
