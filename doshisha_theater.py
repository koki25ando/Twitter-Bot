import os
import tweepy
import datetime
from datetime import date, timedelta
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

# Main url
theater_url = 'http://www.d-live.info/program/movie/index.php'

uClient = uReq(theater_url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

whole_listbox = soup.find_all("div", {"class" : "listbox"})
end_listbox = soup.find_all("div", {"class" : "listbox event_end"})

movie_title_list = []
movie_info_list = []
movie_link_list = []

for i in range(0, len(whole_listbox)-len(end_listbox)):
    movie_title = whole_listbox[i].h4.a.text
    movie_link = whole_listbox[i].h4.a["href"]
    movie_info = whole_listbox[i].findAll("p")
    movie_title_list.append(movie_title)
    movie_link_list.append(movie_link)
    movie_info_list.append(movie_info)

# doshisha_theater_news = pd.DataFrame({"Movie_Title" : movie_title_list, "Movie_link" : movie_link_list})
doshisha_theater_news = pd.DataFrame({"Movie_Title" : movie_title_list, "Movie_Info" : movie_info_list, "Movie_link" : movie_link_list})
# doshisha_theater_news['Movie_Info'] = str(doshisha_theater_news['Movie_Info'])
date = datetime.datetime.now()
today = "{}-{}-{}".format(date.year, date.month, "%02d" % date.day)
datetimeFormat = "%Y-%m-%d"

tweet_title_list = []
tweet_info_list = []
tweet_link_list = []
open_date_list = []
date_diff_list = []

for i in range(len(doshisha_theater_news)):
    tweet_title = doshisha_theater_news['Movie_Title'][i]
    tweet_info = str(doshisha_theater_news['Movie_Info'][i])
    tweet_link = doshisha_theater_news['Movie_link'][i]
    open_date = str(doshisha_theater_news['Movie_Info'][i]).split('開催年月日：')[1][0:10].replace("/", "-")
    tweet_title_list.append(tweet_title)
    tweet_info_list.append(tweet_info)
    tweet_link_list.append(tweet_link)
    open_date_list.append(open_date)
    date_diff = datetime.datetime.strptime(open_date_list[i], datetimeFormat) - datetime.datetime.strptime(today, datetimeFormat)
    date_diff_list.append(date_diff)

theater_news = pd.DataFrame({"Title" : tweet_title_list, "Info" : tweet_info_list, "Link" : tweet_link_list,
                             "Open_date" : open_date_list, "Date_diff" : date_diff_list})


for i in range(len(theater_news)):
    theater_news.iloc[i]

for i in range(len(theater_news)):
    if int(theater_news.iloc[i]['Date_diff'].__str__()[:7].replace("days", "").replace(" ","")) == 0:
        msg = "同志社大学映画上映情報: 本日上映！\n{}\n{}\n{}".format(
                                                      theater_news.iloc[i]['Title'],
                                                      theater_news.iloc[i]['Info'].replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""),
                                                      theater_news.iloc[i]['Link'].replace("../movie", "http://www.d-live.info/program/movie"))
        # print(msg)
        api.update_status(msg)
    elif int(theater_news.iloc[i]['Date_diff'].__str__()[:7].replace("days", "").replace(" ","")) <= 7:
        msg = "同志社大学映画上映情報: 開催間近！上映まで{}日！\n{}\n{}\n{}".format(theater_news.iloc[i]['Date_diff'].__str__()[:7].replace("days", "").replace(" ",""),
                                                      theater_news.iloc[i]['Title'],
                                                      theater_news.iloc[i]['Info'].replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""),
                                                      theater_news.iloc[i]['Link'].replace("../movie", "http://www.d-live.info/program/movie"))
        # print(msg)
        api.update_status(msg)
    else:
        msg = "同志社大学映画上映情報: 上映まで{}日\n{}\n{}\n{}".format(theater_news.iloc[i]['Date_diff'].__str__()[:7].replace("days", "").replace(" ",""),
                                                      theater_news.iloc[i]['Title'],
                                                      theater_news.iloc[i]['Info'].replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""),
                                                      theater_news.iloc[i]['Link'].replace("../movie", "http://www.d-live.info/program/movie"))
        # print(msg)
        api.update_status(msg)
