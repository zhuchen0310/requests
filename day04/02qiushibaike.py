#coding=utf-8

import requests
import re
import json
from lxml import etree
class QiuShiSpider(object):

    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

        }
        self.proxies = {
            'https': 'https://177.92.19.238:53281'

        }

    def get_url_list(self): #1. 构造url_list
        url_list = [self.start_url.format(i) for i in range(1,14)]
        return url_list


    def pares_url(self,url):  #2. 发送请求获得页面信息
        responses = requests.get(url,headers=self.headers,timeout=5)
        return etree.HTML(responses.content)

    def get_html_content(self,html): #3. 提取页面信息 用户名  性别 年龄 段子内容等
        div_list = html.xpath("//div[contains(@id,'qiushi_tag_')]")
        if div_list is not None:
            all_content_list = []
            for div in div_list:
                temp = {}
                temp['user_img'] = div.xpath("./div[@class='author clearfix']/a/img/@src")[0] \
                    if len(div.xpath("./div[@class='author clearfix']/a/img/@src"))>0 else None
                temp['user_name'] = div.xpath("./div[@class='author clearfix']/a/img/@alt")[0] \
                    if len(div.xpath("./div[@class='author clearfix']/a/img/@alt"))>0 else None
                temp['user_gender'] = div.xpath("./div[@class='author clearfix']/div/@class")[0].split(' ')[-1].replace('Icon','') \
                    if len(div.xpath("./div[@class='author clearfix']/div/@class"))>0 else None
                temp['user_age'] = div.xpath("./div[@class='author clearfix']/div/text()")[0] \
                    if len(div.xpath("./div[@class='author clearfix']/div/text()"))>0 else None
                content_list = div.xpath(".//div[@class='content']/span/text()")
                temp['content'] = content_list[0] if len(content_list)>0 else None
                temp['img_url'] = div.xpath(".//img[@class='illustration']/@src")[0] \
                    if len(div.xpath(".//img[@class='illustration']/@src"))>0 else None

                all_content_list.append(temp)
            return all_content_list


    def save_content_list(self,content):
        with open('./qiushi.txt','a',encoding='utf8') as f:
            f.write(str(content['user_img']))
            f.write(str(content['user_name']))
            f.write(str(content['user_gender']))
            f.write(str(content['user_age'])+'\n')
            f.write(content['content']+'\n')
            f.write(str(content['img_url']))


    def run(self):
        #1. 构造url_list
        url_list = self.get_url_list()
        #2. 发送请求获得页面信息
        for url in url_list:
            html = self.pares_url(url)
        #3. 提取页面信息 用户名  性别 年龄 段子内容等
            all_content_list = self.get_html_content(html)
        #4. 保存信息
            if len(all_content_list)>0:
                for content in all_content_list:
                    self.save_content_list(content)
            print('第 %s 页' %(url_list.index(url)+1))

if __name__ == '__main__':
    qiushi = QiuShiSpider()
    qiushi.run()