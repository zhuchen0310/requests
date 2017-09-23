# -*- coding: utf-8 -*-
import scrapy
import logging


logger = logging.getLogger(__name__)

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://tieba.baidu.com/f?kw=%E6%B0%B8%E6%B5%8E']

    def parse(self, response):
        tiebas = response.xpath('//ul[@id="thread_list"]/li[@class="j_thread_list clearfix"]')
        for tie in tiebas:
            title = tie.xpath(".//a[@class='j_th_tit']/text()").extract_first()
            url = tie.xpath(".//a[@class='j_th_tit']/@href").extract_first()
            sub_title = tie.xpath(".//div[contains(@class,'threadlist_abs')]/text()").extract_first()
            item = dict(
                title = title,
                url = url,
                sub_title = sub_title
            )
            logger.warning("spider成功")
            yield item


