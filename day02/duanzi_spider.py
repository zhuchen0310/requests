# coding=utf-8
from pprint import pprint

import requests
import json
import re
class DuanZi_Spider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"

        }
        self.proxies = {
            "http": "115.46.97.114:8123",
            # "http": "http://110.73.9.82:8123",
            # "http": "http://121.232.144.138:9000",
            # "http": "http://117.90.1.122:9000",
            # "http": "http://122.96.59.107:843",
            # "http": "http://121.232.194.195:9000",

        }
        self.url = 'http://www.neihan8.com/article/list_5_1.html'

    def parse_url(self,url):
        response = requests.get(url,timeout=10,verify=False,headers=self.headers)
        if response.status_code == 200:
            return response.content.decode('gbk')
        else:
            raise ValueError('status_code is:',response.status_code)

    def get_content(self,html):
        '''
        根据网页对象匹配标题和段子内容
        :param html: 
        :return: 
        '''

        pattern = re.compile(r'<a href="/article/\d+\.html">(.*?)</a>.*?<div\sclass="f18 mb20">(.*?)</div>', re.S)  #### (r'<a href="/article/(?P<html_id>\d+)\.html">(.*?)</a>(.*?)<div class="f18 mb20">(.*?)</div>,re.S')
        ret = pattern.findall(html)
        content = []
        for i in ret:
                con = re.sub(r'\n|<p>|\u3000|<br />|<b>|</b>|</p>|&ldquo;|&rdquo;|&rdquo', '', i[1])
                con = con.replace('&ldquo;','"').replace('&rdquo','"').replace('&hellip;','...')
                title = i[0].replace('<b>','').replace('</b>','')
                content.append([title,con])
        return content

    def save_content(self,content):     # 保存数据
        with open('./duanzi.txt','a',encoding='utf8') as myFile:
            for temp in content:
                index = content.index(temp)+1
                myFile.write(str(index)+'.'+temp[0]+'\n'+temp[1]+'\n')
        print('执行完成!')



    def run(self):      # 主要函数
        # 1.构造url_list
        url = self.url
        # 2.发送请求
        content_html = self.parse_url(url=url)
        # 3.处理数据
        content = self.get_content(html=content_html)
        # 4.保存数据
        self.save_content(content=content)




if __name__ == '__main__':
    duanzi = DuanZi_Spider()
    duanzi.run()