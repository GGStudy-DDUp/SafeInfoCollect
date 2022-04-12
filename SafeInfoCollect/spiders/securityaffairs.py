# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/6 11:14
@Author  : GGStudy-DDUp
@FileName: securityaffairs.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""

import scrapy
import SafeInfoCollect.items as items
from SafeInfoCollect.demo import date_demo as dd


class SecurityaffairsSpider(scrapy.Spider):
    name = "securityaffairs"

    start_urls = [
        'https://securityaffairs.co/wordpress/page/1',
        'https://securityaffairs.co/wordpress/page/2',
        'https://securityaffairs.co/wordpress/page/3'
    ]

    def parse(self, response, **kwargs):
        item = items.TutorialItem()
        for date in response.xpath("/html/body/div[2]/div[5]/div/div/div[1]/div/div/div"):
            item['source_url'] = response.url
            item['date_time'] = dd.change_date(date.xpath("./div[4]/a[1]/text()")[0].extract())
            item['date_title'] = dd.sqliteEscape(dd.translate(date.xpath("normalize-space(./div[2]/div/h3/a/text())")[0].extract()))
            item['date_content'] = dd.sqliteEscape(dd.translate(date.xpath("normalize-space(./div[3]/p/text())")[0].extract()))
            item['date_url'] = date.xpath("./div[2]/div/h3/a/@href")[0].extract()
            item['date_tag'] = '安全简讯'
            yield item
