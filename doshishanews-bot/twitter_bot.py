import tweepy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

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
today = "{}-{}-{}".format(date.year, date.month, date.day)
the_day = "2018-11-13"

# Starts of Scraping Scripts

news_all_url = "https://www.doshisha.ac.jp/news/all/2018/1"

uClient = uReq(news_all_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

date_containers = soup.find("dl", {"class" : "newsList"}).findAll("dt")
title_containers = soup.find("dl", {"class" : "newsList"}).find_all("a", {"class" : "link01"})

date_list = []
title_list = []
url_list = []

for date_container in date_containers:
    date = date_container.span.text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
    date_list.append(date)

for title_container in title_containers:
    title = title_container.text
    title_list.append(title)

for title_container in title_containers:
    title_url = title_container["href"]
    url_list.append(title_url)
    # url_list.append(title_url)

# End of scraping Scripts


doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list})
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == today[2:]]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        Publish_Date = doshisha_news_today.iloc[[i]]['publish_date']
        Content_Title = doshisha_news_today.iloc[[i]]['title']
        Title_Url = doshisha_news_today.iloc[[i]]['url']

        msg = "{}\n{}\n https://www.doshisha.ac.jp{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        # print(msg.replace("['", "").replace("']", ""))
        api.update_status(msg.replace("['", "").replace("']", ""))
