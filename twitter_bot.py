import tweepy
import datetime
import pandas as pd

# @doshishauni_inf
appname = 'DoshishaNews_Bot'
consumer_key = 'MVvmXgcswDTez6n4SRB89oWUT'
consumer_secret = 'YdMUBRowq55WqwgqGStK5GjXU0sFJ4yjEuM6o4u1eYJin6NoN9'
access_token = '1060894340912795648-UH8qqX3cWE3zgUF7rR8cP6CL5hZFeJ'
access_secret = 'dEjiDGDQ0QzDaqzmmrqeud9b6BhTQ6d64vzVMVdtM0j0J'

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
today = "{}年{}月{}日".format(date.year, date.month, date.day)

doshisha_news = pd.read_csv("/Users/KokiAndo/Desktop/Python/Doshisha/Data/Doshisha_news.csv")
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == today]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        publish_date = doshisha_news_today.iloc[[i]]['publish_date']
        news_type = doshisha_news_today.iloc[[i]]['type']
        title = doshisha_news_today.iloc[[i]]['content_title']
        title_url = doshisha_news_today.iloc[[i]]['content_url']

        msg = "{}:{}\n{}\n{}".format(publish_date.values, news_type.values, title.values, title_url.values)
        # print(msg.replace("['", "").replace("']", ""))
        api.update_status(msg.replace("['", "").replace("']", ""))
