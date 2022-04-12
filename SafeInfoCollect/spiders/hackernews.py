# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/6 9:46
@Author  : GGStudy-DDUp
@FileName: hackernews.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""
import scrapy
import SafeInfoCollect.items as items
from SafeInfoCollect.demo import date_demo as dd


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"

    start_urls = [
        'https://hackernews.cc/archives/category/%e4%bb%8a%e6%97%a5%e6%8e%a8%e9%80%81',
        'https://hackernews.cc/archives/category/%e5%9b%bd%e9%99%85%e5%8a%a8%e6%80%81',
        'https://hackernews.cc/archives/category/%e6%bc%8f%e6%b4%9e%e4%ba%8b%e4%bb%b6',
        'https://hackernews.cc/archives/category/%e9%bb%91%e5%ae%a2%e4%ba%8b%e4%bb%b6',
        'https://hackernews.cc/archives/category/%e6%95%b0%e6%8d%ae%e6%b3%84%e9%9c%b2'
    ]

    def parse(self, response, **kwargs):
        item = items.TutorialItem()
        for date in response.xpath('/html/body/div[2]/div/div/div/section/section/div/article'):
            item['source_url'] = response.url
            item['date_time'] = date.xpath('./div[2]/div[1]/span[2]/a/text()')[0].extract()
            item['date_title'] = dd.sqliteEscape(date.xpath('./div[2]/h3/a/text()')[0].extract())
            item['date_content'] = dd.sqliteEscape(date.xpath('./div[2]/div[2]/text()')[0].extract())
            item['date_url'] = date.xpath('./div[2]/div[1]/span[2]/a/@href')[0].extract()
            item['date_tag'] = '安全简讯'
            yield item
