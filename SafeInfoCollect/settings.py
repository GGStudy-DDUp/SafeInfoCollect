# 项目启动名
BOT_NAME = 'SafeInfoCollect'

# 爬虫项目名
SPIDER_MODULES = ['SafeInfoCollect.spiders']
NEWSPIDER_MODULE = 'SafeInfoCollect.spiders'

# 日志信息
LOG_LEVEL = 'INFO'
# LOG_FILE = 'date.log'

# 数据库名
SQLITE_DATABASE = 'date.db'

"""
有道翻译关键字符，查询方式：
1、访问有道 https://fanyi.youdao.com/
2、F12打开调试窗口
3、在源代码列找到 fanyi.min.js 文件
4、在文件中找到 sign: n.md5("fanyideskweb" + e + i + "XXX"), XXX为所需关键字
5、拷贝关键字替换 TRANSLATE_KEYWORD 
6、在调试窗口切换到控制台
7、输入 document.cookie
8、复制输出值，替换 TRANSLATE_COOKIES 
9、可尝试登录有道，再获取Cookie修改

注：无法翻译先尝试修改Cookie，后查看KEYWORD，KEYWORD无问题更换多次Cookie均无法翻译尝试更换IP或代理
"""
TRANSLATE_KEYWORD = "Ygy_4c=r#e#4EX^NUGUc5"
TRANSLATE_COOKIES = 'OUTFOX_SEARCH_USER_ID=-451061600@113.109.41.46; UM_distinctid=17fed645f85cb0-04d6c2a4f1f621-26021b51-144000-17fed645f8610be; OUTFOX_SEARCH_USER_ID_NCOO=2042273742.5933518; fanyi-ad-id=305426; fanyi-ad-closed=1; JSESSIONID=aaaeiM8jVDcasbopyTBay; ___rl__test__cookies=1649732323290'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'SafeInfoCollect (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'SafeInfoCollect.middlewares.TutorialSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'SafeInfoCollect.middlewares.RandomUserAgentMiddleware': 500,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'SafeInfoCollect.pipelines.Sqlite3Pipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# FEED_EXPORT_ENCODING = 'utf-8'
