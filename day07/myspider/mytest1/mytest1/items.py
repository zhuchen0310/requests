# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()

# class ZhihuItem(scrapy.Item)
import scrapy

class DongguanItem(scrapy.Item):
    # 每个帖子的标题
    title = scrapy.Field()
    # 每个帖子的编号
    number = scrapy.Field()
    # 每个帖子的文字内容
    content = scrapy.Field()
    # 每个帖子的url
    url = scrapy.Field()

