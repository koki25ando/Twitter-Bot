import tweepy
import datetime
from datetime import date, timedelta
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

# @doshishauni_inf
appname = 'DoshishaNews_Bot'
consumer_key = 'MVvmXgcswDTez6n4SRB89oWUT'
consumer_secret = 'YdMUBRowq55WqwgqGStK5GjXU0sFJ4yjEuM6o4u1eYJin6NoN9'
access_token = '1060894340912795648-UH8qqX3cWE3zgUF7rR8cP6CL5hZFeJ'
access_secret = 'dEjiDGDQ0QzDaqzmmrqeud9b6BhTQ6d64vzVMVdtM0j0J'

##### Twitter Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


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
today = "{}-{}-{}".format(date.year, date.month, date.day)
datetimeFormat = "%Y-%m-%d"

for i in range(0, len(doshisha_theater_news)):
    tweet_title = doshisha_theater_news['Movie_Title'][i]
    tweet_info = str(doshisha_theater_news['Movie_Info'][i])
    tweet_link = doshisha_theater_news['Movie_link'][i]
    open_date = tweet_info.split('開催年月日：')[1][0:10].replace("/", "-")


    diff = datetime.datetime.strptime(open_date, datetimeFormat) - datetime.datetime.strptime(today, datetimeFormat)
    days_left = int(diff.__str__()[0:2])

    if open_date == today:
        msg = "同志社大学映画上映情報: 本日上映！\n{}\n{}\n{}".format(tweet_title,
                                                      tweet_info,
                                                      tweet_link.replace("../movie", "http://www.d-live.info/program/movie"))
        # print(msg.replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""))
        api.update_status(msg.replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""))
    elif days_left >= 7:
        msg = "同志社大学映画上映情報: 開催間近！上映まで{}日！\n{}\n{}\n{}".format(days_left, tweet_title,
                                                                            tweet_info,
                                                                            tweet_link.replace("../movie", "http://www.d-live.info/program/movie"))
        # print(msg.replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""))
        api.update_status(msg.replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""))
    else:
        msg = "同志社大学映画上映情報: 上映まで{}日 \n{}\n{}\n{}".format(days_left, tweet_title,
                                                                    tweet_info,
                                                                    tweet_link.replace("../movie", "http://www.d-live.info/program/movie"))
        # print(msg.replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""))
        api.update_status(msg.replace("</p>, <p>", "\n").replace("[<p>", "").replace("</p>]", ""))
