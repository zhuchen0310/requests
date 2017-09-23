# -*- coding: utf-8 -*-
import scrapy
from yongjispider.yjspider.yjspider.items import YjspiderItem

class YjSpider(scrapy.Spider):
    name = "yj"
    allowed_domains = ["yongji.gov.cn"]
    start_urls = ['http://www.yongji.gov.cn/main/newsMore.action']

    def parse(self, response):
        tr_list = response.xpath('//*[@id="ec_table"]/tbody/tr') if len(response.xpath('//*[@id="ec_table"]/tbody/tr'))>0 else None
        for tr in tr_list:
            item = YjspiderItem()
            item['title'] = tr.xpath('./td[2]/a/text()')[0] if len(tr.xpath('./td[2]/a/text()')) > 0 else None
            item['publish_date'] = tr.xpath('./td[3]/text()')[0] if len(tr.xpath('./td[3]/text()')) > 0 else None
            item['url'] = 'http://www.yongji.gov.cn/main' + tr.xpath('./td[2]/a/@href')[0] if len(
                tr.xpath('./td[2]/a/@href')) > 0 else None
            yield item


