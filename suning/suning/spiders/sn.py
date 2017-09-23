# -*- coding: utf-8 -*-
import scrapy


class SnSpider(scrapy.Spider):
    name = "sn"
    allowed_domains = ["suning.com"]
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        # li_list = response.xpath('//ur[@class="ulwrap"]/li')
        # for li in li_list:
        #     item = {}
        #     item['book_cate'] = li.xpath("./div[1]//a/text()").extract_first()
        #     print(item['book_cate'])
        #     a_list = li.xpath("./div[2]/a")
        #     for a in a_list:
        #         item['sbook_cate'] = a.xpath("./text()").extract_first()
        #         item['sbook_url'] = 'http://snbook.suning.com'+a.xpath("./@href").extract_first() if len(a.xpath("./@href"))>0 else None
        #
        #         print(item)
        #         yield item
        pass