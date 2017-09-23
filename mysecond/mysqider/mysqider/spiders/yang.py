# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class YangSpider(scrapy.Spider):
    name = "yang"
    allowed_domains = ["sun0769.com"]
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?page={}'.format(i) for i in range(30,100,30)]


    def parse(self, response):
        items = response.xpath("//*[@id='morelist']/div/table[2]/tbody/tr/td/table/tbody/tr")
        for item in items:
            temp = dict(
                complain_id=item.xpath("./td[1]/text()").extract_first(),
                complain_url=item.xpath("./td[2]/a[2]/@href").extract_first(),
                complain_title=item.xpath("./td[2]/a[2]/text()").extract_first(),
                from_place=item.xpath("./td[2]/a[3]/text()").extract_first(),
                complain_state=item.xpath("./td[3]/span/text()").extract_first(),
                complain_user=item.xpath("../td[4]/text()").extract_first(),
                complain_time=item.xpath("../td[5]/text()").extract_first(),

            )
            print(temp)
            logger.warning('111')
            yield temp

