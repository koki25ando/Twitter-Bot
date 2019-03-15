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
the_day = ""

com_url = "https://com.doshisha.ac.jp/news/news/"
econ_url = "https://www.econ.doshisha.ac.jp/news/topics/"
gc_url = "https://globalcommunications.doshisha.ac.jp/news"
gr_url = "https://gr.doshisha.ac.jp/news/news/"
biomedic_url = "https://biomedical.doshisha.ac.jp/"

def read_to_soup(url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    soup = BeautifulSoup(page_html, "html.parser")
    return soup

econ = read_to_soup(econ_url)

 = econ.find("dl", {"class" : "newsList"}).findAll("dt")
