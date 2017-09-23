# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysqiderItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()
    # name = scrapy.Field()

#
# class TencentItem(scrapy.Item):
#     name = scrapy.Field()
#     detailLink = scrapy.Field()
#     positionInfo = scrapy.Field()
#     peopleNumber = scrapy.Field()
#     workLocation = scrapy.Field()
#     publishTime = scrapy.Field()


