# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem


class TxSpider(scrapy.Spider):
    name = "tx"
    allowed_domains = ["tencent.com"]
    start_urls = ['http://hr.tencent.com/position.php?&start=#a0']

    def parse(self, response):
        tr_list = response.xpath('//*[@id="position"]/div[1]/table//tr[contains(@class,"even") or contains(@class,"odd")]')
        for tr in tr_list:
            item = TencentItem()
            item['title'] = tr.xpath('./td[1]/a/text()').extract_first()
            item['url'] = 'http://hr.tencent.com/'+tr.xpath('./td[1]/a/@href').extract_first()
            item['position'] = tr.xpath('./td[2]/text()').extract_first()
            item['number'] = tr.xpath('./td[3]/text()').extract_first()
            item['city'] = tr.xpath('./td[4]/text()').extract_first()
            item['publish_date'] = tr.xpath('./td[5]/text()').extract_first()
            print(item)
            yield item

        # 获取下一页url
        next_page_url_temp = response.xpath("//div[@class='pagenav']/a[text()='下一页']/@href").extract_first()
        next_page = 'http://hr.tencent.com/'+next_page_url_temp if next_page_url_temp != 'javascript:;' else None
        if next_page is not None:
            yield scrapy.Request(
                next_page,
                callback= self.parse
            )
