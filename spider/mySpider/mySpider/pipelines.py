# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道保存数据
import json
import logging
logger = logging.getLogger(__name__)

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        logger.warning('pip管道成功')
        with open('./static/itcast.txt','a',encoding='utf8')as f:
            json.dump(item,f,ensure_ascii=False,indent=4)
        return item

class MyspiderPipeline1(object):
    def process_item(self,item,spider):
        logger.warning('管道接收成功')
        with open('./tieba.txt','a',encoding='utf8')as f:
            json.dump(item,f,ensure_ascii=False,indent=4)
        return item

