# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        with open('./a.txt','a',encoding='utf8') as f:
            f.write(json.dumps(item,ensure_ascii=False,indent=4))
        return item
