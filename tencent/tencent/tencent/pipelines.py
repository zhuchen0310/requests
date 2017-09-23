# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


# class TencentPipeline(object):
#     def process_item(self, item, spider):
#         with open('./tx.txt','a') as f:
#             f.write(json.dump(item,open('./tx.txt','a'),ensure_ascii=False,indent=4))
#
#         return item
class TencentPipeline(object):
    def process_item(self, item, spider):
        print("****%s******************************"%item)
        with open("tc.txt","a") as f:
            f.write(json.dumps(dict(item),ensure_ascii=False,indent=4).encode())
        return item