# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 10:24
@Author  : GGStudy-DDUp
@FileName: venustech_spider.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""
import scrapy
import SafeInfoCollect.items as items
from SafeInfoCollect.demo import date_demo as dd


class VenustechSpider(scrapy.Spider):
    name = "venustech"

    start_urls = [
        'https://www.venustech.com.cn/new_type/aqjx/'
    ]

    def parse(self, response, **kwargs):
        url = []
        for date in response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/ul/li'):
            url.append(date.xpath('./a/@href')[0].extract())
        for i in url:
            x = response.urljoin(i)
            # print(x)
            yield scrapy.Request(url=x, callback=self.next_parse, encoding='utf-8')

    def next_parse(self, response):
        li = []
        temp = []
        source_url = response.url
        time = response.xpath('/html/body/div/div[4]/div[2]/div/div/div[2]/span/text()')[0].extract()
        for page2_date in response.xpath('/html/body/div/div[4]/div[2]/div/div/div[2]/div/p'):
            temp.append(page2_date.xpath('.//text()').extract())
        for i in temp:
            if i:
                li.append(i[0])
        item = items.TutorialItem()
        title, date, url, tag = dd.date_venustech(li)
        for i in range(len(title)):
            item['source_url'] = source_url
            item['date_title'] = dd.sqliteEscape(title[i])
            item['date_content'] = dd.sqliteEscape(date[i])
            item['date_url'] = url[i]
            item['date_time'] = time
            item['date_tag'] = tag[i]
            yield item

