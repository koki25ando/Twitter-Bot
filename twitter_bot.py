import tweepy as tp
import time
import os

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, access_secret)
api = tp.API(auth)

os.chdir('')
for model_image in os.listdir('.'):
    api.update_with_media()
    time.sleep()
