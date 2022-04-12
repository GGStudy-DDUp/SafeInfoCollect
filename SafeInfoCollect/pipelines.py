# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from SafeInfoCollect.settings import *
import sqlite3


class TutorialPipeline:
    def process_item(self, item, spider):
        return item


class Sqlite3Pipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect(SQLITE_DATABASE)
        self.c = self.conn.cursor()
        try:
            sql = "CREATE TABLE InfoDate(source_url TEXT, date_title TEXT, date_content TEXT, date_url TEXT, date_time TEXT, date_tag TEXT);"
            self.c.execute(sql)
            self.conn.commit()
        except:
            print('', end='')

    def process_item(self, item, spider):

        sql = "SELECT * FROM InfoDate WHERE date_title='%s'" % (item['date_title'])
        self.c.execute(sql)
        if not self.c.fetchall():
            sql = "INSERT INTO InfoDate (source_url,date_title,date_content,date_url,date_time,date_tag) VALUES ('{}','{}','{}','{}','{}','{}');".format(
                item['source_url'], item['date_title'], item['date_content'], item['date_url'], item['date_time'],
                item['date_tag'])
            self.c.execute(sql)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.c.close()
        self.conn.close()


