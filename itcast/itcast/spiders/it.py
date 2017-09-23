# -*- coding: utf-8 -*-
import re

import scrapy
from copy import deepcopy


class ItSpider(scrapy.Spider):
    name = "sn"
    allowed_domains = ["suning.com"]
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap']/li")
        for li in li_list:
            item = {}
            item["b_cate"] = li.xpath("./div[@class='second-sort']/a/text()").extract_first()
            a_list = li.xpath("./div[@class='three-sort']/a")
            for a in a_list:
                item['sbook_cate'] = a.xpath("./text()").extract_first()
                item['sbook_url'] = 'http://snbook.suning.com'+a.xpath("./@href").extract_first() if len(a.xpath("./@href"))>0 else None

                yield scrapy.Request(
                    item['sbook_url'],
                    callback=self.parse_book_list,
                    meta={'item':deepcopy(item),'next_page_num':2}
                )

    def parse_book_list(self,response):
        global item
        book_list = response.xpath('//*[@id="mainSearch"]/div[1]/ul/li')
        for book in book_list:
            item = response.meta['item']
            item['book_title'] = book.xpath("./div[1]//img/@alt").extract_first()
            item['book_img'] = book.xpath("./div[1]//img/@src").extract_first()
            item['book_url'] = book.xpath("./div[1]/a/@href").extract_first()
            item['book_author'] = book.xpath("./div[2]/div[2]/div[1]/a/text()").extract_first()
            item['book_publish'] = book.xpath("./div[2]/div[2]/div[2]/a/text()").extract_first()
            item['book_descrip'] = book.xpath("./div[2]/div[3]/text()").extract_first()

            yield scrapy.Request(
                item['book_url'],
                callback=self.parse_book_detail,
                meta={'item':deepcopy(item)}
            )
        # next_page_num = re.findall(r'var currentPage=(\d+);',response.body.decode(),re.S)
        now_number = response.meta['next_page_num']
        total_page_num = re.findall(r'var pagecount=(\d+);',response.body.decode(),re.S)[0]
        if now_number <= int(total_page_num):
            now_number +=1
            print(now_number)
            yield scrapy.Request(
                'http://snbook.suning.com/web/trd-fl/100303/48.htm?pageNumber={}&sort=0'.format(now_number),
                callback=self.parse_book_list,
                meta={'item':deepcopy(item),'next_page_num':now_number}
            )



    def parse_book_detail(self,response):
        item = response.meta['item']
        book_price = re.findall(r'"bp":\'(.*?)\',',response.body.decode(),re.S)[0]
        item['book_ price'] = book_price
        yield item