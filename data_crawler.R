# Package preparatinon
library(tidyverse)
library(rvest)
# Sys.setlocale("LC_TIME", "de_DE")

Doshisha_Data_Scraping <- function (url) {
  # Requesting connection
  page <- read_html(as.character(url))
  
  # Date data
  publish_date <- page %>% 
    html_nodes("dt") %>% 
    html_nodes("span") %>% 
    html_text() %>% 
    str_replace("'", "20")
  
  # Title data
  content_title <- page %>% 
    html_nodes("dd") %>% 
    html_nodes("a") %>% 
    html_text()
  
  # Title url data
  tail_url <- page %>% 
    html_nodes("dd") %>% 
    html_nodes("a") %>% 
    html_attr("href")
  content_url <- paste0("https://www.doshisha.ac.jp", tail_url)
  
  type = url %>% 
    str_remove("https://www.doshisha.ac.jp/news/") %>% 
    str_remove("/2018/1")
  # Merging data
  data.frame(publish_date, content_title, content_url, type)
}

## Execute functions Doshisha_Data_Scraping()
important = "https://www.doshisha.ac.jp/news/important/2018/1"
press_url = "https://www.doshisha.ac.jp/news/press/2018/1"
topic_url = "https://www.doshisha.ac.jp/news/topics/2018/1"
info_url = "https://www.doshisha.ac.jp/news/info/2018/1"


news_important <- Doshisha_Data_Scraping(important)
news_press <- Doshisha_Data_Scraping(press_url)
news_topic <- Doshisha_Data_Scraping(topic_url)
news_info <- Doshisha_Data_Scraping(info_url)


# Merge datasets
# Doshisha.News.df <- bind_rows(news_important, news_info, news_topic, news_press, .id = "id")
Doshisha.News.df <- rbind(news_important, news_info, news_topic, news_press)

# Cleaning dataset
# Doshisha.News.df$publish_date <- Doshisha.News.df$publish_date %>% 
#  str_replace("???", "-") %>% 
#  str_replace("???", "-") %>% 
#  str_remove("???")
# Doshisha.News.df$publish_date <- as.Date(Doshisha.News.df$publish_date)

# Exporting dataset
write.csv(Doshisha.News.df, "/Users/KokiAndo/Desktop/Python/Doshisha/Data/Doshisha_news.csv")
