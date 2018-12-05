# coding: utf-8
import os
import tweepy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

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
