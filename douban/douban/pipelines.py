# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from .settings import MONGO_PORT,MONGO_HOST
class DoubanPipeline(object):
    def open_spider(self,spider):
        client = MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        self.colliction = client["douban"]["movie_top250"]
    def process_item(self, item, spider):
        self.colliction.insert(item)
        return item
