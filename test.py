import datetime
import pandas as pd

date = datetime.datetime.now()
today = "{}-{}-{}".format(date.year, date.month, date.day)
day = '2018-11-08'
the_other_day = '2018-08-22'

doshisha_news = pd.read_csv("/Users/KokiAndo/Desktop/Python/Doshisha/Data/Doshisha_news.csv")
doshisha_news_today = doshisha_news[doshisha_news['publish_date'] == the_other_day]

if len(doshisha_news_today) is 0:
    pass
else:
    for i in range(0, len(doshisha_news_today)):
        publish_date = doshisha_news_today.iloc[[i]]['publish_date']
        news_type = doshisha_news_today.iloc[[i]]['type']
        title = doshisha_news_today.iloc[[i]]['content_title']
        title_url = doshisha_news_today.iloc[[i]]['content_url']

        msg = "{}:{}\n{}\n{}".format(publish_date.values, news_type.values, title.values, title_url.values)
        print(msg.replace("['", "").replace("']", ""))
