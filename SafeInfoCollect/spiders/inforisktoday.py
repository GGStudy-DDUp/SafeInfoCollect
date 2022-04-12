# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 10:24
@Author  : GGStudy-DDUp
@FileName: inforisktoday_spider.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""
import scrapy
import SafeInfoCollect.items as items
from SafeInfoCollect.demo import date_demo as dd


class InforisktodaySpider(scrapy.Spider):
    name = "inforisktoday"

    start_urls = [
        'https://www.inforisktoday.com/latest-news'
    ]

    def parse(self, response, **kwargs):
        item = items.TutorialItem()
        for date in response.xpath('/html/body/div[4]/div/div/div/section/div[1]/article'):
            item['source_url'] = response.url
            item['date_time'] = dd.change_date(date.xpath('./div/div[2]/p[1]/span[1]/text()')[0].extract())
            item['date_title'] = dd.sqliteEscape(dd.translate(date.xpath('./div/div[2]/h2/a/text()')[0].extract()))
            item['date_content'] = dd.sqliteEscape(dd.translate(date.xpath('./div/div[2]/p[2]/text()')[0].extract()))
            item['date_url'] = date.xpath('./div/div[2]/h2/a/@href')[0].extract()
            item['date_tag'] = '安全简讯'
            yield item
