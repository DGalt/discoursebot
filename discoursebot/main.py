#!/usr/bin/env python

#import pdb; pdb.set_trace()

import time, urllib, locale, os
#import simplejson as json
import json
from datetime import date, datetime, timedelta
from config import config
import requests
import tweepy

# -----------------------------------------
# Kevin giving up and trying TWEEPY instead
# -----------------------------------------

consumer_key=config['consumer_key']
consumer_secret=config['consumer_secret']
access_token=config['access_token_key']
access_token_secret=config['access_token_secret']
user = '@Discourse_Bot'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
since_id = 0
tweets_to_respond = ""

def load_tweets_to_respond():
    tweets_to_respond = api.search(q = user)
    return tweets_to_respond

def respond_to_tweets():
    tweets_to_respond = load_tweets_to_respond()
    for result in tweets_to_respond:
	    response_tweet = "@" + result.author.screen_name + " this is an automated response to all my haters"
	    print(response_tweet)
    return

respond_to_tweets()
#print(api.search(q = user))

# docs : http://tweepy.readthedocs.org/en/v3.5.0/api.html?highlight=update_status#API.search
#print(parsed_tweets_to_respond)
#print(type(tweets_to_respond))

	#print(result.__getstate__())
	#print(result.id_str)
	#print("-----")
	#print(result.entities.user_mentions.id_str)
	#print(result.author.id_str)
	#print(result.author.screen_name)
	#print("-----")
	#print(result.text)
	#print("=====TWEET BELOW========")
	
	#api.update_status(response_tweet,result.id_str)
	#print(response_tweet)
	#print("========================")



#tweets_to_respond.__dict__
#tweets_to_respond.__dir__
#print(tweets_to_respond.text.encode("ascii",errors="replace").decode("utf8"))

# --------------------------------------------------------------
# main body
# --------------------------------------------------------------
# check_mentions()

#print("Hello World")
# if check_mentions() == "true":
#    print("I saw your Tweet, thanks!!")

#api = twitter.Api(consumer_key=config['consumer_key'], consumer_secret=config['consumer_secret'], access_token_key=config['access_token_key'], access_token_secret=config['access_token_secret'])
#api = twitter.Api(consumer_key='1', consumer_secret='2', access_token_key='3', access_token_secret='4')
#print(api.VerifyCredentials())
"""tweets_to_respond = [["@therebutforthe9" , 701246615387037697], ["@therebutforthe9", 701289857180688384]]

api = twitter.Api(consumer_key=config['consumer_key'],
                    consumer_secret=config['consumer_secret'],
                    access_token_key=config['access_token_key'],
                    access_token_secret=config['access_token_secret'])


stream = api.GetStreamFilter(follow=user)"""

#for x in range(0,2):
 #   	api.PostUpdate("%s this is an attempt to reply to multiple from a for loop python file to tweet" % (tweets_to_respond[x][0]),in_reply_to_status_id=(tweets_to_respond[x][1]))
        