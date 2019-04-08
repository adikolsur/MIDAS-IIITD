# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:50:08 2019

@author: adiko
"""

import tweepy
import jsonlines
import pandas as pd

consumer_key = "EPpD21VPkhxzz7lvv2K7M1rUL"
consumer_secret = "5KB6BXznGDnlC4nzsF8gb4T4r6x0xMcgpIo2J4ECuI6ZczRzeQ"
access_token = "1114884355711746054-Fz4BdRWnQjR8x4Rf8DzAOr6Wkl90ru"
access_token_secret = "IWmC1JWUAhsMu6LGPpkpffphmuwcVv9FVlQfAvghoGuin"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# The Twitter user who we want to get tweets from
name = "midasIIITD"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

with jsonlines.open("results.jsonl",mode='w') as writer:
    for tweet in results:
        writer.write(tweet._json)

answer=[]

with jsonlines.open("results.jsonl",mode='r') as reader:
    for item in reader.iter():
        temp=[]
        temp.append(item['text'])
        temp.append(item['created_at'][:16])
        temp.append(item['favorite_count'])
        temp.append(item['retweet_count'])
        answer.append(temp)
        
df=pd.DataFrame(answer,columns=['text','data','likes','retweets'])
