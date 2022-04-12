# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/6 10:08
@Author  : GGStudy-DDUp
@FileName: antiy.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""

import scrapy
import SafeInfoCollect.items as items
from SafeInfoCollect.demo import date_demo as dd


class AntiySpider(scrapy.Spider):
    name = "antiy"

    start_urls = [
        'https://bbs.antiy.cn/forum-news-1.html'
    ]

    def parse(self, response, **kwargs):
        yield from response.follow_all(urls=response.xpath("/html/body/div[6]/div[4]/div/div[2]/div[4]/div[2]/form/table/tbody/tr/th/a[@class='s xst']/@href").extract(), callback=self.next_parse)

    def next_parse(self, response):
        # item = items.TutorialItem()
        # time = dd.choise_date(response.xpath('/html/body/div[6]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td/div[1]/div[2]/div[2]/em/text()')[0].extract())
        # for date in response.xpath('/html/body/div[6]/div[4]/div[2]/div[1]/table/tbody/tr/td/div/div/div[1]/table/tbody/tr/td'):
        #     item['source_url'] = response.url
        #     item['date_time'] = time
        #     item['date_title'] = date.xpath('./div[2]/h3/a/text()')[0].extract()
        #     item['date_content'] = date.xpath('./div[2]/div[2]/text()')[0].extract()
        #     item['date_url'] = date.xpath('./div[2]/div[1]/span[2]/a/@href')[0].extract()
        #     item['date_tag'] = '安全简讯'
        #     yield item
        print(response.xpath('/html/body/div[6]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[1]/table/tbody/tr/td/font[2]/text()[2]'))