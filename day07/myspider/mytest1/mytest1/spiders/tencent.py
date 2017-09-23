# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']
    # page_lx = LinkExtractor(allow=(r'position_detail.php'))

    rules = (
        Rule(LinkExtractor(allow=(r'position_detail.php')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        items = response.xpath("//tr[contains(@class,'even') or contains(@class,'odd')]")
        for item in items:
            temp = dict(
                name=item.xpath("./td[1]/a/text()").extract_first(),
                detailLink='http://hr.tencent.com' + item.xpath("./td[1]/a/@href").extract_first(),
                positionInfo=item.xpath("./td[2]/text()").extract_first(),
                peopleNumber=item.xpath("./td[3]/text()").extract_first(),
                workLocation=item.xpath("./td[last()-1]/text()").extract_first(),
                publishTime=item.xpath("./td[last()]/text()").extract_first()
            )

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
            print(temp)
            yield temp
