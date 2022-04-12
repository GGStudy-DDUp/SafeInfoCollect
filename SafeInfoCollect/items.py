# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source_url = scrapy.Field()
    date_title = scrapy.Field()
    date_content = scrapy.Field()
    date_url = scrapy.Field()
    date_time = scrapy.Field()
    date_tag = scrapy.Field()
    pass

