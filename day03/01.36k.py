# coding=utf-8
import requests
import json
import re
class K_News(object):
    # 数据处理
    def __init__(self):

        with open('../day02/36.html','r',encoding='utf8') as f:
           self.html = f.read()
        self.data ={

        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"

        }
        self.proxies = {

        }

    def get_url_list(self,html):  # 提取url
        url_list = re.findall(r'"url.*?.html"',html)

    def parse_url(self,url):        # 发送请求
        responses = requests.get(url,self.headers)
        html = responses.content.decode()
        return html

    def save_content(self,content): # 保存数据
        file_name= 'content1.html'
        with open(file_name,'w',encoding='gbk') as f:
            f.write(content)
    def get_content(self,html): # 提取新闻内容
        content_list = re.findall()

if __name__ == '__main__':
    k = K_News()
    content = k.parse_url(url='http://36kr.com/p/5092139.html')
    k.save_content(content)