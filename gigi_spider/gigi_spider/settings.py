# Scrapy settings for gigi_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime
BOT_NAME = 'gigi_spider'

SPIDER_MODULES = ['gigi_spider.spiders']
NEWSPIDER_MODULE = 'gigi_spider.spiders'

Today = datetime.datetime.now()
LOG_FILE = "gigi_spider/log/{}.{}.{}_{}.{}.{}.log".format(
    Today.year,
    Today.month,
    Today.day,
    Today.hour,
    Today.minute,
    Today.second)

# Crawl responsibly by identifying yourself (and your website) on the user-agent

USER_AGNET_LIST = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; \
        .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',

    "Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.1 (KHTML, like Gecko) \
            Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) \
        AppleWebKit/536.11 (KHTML, like Gecko) \
            Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/536.6 (KHTML, like Gecko) \
            Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) \
        AppleWebKit/536.6 (KHTML, like Gecko) \
            Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) \
        AppleWebKit/537.1 (KHTML, like Gecko) \
            Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) \
        AppleWebKit/536.5 (KHTML, like Gecko) \
            Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) \
        AppleWebKit/536.5 (KHTML, like Gecko) \
            Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) \
        AppleWebKit/536.3 (KHTML, like Gecko) \
            Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) \
        AppleWebKit/535.24 (KHTML, like Gecko) \
            Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) \
        AppleWebKit/535.24 (KHTML, like Gecko) \
            Chrome/19.0.1055.1 Safari/535.24"]

# USER_AGENT = 'gigi_spider (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'

IP_LIST = [
    "https://195.154.255.194:8000",
    "https://202.169.51.46:8080",
    "https://200.13.22.210:80",
    "https://123.56.250.62:60080",
    "https://41.77.13.186:53281",
    "https://5.153.234.91:3128",
    "https://39.105.156.66:60080",
    "https://39.105.15.159:60080",
    "https://41.77.13.186:53281",
    "https://190.61.48.25:999",
    "https://118.31.2.38:8999",
    "https://103.11.107.50:3125",
    "https://195.154.255.194:8000",
    "https://103.173.128.51:8080",
    "https://102.68.130.18:6666",
    "https://195.154.255.194:8000",
    "https://5.153.234.91:3128",
    "https://39.105.108.22:60080",
    "https://182.92.161.220:60080",
    "https://39.107.234.215:60080",
    "https://39.105.156.66:60080",
    "https://85.14.243.31:3128",
    "https://39.105.15.159:60080",
    "https://39.105.15.159:60080",
    "https://39.105.15.159:60080",
    "https://195.154.255.194:8000",
    "https://39.105.156.66:60080",
    "https://103.173.128.51:8080",
    "https://118.31.2.38:8999",
    "https://201.222.83.145:999",
    "https://103.173.128.51:8080",
    "https://182.92.161.220:60080",
    "https://201.71.2.152:999",
    "https://103.243.177.90:8080",
    "https://85.14.243.31:3128",
    "https://201.71.2.152:999",
    "https://200.13.22.210:80",
    "https://41.77.13.186:53281",
    "https://201.71.2.152:999",
    "https://102.68.130.18:6666",
    "https://103.153.254.111:8888",
    "https://123.56.250.62:60080",
    "https://201.71.2.152:999",
    "https://194.169.167.5:8080",
    "https://201.222.83.145:999",
    "https://41.77.13.186:53281",
    "https://201.71.2.152:999",
    "https://102.68.130.18:6666",
    "https://39.105.108.22:60080",
    "https://182.92.161.220:60080"]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# CONCURRENT_REQUESTS = 16


# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'gigi_spider.middlewares.GigiSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',
    'scrapy_fake_useragent.providers.FakerProvider',
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',
]


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#     'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'gigi_spider.pipelines.GigiSpiderPipeline': 300,
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

MONGODB_URI = "mongodb://10.108.17.218:27017"
MONGODB_DB = "gigi"
