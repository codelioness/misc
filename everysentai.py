#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random, urllib

from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '927a73bea29d0c478d00407f12b04d881d74701bb4d7ef3f6'
client = swagger.ApiClient(apiKey, apiUrl)
wordsApi = WordsApi.WordsApi(client)

CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_KEY =  'x'
ACCESS_SECRET = 'x'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
first = wordsApi.getRandomWord(hasDictionaryDef = True, minLength = 3, minDictionaryCount = 2).word
first = first[0].capitalize() + first[1:]

second = wordsApi.getRandomWord(hasDictionaryDef = True, minLength = 3, minDictionaryCount = 2).word
second = second[0].capitalize() + second[1:]

num = random.randint(1,50);
end = ''
if num <= 22:
	end = 'ranger'
elif num <= 33:
	end = 'ger'
elif num <= 44:
	end = 'man'
elif num == 46:
	end = second+'V'
elif num == 48:
	end = ' Vulcan'
else:
	end = ' J'
ranger = first + ' Sentai ' + second + end
 
# print ranger # for testing
api.update_status(ranger)