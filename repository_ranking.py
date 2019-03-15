# coding: utf-8
import os
import tweepy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

# @doshishauni_inf
appname = os.environ.get('DoshishaNews_Bot')
consumer_key = os.environ.get('doshisha_tb_consumer_key')
consumer_secret = os.environ.get('doshisha_tb_consumer_secret')
access_token = os.environ.get('doshisha_tb_access_token')
access_secret = os.environ.get('doshisha_tb_access_secret')

##### Twitter Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

date = datetime.datetime.now()
today = "{}{}{}".format(date.year, str(date.month).zfill(2), date.day)
url = "https://doors.doshisha.ac.jp/duar/repository/ir/ranking/?lang=0&kind=0&dayfrom={}&dayto=".format(today)


uClient = uReq(url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")
title = soup.find("table", {"class": "tstyle wi100P"}).findAll("tr")
# print(title[1].a.text)
# print(title[2].a.text)
# print(title[3].a.text)

# print(title[1].a['href'].replace('../', 'https://doors.doshisha.ac.jp/duar/repository/ir/'))
# print(title[2].a['href'].replace('../', 'https://doors.doshisha.ac.jp/duar/repository/ir/'))
# print(title[3].a['href'].replace('../', 'https://doors.doshisha.ac.jp/duar/repository/ir/'))

access = soup.find("table", {"class": "tstyle wi100P"}).findAll("td", {"style": "text-align:right;vertical-align:middle;"})
# print(access[1].text.strip())
# print(access[3].text.strip())
# print(access[5].text.strip())

for i in range(1,4):
    msg = "{}-{}-{}\n【本日の学術リポジトリアクセスランキング】\nNo.{} {}アクセス\nタイトル: {}\nURL: {}".format(date.year, date.month, date.day, i, access[i*2-1].text.strip(), title[i].a.text, title[i].a['href'].replace('../', 'https://doors.doshisha.ac.jp/duar/repository/ir/'))
    api.update_status(msg)
