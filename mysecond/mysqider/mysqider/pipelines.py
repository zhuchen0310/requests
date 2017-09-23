# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


# class TencentPipeline(object):
class YangPipeline(object):
# class YangguangPipeline(object):
#     pass

    def __init__(self):
        # self.file = open('./teacher.json','wb')

        self.file = open('./yang.json','ab')

    def process_item(self, item, spider):
        print(item)
        content = json.dumps(dict(item),ensure_ascii=False,indent=4) + '\n'
        self.file.write(content.encode('utf8'))
        return item

    def close_spider(self,spider):
        self.file.close()
