# coding=utf-8
import re

import requests
import json
from retrying import retry



class TryHtml(object):
    '''
        36K
    '''

    def __init__(self):  # 初始化
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"

        }
        self.proxies = {
            "http":"http://121.232.147.76:9000",
            "http":"http://110.73.9.82:8123",
            "http": "http://121.232.144.138:9000",
            "http": "http://117.90.1.122:9000",
            "http": "http://122.96.59.107:843",
            "http": "http://121.232.194.195:9000",

        }
        self.url = 'http://36kr.com/p/5091{}.html'

    def get_url(self):
        url_list = [self.url.format(i) for i in range(800,890)]
        return url_list

    def parse_url(self,url='http://36kr.com/'):    # 发送请求
        try:
            responses = requests.get(url=url,headers=self.headers,proxies=self.proxies,
                                     timeout=5,verify=False)
            return responses.content.decode()
        except:
            return None

    def save_html(self,ret_html,page_num):    # 保存数据
        file_path = '36k'+str(page_num)+'.html'
        if ret_html:
            with open(file_path,'w',encoding='utf8') as f:
                f.write(ret_html)
        else:
            return
    def run(self):  # 主程序
        #1.构造url_List
        url_list = self.get_url()
        #2.发送请求
        for url in url_list:
            page_num = url_list.index(url)+1
            ret_html = self.parse_url(url)
        #3.保存数据
            self.save_html(ret_html,page_num)
    def run_two(self):
        ret_html = self.parse_url()
        pattern = re.compile('\d+')
        a_ret = pattern.findall(ret_html)
        print(str(a_ret))
if __name__ == '__main__':
    try_k = TryHtml()
    try_k.run_two()
    print('执行完成!')


