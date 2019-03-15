# Blueprint
+ daily tweet bot
+ tweets are about news, topics and events that are related to Doshisha university

# User Information
Twitter Link: https://twitter.com/doshishauni_inf
Username: Doshisha_Info/同志社ニュース-bot
id: @doshishauni_inf
password: *********
e-mail: doshishauniv.info@gmail.com

introduction:
    同志社大学の公式情報をお届けする、非公式アカウントです。
    不具合などがあればDMでご連絡下さい。

## Task Schedule Management
crontab -e
00 18 * * 1-6 /usr/local/bin/python "/Users/KokiAndo/Desktop/Python/Doshisha/twitter_bot.py"

## Running Python Script on heroku server
reference: https://qiita.com/noexpect/items/896c583945c2eec16093
App name: DoshishaNews_Bot


## Update Plans
+ Doshisha events alert(https://liaison.doshisha.ac.jp/events/event/calendar.html)
+ !クローバーシアター上映スケジュール(http://www.d-live.info/program/movie/index.php)
+ 京都シネマ上映スケジュール（本学学生は割引料金で鑑賞可能）(http://www.kyotocinema.jp/)
+ 課外プログラム
++ ライブ（http://www.d-live.info/program/live/index.php）
++ その他（http://www.d-live.info/program/other/index.php）
+ !英語版ニュース
+ 商学部(https://com.doshisha.ac.jp/news/news/)
+ 経済学部(https://www.econ.doshisha.ac.jp/news/topics/)
+ 学部・研究科一覧（https://www.doshisha.ac.jp/academics/）
+ 赤ちゃん学研究センター(https://akachan.doshisha.ac.jp/)
+ 研究開発機構（https://kikou.doshisha.ac.jp/organization/advance.html）
+ 研究一覧（https://www.doshisha.ac.jp/news/person/）

# Scripts execution
+ python3 doshisha_theater.py
+ python3 event.py

+ python3 twitter_bot.py
+ python3 doshisha_en_news.py
+ python3 faculty.py
+ python3 paper.py
+ python3 repository_ranking.py

Twitter Link: https://twitter.com/doshishauni_inf
