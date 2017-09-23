# coding=utf-8
import requests
import re
import json
from retrying import retry
from lxml import etree



class BaiDuTieBa(object):

    def __init__(self,tieba_name):
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---/m?kw={}".format(tieba_name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'

        }
        self.proxies = {
            'https': 'https://177.92.19.238:53281'

        }

    @retry(stop_max_attempt_number=3)
    def _pares_url(self, url):
        response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=5)
        assert response.status_code == 200
        html = etree.HTML(response.content)
        return html

    def pares_url(self, url):  # 发送url请求
        try:
            return self._pares_url(url)
        except Exception as e:
            print(e)
            return None

    def get_html_content_list(self,html):
        if html is not None:
            #1.获取所有div标签
            div_list= html.xpath("//div[contains(@class,'i')]")
            content_list = []
            if len(div_list) > 0 :
                for div in div_list:
                    temp = {}
                    title = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()"))>0 else None
                    detail_url = 'http://tieba.baidu.com' + div.xpath("./a/@href")[0] \
                        if len(div.xpath("./a/@href"))>0 else None
                    temp['title'] = title
                    temp['url'] = detail_url
                    content_list.append(temp)
                next_url = html.xpath("//a[text()='下一页']/@href")
                next_page_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2'+next_url[0] if len(next_url)>0 else None
                return content_list,next_page_url

    def get_img_list(self,html):
            img_list = html.xpath('//img[@class="BDE_Image"]/@src')
            if img_list is not None:
                img_url_list = [requests.utils.unquote(i).split('src=')[-1] for i in img_list]
                return img_url_list

    def save_content(self,content_list):
        with open('./tiebaba.txt','a',encoding='utf8') as f:
            for content in content_list:
                f.write(content['title']+'\n')
                f.write(content['url']+'\n\n')
                f.write(str(content['img_url'])+'\n\n\n')

    def run(self):
        #1. 起始页url
        next_url = self.start_url
        while next_url is not None:
            print(next_url)
        #2. 发送URL 请求获得响应
            html = self.pares_url(next_url)
        #3. 从响应体中提取 主题, 连接, 下一页信息
            content_list,next_url = self.get_html_content_list(html)
        #4. 请求详情页获得图片地址
            if content_list is not None:
                for content in content_list:
                    detail_html = self.pares_url(content['url'])
                    # 4. 提取详情页图片信息
                    content['img_url'] = self.get_img_list(detail_html)
        #4. 保存数据 并将下一页的url继续执行
                self.save_content(content_list)

if __name__ == '__main__':
    tieba=BaiDuTieBa('永济')
    tieba.run()