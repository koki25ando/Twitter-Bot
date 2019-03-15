# coding: utf-8
import os
import tweepy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

# @doshishauni_inf
appname = 'DoshishaNews_Bot'
consumer_key = os.environ.get('doshisha_tb_consumer_key')
consumer_secret = os.environ.get('doshisha_tb_consumer_secret')
access_token = os.environ.get('doshisha_tb_access_token')
access_secret = os.environ.get('doshisha_tb_access_secret')

##### Twitter Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

date = datetime.datetime.now()
today = "{}-{}-{}".format(date.year, date.month, date.day)
gc_today = "{}-{}-{}".format(date.year, date.month, "%02d" % date.day)
the_day = "2018-11-21"

todays_event_url = "https://www.doshisha.ac.jp/event/?year={}&month={}&day={}".format(date.year, "%02d" % date.month, "%02d" % date.day)


uClient = uReq(todays_event_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")


date_list = []
place_list = []
content_list = []
link_list = []

title_container = soup.find("dl", {"class" : "newsList"}).findAll("dt")
content_container = soup.find("dl", {"class" : "newsList"}).findAll("dd")
for i in range(len(title_container)):
    date = title_container[i].strong.text
    place = title_container[i]["class"]
    content = content_container[i].text
    link = content_container[i].p.a["href"]
    date_list.append(date)
    place_list.append(place)
    content_list.append(content)
    link_list.append(link)

event_df = pd.DataFrame({
        "Date" : date_list,
        "Place" : place_list,
        "Content" : content_list,
        "Link" : link_list
    })

for i in range(len(event_df)):
    tweet_date = event_df.iloc[i]['Date'].replace("開催", "")
    tweet_place = event_df.iloc[i]['Place']
    tweet_content = event_df.iloc[i]['Content']
    tweet_link = event_df.iloc[i]['Link']
    msg = "【本日開催のイベント】\n開催時期:{}\n{}\nhttps://www.doshisha.ac.jp{}".format(
          tweet_date, tweet_content.replace("\n", ""), tweet_link)
    # print(msg)
    api.update_status(msg)
