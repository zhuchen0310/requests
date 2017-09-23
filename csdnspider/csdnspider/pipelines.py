# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from .settings import MONGO_HOST,MONGO_PORT
class CsdnspiderPipeline(object):

    def open_spider(self,spider):
        client = MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        self.collection = client["csdn"]["info"]

    def process_item(self, item, spider):
        self.collection.insert(item)
        print("保存成功!")
        return item
