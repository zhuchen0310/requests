 # -*- coding: utf-8 -*-
# import scrapy
# from
#
# class ExampleComSpider(scrapy.Spider):
#     name = "myfirst"
#     allowed_domains = ["example.com"]
#     start_urls = [
#         'http://www.example.com/1.html',
#         'http://www.example.com/2.html',
#         'http://www.example.com/3.html',
#
#     ]
#
#     def parse(self, response):
#         sel = scrapy.Selector(response)
#         for h3 in response.xpath('//h3').extract():
#

# import scrapy
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor
#
# class MySpider(CrawlSpider):
#     name = 'myfirst'
#     allowed_domains = ['example.com']
#     start_urls = ['http://www.example.com']
#
#     rules = (
#         # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
#         Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
#
#         # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
#         Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
#     )
#
#     def parse_item(self, response):
#         self.log('Hi, this is an item page! %s' % response.url)
#
#         item = scrapy.Item()
#         item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
#         item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
#         item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
#         return item


from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider
from ..items import TestItem

class MySpider(XMLFeedSpider):
    name = 'myfirst'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        log.msg('Hi, this is a <%s> node!: %s' % (self.itertag, ''.join(node.extract())))

        item = TestItem()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item