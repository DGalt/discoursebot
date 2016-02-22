#!/usr/bin/env python

import time, urllib, locale, os
import simplejson as json
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

#print(api.search(q = user))
tweets_to_respond = api.search(q = user)
for x in tweets_to_respond:
	print(x)

target_user = "@therebutforthe9"
target_status = 701246615387037697

#api.update_status("%s this is an attempt to reply from tweepy" % target_user,in_reply_to_status_id=target_status)
#print(api.verify_credentials())

# ----------------------------------------------------------------
# END TWEEPY
# ----------------------------------------------------------------

# check for mentions of Discourse_Bot that should be replied to
#def check_mentions():
"""api = twitter.Api(consumer_key=config['consumer_key'],
                    consumer_secret=config['consumer_secret'],
                    access_token_key=config['access_token_key'],
                    access_token_secret=config['access_token_secret'])
"""
#print(api.GetStreamFilter(follow=user))

#statuses = api.GetStreamFilter(follow=user)
#tweets = [s.text for s in statuses]
#tweetobj = api.GetStreamFilter(follow=user)
#tweetobj_str = tweetobj.readall().decode('utf-8')

#from simplejson.compat import StringIO
#io = StringIO(api.GetStreamFilter(follow=user))
#json.load(io)[0] == api.GetStreamFilter(follow=user)
#_dict = json.loads(api.GetStreamFilter(follow=user))
#api.VerifyCredentials()
#for x in api.GetStreamFilter(follow=user):
#    print(x)
#print(r.text)

#for found_tweet in r.text:
#	print(found_tweet)

"""
# Get text and post it to Twitter
def postReply(text, reply_target):
    api = twitter.Api(consumer_key=config['consumer_key'],
                        consumer_secret=config['consumer_secret'],
                        access_token_key=config['access_token_key'],
                        access_token_secret=config['access_token_secret'])

    status = Api.PostUpdate(text, in_reply_to_status_id = 0x00000153CA4A6938)



"""
# Test connection to twitter api
"""
def test_api():
    api = twitter.Api(consumer_key=config['consumer_key'],
                    consumer_secret=config['consumer_secret'],
                    access_token_key=config['access_token_key'],
                    access_token_secret=config['access_token_secret'])

    print(api.VerifyCredentials())
"""
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
        