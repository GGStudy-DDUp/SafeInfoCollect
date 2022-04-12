# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 10:24
@Author  : GGStudy-DDUp
@FileName: venustech2_spider.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""
import scrapy
import SafeInfoCollect.items as items
from SafeInfoCollect.demo import date_demo as dd


class Venustech2_Spider(scrapy.Spider):
    name = "venustech2"

    start_urls = [
        'https://www.venustech.com.cn/new_type/aqtg/'
    ]

    def parse(self, response, **kwargs):
        url = []
        for date in response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/ul/li'):
            url.append(date.xpath('./a/@href')[0].extract())
        for i in url:
            x = response.urljoin(i)
            yield scrapy.Request(url=x, callback=self.next_parse, encoding='utf-8', meta={'url': x})

    def next_parse(self, response):
        li = []
        item = items.TutorialItem()
        item['source_url'] = response.url
        item['date_time'] = response.xpath('/html/body/div/div[4]/div[2]/div/div/div[2]/span/text()')[0].extract()
        li.append(response.xpath('/html/body/div/div[4]/div[2]/div/div/div[2]//text()').extract())
        item['date_title'], item['date_content'] = dd.date_venustech2(li[0])
        item['date_tag'] = '安全通告'
        item['date_url'] = response.meta['url']
        yield item

