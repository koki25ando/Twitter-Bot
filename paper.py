# coding: utf-8
import os
import tweepy
import datetime
import pandas as pd

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

paper_info = pd.read_csv("paper_info_df.csv")
data_subject = paper_info.sort_values(by = ['author']).head(5)
for i in range(5):
    msg = "【学位論文紹介】{}\nタイトル: {} \n著者: {}\n発行年月日: {}\nURL: {}".format(data_subject.iloc[i, 0], data_subject.iloc[i, 1], data_subject.iloc[i, 2], data_subject.iloc[i, 3], data_subject.iloc[i, 5])
    api.update_status(msg)

paper_info.iloc[5:len(paper_info), :].to_csv("paper_info_df.csv")
