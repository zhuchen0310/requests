# -*- coding: utf-8 -*-
import scrapy
import logging
import re
import json
logger = logging.getLogger(__name__)

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    # start_urls = ['http://hr.tencent.com/position.php?&start=0']
    start_urls = ['http://hr.tencent.com/position.php?&start={}'.format(i) for i in range(0,1000,10)]

    def parse(self, response):
        items = response.xpath("//tr[contains(@class,'even') or contains(@class,'odd')]")
        for item in items:
            temp = dict(
                name=item.xpath("./td[1]/a/text()").extract_first(),
                detailLink = 'http://hr.tencent.com'+item.xpath("./td[1]/a/@href").extract_first(),
                positionInfo = item.xpath("./td[2]/text()").extract_first(),
                peopleNumber = item.xpath("./td[3]/text()").extract_first(),
                workLocation = item.xpath("./td[last()-1]/text()").extract_first(),
                publishTime = item.xpath("./td[last()]/text()").extract_first()
            )

            logger.warning('spider_success')
            yield temp

        # now_page = int(re.search(r'\d+',response.url).group(0))
        # print('*'*60)
        # if now_page < 216:
        #     url = re.sub(r'\d+',str(now_page+10),response.url)
        #     print('下一个url:%s'%url)
        #     yield scrapy.Request(url,callback=self.parse)

