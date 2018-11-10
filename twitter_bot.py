import tweepy
import datetime
import pandas as pd

# @ko25and
appname = "koki25ando"
consumer_key = 'MWoMFMiEyA0MrigZFL1ysDShc'
consumer_secret = 'ZEiofsto5uGOA4SAhrEQ1E5yJDOFkaAuHVqrALX8o7Jlxy8u89'
access_token = '2183834275-ACgyhcjpMjKKz0F8DpzdVl3PNXGuUy7XhVwUBEe'
access_secret = 'IPLnlh6m6py3lA1IeOLl5fvIHOlqr2yG7hpCgOHCRVgRe'

# @doshishauni_inf
'''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
'''

# login to twitter account api
'''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print("Access:", auth.get_authorization_url())
verifier = input('Verifier:')
auth.get_access_token(verifier)
print("Access Token:", auth.access_token)
print("Access Token Secret:", auth.access_token_secret)
'''
##### Twitter Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# Tweet content
date = datetime.datetime.now()
today = "{}-{}-{}".format(date.year, date.month, date.day)
day = '2018-11-08'
the_other_day = '2018-08-22'

doshisha_news = pd.read_csv("/Users/KokiAndo/Desktop/Python/Doshisha/Data/Doshisha_news.csv")
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == the_other_day]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        publish_date = doshisha_news_today.iloc[[i]]['publish_date']
        news_type = doshisha_news_today.iloc[[i]]['type']
        title = doshisha_news_today.iloc[[i]]['content_title']
        title_url = doshisha_news_today.iloc[[i]]['content_url']

        msg = "{}:{}\n{}\n{}".format(publish_date.values, news_type.values, title.values, title_url.values)
        print(msg.replace("['", "").replace("']", ""))



# post text
api.update_status('game is tied')
