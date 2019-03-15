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
the_day = "2018-1-29"

commerce_url = "https://com.doshisha.ac.jp/news/news/"
economics_url = "https://www.econ.doshisha.ac.jp/news/topics/"
letter_url = "https://letters.doshisha.ac.jp/"
gc_url = "https://globalcommunications.doshisha.ac.jp/news"
gr_url = "https://gr.doshisha.ac.jp/"
biomedic_url = "https://biomedical.doshisha.ac.jp/"

faculty_link_list = [commerce_url, economics_url, letter_url, gc_url, gr_url, biomedic_url]



for i in range(len(faculty_link_list)):

    url = faculty_link_list[i]
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    soup = BeautifulSoup(page_html, "html.parser")

    if url == faculty_link_list[0] or url == faculty_link_list[1]:
        date_containers = soup.find("dl", {"class" : "newsList2 clearfix"}).findAll("dt")
        title_containers = soup.find("dl", {"class" : "newsList2 clearfix"}).find_all("a", {"class" : "link01"})
    elif url == faculty_link_list[2] or url == faculty_link_list[5]:
        date_containers = soup.find("dl", {"class" : "tab1 newsList"}).findAll("dt")
        title_containers = soup.find("dl", {"class" : "tab1 newsList"}).find_all("a", {"class" : "link01"})
    elif url == faculty_link_list[3]:
        date_containers = soup.findAll("p", {"class" : "date"})
        title_containers = soup.findAll("p", {"class" : "txt"})
    elif url == faculty_link_list[4]:
        date_containers = soup.find("dl", {"class" : "newsList2"}).findAll("dt")
        title_containers = soup.find("dl", {"class" : "newsList2"}).find_all("a", {"class" : "link01"})
    else:
        pass

    date_list = []
    title_list = []
    url_list = []

    if url == faculty_link_list[3]:
        for title_container in title_containers:
            title = title_container.text
            title_list.append(title)
            title_url = title_container.a["href"]
            url_list.append(title_url)
    else:
        for title_container in title_containers:
            title = title_container.text
            title_list.append(title)
            title_url = title_container["href"]
            url_list.append(title_url)

    if url == faculty_link_list[0] or url == faculty_link_list[1] or url == faculty_link_list[2] or url == faculty_link_list[5]:
        for date_container in date_containers:
            date = date_container.span.text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
            date_list.append(date)

    elif url == faculty_link_list[3]:
        for i in range(len(date_containers)):
            date = date_containers[i].text.replace(".", "-")
            date_list.append(date)

    elif url == faculty_link_list[4]:
        for i in range(len(date_containers)):
            date = date_containers[i].text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
            date_list.append(date)

    else:
        pass

    if url == faculty_link_list[0]:
        doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list, "Faculty" : "商"})
    elif url == faculty_link_list[1]:
        doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list, "Faculty" : "経済"})
    elif url == faculty_link_list[2]:
        doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list, "Faculty" : "文"})
    elif url == faculty_link_list[3]:
        doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list, "Faculty" : "グローバルコミュニケーション"})
    elif url == faculty_link_list[4]:
        doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list, "Faculty" : "グローバル地域文化"})
    elif url == faculty_link_list[5]:
        doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list, "Faculty" : "生命医科"})
    else:
        pass

    if url == faculty_link_list[3]:
        doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == gc_today]
        for i in range(len(doshisha_news_today)):
            msg = "{}【{}学部】\n{}\n{}".format(
                  doshisha_news_today.iloc[i]['publish_date'],
                  doshisha_news_today.iloc[i]['Faculty'],
                  doshisha_news_today.iloc[i]['title'],
                  doshisha_news_today.iloc[i]['url'])
            # print(msg)
            api.update_status(msg)
    else:
        doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == the_day[2:]]
        for i in range(len(doshisha_news_today)):
            msg = "20{}【{}学部】\n{}\nhttps://www.doshisha.ac.jp{}".format(
                  doshisha_news_today.iloc[i]['publish_date'],
                  doshisha_news_today.iloc[i]['Faculty'],
                  doshisha_news_today.iloc[i]['title'],
                  doshisha_news_today.iloc[i]['url'])
            # print(msg)
            api.update_status(msg)
