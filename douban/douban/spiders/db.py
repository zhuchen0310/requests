# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DbSpider(CrawlSpider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        # 找下一页url
        Rule(LinkExtractor(allow=r'\?start=\d+&filter=$'),follow=True),
        Rule(LinkExtractor(allow=r'https://movie\.douban\.com/subject/\d+/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['movie_title'] =response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        # item['movie_year'] = response.xpath('//*[@id="info"]/span[11]/text()').extract_first()
        item['movie_dirctor'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract_first()
        # item['movie_star'] = response.xpath('//*[@id="info"]/span[3]/span[2]/span[1]/a/text()').extract_first()
        item['movie_tating_num'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        # item['movie_run_time'] = response.xpath('//*[@id="info"]/span[13]/text()').extract_first()
        item['movie_year'] = re.findall(r'<span property="v:initialReleaseDate" content=".*?">(.*?)</span><br/>',response.text,re.S)[0] if len(re.findall(r'<span property="v:initialReleaseDate" content=".*?">(.*?)</span><br/>',response.text,re.S))>0 else None
        item['movie_star'] = re.findall(r'rel="v:starring">(.+?)</a>',response.text,re.S) if len(re.findall(r'rel="v:starring">(.+?)</a>',response.text,re.S))>0 else None
        item['movie_run_time'] = re.findall(r'<span property="v:runtime" content="\d+">(.*?)</span><br/>',response.text,re.S)[0] if len(re.findall(r'<span property="v:runtime" content="\d+">(.*?)</span><br/>',response.text,re.S))>0 else None


        # item['movie_']
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # print(item)
        yield item
