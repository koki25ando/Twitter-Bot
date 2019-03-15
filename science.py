# coding: utf-8
import os
import tweepy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

date = datetime.datetime.now()
today = "{}-{}-{}".format(date.year, date.month, date.day)
today_gc = "{}-{}-{}".format(date.year, date.month, "%02d" % date.day)
the_day = "2018-12-4"

## Fuculty of Biomedical

biomedic_url = "https://biomedical.doshisha.ac.jp/"


uClient = uReq(biomedic_url)
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
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == the_day[2:]]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        Publish_Date = doshisha_news_today.iloc[[i]]['publish_date']
        Content_Title = doshisha_news_today.iloc[[i]]['title']
        Title_Url = doshisha_news_today.iloc[[i]]['url']

        msg = "20{} [生命医科学部]\n{}\nhttps://www.doshisha.ac.jp{}".format(Publish_Date.values, Content_Title.values, Title_Url.values)
        print(msg.replace("['", "").replace("']", "").replace("3000", ""))
        # api.update_status(msg.replace("['", "").replace("']", "").replace("3000", ""))
