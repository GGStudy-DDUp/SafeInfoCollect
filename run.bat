start cmd /k "cd Web && python -m flask run"
:scrapy_name
scrapy crawl venustech
scrapy crawl venustech2
scrapy crawl inforisktoday
scrapy crawl hackernews
scrapy crawl securityaffairs
# 定时时间，单位秒
choice /t 6000 /d y /n >nul
goto scrapy_name