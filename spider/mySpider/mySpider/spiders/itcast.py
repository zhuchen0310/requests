# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = "itcast"  # 爬虫名称
    allowed_domains = ["itcast.cn"] # 爬去的域名
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']    # 开始爬的网站

    def parse(self, response):
        teachers = response.xpath("//div[@class='tea_con']//li")

        for t in teachers:
            name = t.xpath(".//h3/text()").extract_first()
            position = t.xpath(".//h4/text()").extract_first()
            profile = t.xpath(".//p/text()").extract_first()
            item = dict(
                name = name,
                position = position,
                profile = profile,
                come_from = 'itcast'
            )
            logger.warning('spider成功')
            yield item
