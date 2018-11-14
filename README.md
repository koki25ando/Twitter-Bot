# Blueprint
+ daily tweet bot
+ tweets are about news, topics and events that are related Doshisha university

# User Information
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
