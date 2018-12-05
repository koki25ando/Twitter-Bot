# coding: utf-8
import os
import tweepy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

appname = os.environ.get('DoshishaNews_Bot')
consumer_key = os.environ.get('doshisha_tb_consumer_key')
consumer_secret = os.environ.get('doshisha_tb_consumer_secret')
access_token = os.environ.get('doshisha_tb_access_token')
access_secret = os.environ.get('doshisha_tb_access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

date = datetime.datetime.now()
today = "{}-{}-{}".format(date.year, date.month, date.day)
today_gc = "{}-{}-{}".format(date.year, date.month, "%02d" % date.day)
the_day = "2018-11-21"

commerce_url = "https://com.doshisha.ac.jp/news/news/"
economics_url = "https://www.econ.doshisha.ac.jp/news/topics/"
letter_url = "https://letters.doshisha.ac.jp/"
gc_url = "https://globalcommunications.doshisha.ac.jp/news"
gr_url = "https://gr.doshisha.ac.jp/"


#-- Faculty of commerce

uClient = uReq(commerce_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

date_containers = soup.find("dl", {"class" : "newsList2 clearfix"}).findAll("dt")
title_containers = soup.find("dl", {"class" : "newsList2 clearfix"}).find_all("a", {"class" : "link01"})

date_list = []
title_list = []
url_list = []

for date_container in date_containers:
    date = date_container.span.text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
    date_list.append(date)

for title_container in title_containers:
    title = title_container.text
    title_list.append(title)
    title_url = title_container["href"]
    url_list.append(title_url)



doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list})
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == today[2:]]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        Publish_Date = doshisha_news_today.iloc[[i]]['publish_date']
        Content_Title = doshisha_news_today.iloc[[i]]['title']
        Title_Url = doshisha_news_today.iloc[[i]]['url']

        msg = "20{} [商学部]\n{}\nhttps://www.doshisha.ac.jp{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        # print(msg.replace("['", "").replace("']", "").replace("3000", ""))
        api.update_status(msg.replace("['", "").replace("']", "").replace("3000", ""))


#------ Faculty of economics -----

uClient = uReq(economics_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

date_containers = soup.find("dl", {"class" : "newsList2 clearfix"}).findAll("dt")
title_containers = soup.find("dl", {"class" : "newsList2 clearfix"}).find_all("a", {"class" : "link01"})

date_list = []
title_list = []
url_list = []

for date_container in date_containers:
    date = date_container.span.text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
    date_list.append(date)

for title_container in title_containers:
    title = title_container.text
    title_list.append(title)
    title_url = title_container["href"]
    url_list.append(title_url)



doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list})
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == today[2:]]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        Publish_Date = doshisha_news_today.iloc[[i]]['publish_date']
        Content_Title = doshisha_news_today.iloc[[i]]['title']
        Title_Url = doshisha_news_today.iloc[[i]]['url']

        msg = "20{} [経済学部]\n{}\nhttps://www.doshisha.ac.jp{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        # print(msg.replace("['", "").replace("']", "").replace("3000", ""))
        api.update_status(msg.replace("['", "").replace("']", "").replace("3000", ""))

#---- Faaculty of letters

uClient = uReq(letter_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

date_containers = soup.find("dl", {"class" : "tab1 newsList"}).findAll("dt")
title_containers = soup.find("dl", {"class" : "tab1 newsList"}).find_all("a", {"class" : "link01"})

date_list = []
title_list = []
url_list = []

for date_container in date_containers:
    date = date_container.span.text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
    date_list.append(date)

for title_container in title_containers:
    title = title_container.text
    title_list.append(title)
    title_url = title_container["href"]
    url_list.append(title_url)



doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list})
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == today[2:]]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        Publish_Date = doshisha_news_today.iloc[[i]]['publish_date']
        Content_Title = doshisha_news_today.iloc[[i]]['title']
        Title_Url = doshisha_news_today.iloc[[i]]['url']

        msg = "20{} [文学部]\n{}\nhttps://www.doshisha.ac.jp{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        # print(msg.replace("['", "").replace("']", "").replace("3000", ""))
        api.update_status(msg.replace("['", "").replace("']", "").replace("3000", ""))


#---- Faculty of Global Communications

uClient = uReq(gc_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")


date_containers = soup.findAll("p", {"class" : "date"})
title_containers = soup.findAll("p", {"class" : "txt"})

date_list = []
title_list = []
url_list = []

for i in range(len(date_containers)):
    date = date_containers[i].text.replace(".", "-")
    date_list.append(date)

for title_container in title_containers:
    title = title_container.text
    title_list.append(title)
    title_url = title_container.a["href"]
    url_list.append(title_url)


doshisha_news = pd.DataFrame({"publish_date" : date_list, "title" : title_list, "url" : url_list})
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == today_gc]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        Publish_Date = doshisha_news_today.iloc[[i]]['publish_date']
        Content_Title = doshisha_news_today.iloc[[i]]['title']
        Title_Url = doshisha_news_today.iloc[[i]]['url']

        msg = "{} [グローバルコミュニケーション学部]\n{}\n{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        # print(msg.replace("['", "").replace("']", "").replace("3000", ""))
        api.update_status(msg.replace("['", "").replace("']", "").replace("3000", ""))


#---- Faculty of Global and Regional Studies


uClient = uReq(gr_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

date_containers = soup.find("dl", {"class" : "newsList2"}).findAll("dt")
title_containers = soup.find("dl", {"class" : "newsList2"}).find_all("a", {"class" : "link01"})

date_list = []
title_list = []
url_list = []

for i in range(len(date_containers)):
    date = date_containers[i].text.replace("'", "").replace("年", "-").replace("月", "-").replace("日", "")
    date_list.append(date)

for title_container in title_containers:
    title = title_container.text
    title_list.append(title)
    title_url = title_container["href"]
    url_list.append(title_url)


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

        msg = "20{} [グローバル地域文化学部]\n{}\nhttps://www.doshisha.ac.jp{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        # print(msg.replace("['", "").replace("']", "").replace("3000", ""))
        api.update_status(msg.replace("['", "").replace("']", "").replace("3000", ""))
