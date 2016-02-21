#!/usr/bin/env python

import time, urllib, locale, twitter, os
import simplejson as json
from datetime import date, datetime, timedelta
from config import config

# check for mentions of Discourse_Bot that should be replied to
"""def check_mentions():
	api = twitter.api(consumer_key=config['consumer_key'],
	            		consumer_secret=config['consumer_secret'],
	                    access_token_key=config['access_token_key'],
	                    access_token_secret=config['access_token_secret'])

	return "true"



# Get text and post it to Twitter
def postReply(text):
	api = twitter.api(consumer_key=config['consumer_key'],
	            		consumer_secret=config['consumer_secret'],
	                    access_token_key=config['access_token_key'],
	                    access_token_secret=config['access_token_secret'])

	status = api.PostUpdate(text)


# Test connection to twitter api
def test_api():
	api = twitter.api(consumer_key=config['consumer_key'],
            		consumer_secret=config['consumer_secret'],
                    access_token_key=config['access_token_key'],
                    access_token_secret=config['access_token_secret'])

	print(api.VerifyCredentials())
"""
# --------------------------------------------------------------
# main body
# --------------------------------------------------------------

#print("Hello World")
# if check_mentions() == "true":
#	print("I saw your Tweet, thanks!!")

api = twitter.Api(consumer_key=config['consumer_key'], consumer_secret=config['consumer_secret'], access_token_key=config['access_token_key'], access_token_secret=config['access_token_secret'])
#api = twitter.Api(consumer_key='1', consumer_secret='2', access_token_key='3', access_token_secret='4')
print(api.VerifyCredentials())
#api.PostUpdate("This is the discourse_bots first tweet from a python file")