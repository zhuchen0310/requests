# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CsdnSpider(CrawlSpider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/peoplelist.html?channelid=0&page=1']

    rules = (
        # 专家列表页,没有可提取数据
        Rule(LinkExtractor(allow=r'http://blog.csdn.net/\w+$'), follow=True),
        # 翻页
        Rule(LinkExtractor(allow=r'/peoplelist.html?channelid=0&page=\d+$'), follow=True),
        # 专家详情页d 发送此url 提取数据
        Rule(LinkExtractor(allow=r'/caimouse/article/details/\d+$'), callback='parse_item', follow=True),
        # 专家详情页翻页
        Rule(LinkExtractor(allow=r'/caimouse/article/list/\d+$'), follow=True),

    )

    def parse_item(self, response):
        item = {}
        item['article_url'] = response.url
        item['article_title'] = response.xpath('//title/text()').extract_first()
        item['article_postdata'] = response.xpath('//span[@class="link_postdate"]/text()').extract_first()
        item['article_view'] = response.xpath('//span[@class="link_view"]/text()').extract_first()
        item['article_postdata'] = response.xpath('//span[@class="link_postdate"]/text()').extract_first()
        item['user_name'] = response.xpath('//div[@id="blog_userface"]//a[@class="user_name"]/text()').extract_first()
        item['article_content'] = response.xpath('//div[@id="article_content"]/text()').extract()
        print(item['article_title'])
        yield item
