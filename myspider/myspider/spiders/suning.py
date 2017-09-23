# -*- coding: utf-8 -*-
import re

import scrapy
from copy import deepcopy


class SuningSpider(scrapy.Spider):
    name = "suning"
    allowed_domains = ["suning.com"]
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap']/li")
        for li in li_list:
            item = {}
            item['b_cate'] = li.xpath("./div[1]/a/text()").extract_first()
            a_list = li.xpath("./div[2]/a")
            for a in a_list:
                item['s_cate'] = a.xpath("./text()").extract_first()
                item['s_href'] = 'http://snbook.suning.com'+a.xpath("./@href").extract_first() \
                    if len(a.xpath("./@href"))>0 else None
                item['next_page_num'] = 2
                yield scrapy.Request(
                    item['s_href'],
                    callback=self.parse_book_list,
                    meta={'item':deepcopy(item)}
                )

    def parse_book_list(self,response):
        item=response.meta['item']
        li_list = response.xpath('//*[@id="mainSearch"]/div[1]/ul/li')
        for li in li_list:
            item['book_img'] = li.xpath('.//img/@src').extract_first()
            item['book_title'] = li.xpath('.//img/@alt').extract_first()
            item['book_href'] = li.xpath('.//div[@class="book-title"]/a/@href').extract_first()
            item['book_author'] = li.xpath(".//div[@class='book-author']/a/text()").extract_first()
            item['book_publish'] = li.xpath("//div[@class='book-publish']/a/text()").extract_first()
            item['book_descrip'] = li.xpath("./div[2]/div[3]/text()").extract_first()
            yield scrapy.Request(
                item['book_href'],
                callback=self.parse_book_detail,
                meta={'item':deepcopy(item)}
            )
        # 获取下一页url
        next_page_temp = response.meta['item']
        next_page = next_page_temp['s_href']+'?pageNumber={}&sort=0'.format(next_page_temp['next_page_num'])
        # 获得总的页码数
        total_page_num = re.findall(r"var pagecount=(\d+);",response.body.decode())[0]
        if item['next_page_num'] <= int(total_page_num):
            item['next_page_num'] += 1
            print(item['next_page_num'])
            yield scrapy.Request(
                next_page,
                callback=self.parse_book_list,
                meta={'item':deepcopy(next_page_temp)}
            )

    def parse_book_detail(self,response):
        item= deepcopy(response.meta['item'])
        price_temp = re.findall(r'\"bp\":\'(.*?)\'',response.body.decode(),re.S)
        item['book_price'] = price_temp[0] if len(price_temp)>0 else None
        yield item