# import packages
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd

# Setting of main links

news_url = "https://www.doshisha.ac.jp/news/research/"
event_url = "https://www.doshisha.ac.jp/event/?postpage_id=research"
academic_repository = "https://doors.doshisha.ac.jp/duar/repository/ir/?lang=0"

news_url = "https://www.doshisha.ac.jp/news/all/"
main_url = "https://www.doshisha.ac.jp/"

# Data scraping part
## Topics "https://www.doshisha.ac.jp/news/research_topics/"
topics_url = "https://www.doshisha.ac.jp/news/research_topics/"

uClient = uReq(topics_url)
topics_html = uClient.read()
uClient.close()
soup = BeautifulSoup(topics_html, "html.parser")

### Data we are going to take
### date, topics, titles and title_links
file_name1 = "topics_date.csv"
f = open(file_name1, "w")
header1 = "Date\n"
f.write(header1)

content_dates = soup.findAll("dt", {"class" : "icon_topics"})
for date in content_dates:
    publish_date = date.text.replace("'", "20").replace("年", "-").replace("月", "-").replace("日", "")
    f.write(publish_date + "\n")

f.close()

file_name2 = "topics_title_link.csv"
f = open(file_name2, "w")
header2 = "Title, Link\n"
f.write(header2)

content_titles = soup.find_all("dd")
for title in content_titles:
    content_title = title.text.replace("\n", "")
    title_link = title.p.a["href"]
    f.write(content_title.replace(",", "|") + "," + title_link + "\n")

f.close()
