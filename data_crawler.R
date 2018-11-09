# Package preparatinon
library(tidyverse)
library(rvest)
setwd("/Users/KokiAndo/Desktop/Python/Doshisha")


news_url = "https://www.doshisha.ac.jp/news/all/"
important = "https://www.doshisha.ac.jp/news/important/2018/1"

## Data Scraping Part
## Press data

press_url = "https://www.doshisha.ac.jp/news/info/2018/1"
press_page <- read_html(press_url)
test <- press_page %>% 
  html_nodes("dl.newsList") %>% 
  html_nodes("span") %>% 
  html_text() %>% 
  str_remove("'")

print(test, locale = locale(encoding = "SHIFT-JIS"))

press_link <- press_page %>% 
  html_nodes("dl.newsList") %>% 
  html_nodes("dd") %>% 
  html_nodes("a") %>% 
  html_attr("href")
