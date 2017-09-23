# coding=utf-8

import requests
import re
import json
from lxml import etree
from threading import Thread
from queue import Queue

from retrying import retry

import time
class QiuShiSpider(object):
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

        }
        self.proxies = {
            'https': 'https://177.92.19.238:53281'

        }
        # 创建三个队列 分别用来保存 url html  content
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):  # 1. 构造url_list
        # 构造url_list 放入url_queue
        for i in range(1, 14):
            self.url_queue.put(self.start_url.format(i))

    @retry(stop_max_attempt_number=3)
    def _pares_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=5)
        assert response.status_code == 200
        html = etree.HTML(response.content)
        return html

    def pares_url(self):  # 2. 从url队列中取出url 发送请求获得页面信息
        while True:
            url = self.url_queue.get()  # 取
            try:
                html = self._pares_url(url)
            except Exception as e:
                print(e)
                html = None
            self.html_queue.put(html)  # 存 html
            self.url_queue.task_done()  # 减

    def get_html_content(self):  # 3. 提取页面信息 用户名  性别 年龄 段子内容等
        while True:
            html = self.html_queue.get()  # 取
            if html is not None:
                div_list = html.xpath("//div[contains(@id,'qiushi_tag_')]")
                if div_list is not None:
                    all_content_list = []
                    for div in div_list:
                        temp = {}
                        temp['user_img'] = div.xpath("./div[@class='author clearfix']/a/img/@src")[0] \
                            if len(div.xpath("./div[@class='author clearfix']/a/img/@src")) > 0 else None
                        temp['user_name'] = div.xpath("./div[@class='author clearfix']/a/img/@alt")[0] \
                            if len(div.xpath("./div[@class='author clearfix']/a/img/@alt")) > 0 else None
                        temp['user_gender'] = div.xpath("./div[@class='author clearfix']/div/@class")[0].split(' ')[
                            -1].replace('Icon', '') \
                            if len(div.xpath("./div[@class='author clearfix']/div/@class")) > 0 else None
                        temp['user_age'] = div.xpath("./div[@class='author clearfix']/div/text()")[0] \
                            if len(div.xpath("./div[@class='author clearfix']/div/text()")) > 0 else None
                        content_list = div.xpath(".//div[@class='content']/span/text()")
                        temp['content'] = content_list[0] if len(content_list) > 0 else None
                        temp['img_url'] = div.xpath(".//img[@class='illustration']/@src")[0] \
                            if len(div.xpath(".//img[@class='illustration']/@src")) > 0 else None

                        all_content_list.append(temp)
                    content = all_content_list
                    self.content_queue.put(content)  # 加
            self.html_queue.task_done()  # 减

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            if content_list is not None:
                with open('./qiushi.txt', 'a', encoding='utf8') as f:
                    for content in content_list:
                        f.write(str(content['user_img']))
                        f.write(str(content['user_name']))
                        f.write(str(content['user_gender']))
                        f.write(str(content['user_age']) + '\n')
                        f.write(content['content'] + '\n')
                        f.write(str(content['img_url']))
                print('*'*50)
            self.content_queue.task_done()

    def run(self):
        # 1. 构造url_list
        url_list = self.get_url_list()
        # 2. 发送请求获得页面信息
        for url in url_list:
            html = self.pares_url(url)
            # 3. 提取页面信息 用户名  性别 年龄 段子内容等
            all_content_list = self.get_html_content(html)
            # 4. 保存信息
            if len(all_content_list) > 0:
                for content in all_content_list:
                    self.save_content_list(content)
            print('第 %s 页' % (url_list.index(url) + 1))

    def threading_run(self):
        # 多线程版
        thread_list = []
        # 1. 创建多线程对象url
        t_url = Thread(target=self.get_url_list)
        thread_list.append(t_url)

        # 2. 从url队列中取出url发送请求 返回html 存入html 队列
        t_pares_url = Thread(target=self.pares_url)
        thread_list.append(t_pares_url)
        # 3. 从 html 队列中取出html  查内容 返回content 存入 content队列
        t_get_content = Thread(target=self.get_html_content)
        thread_list.append(t_get_content)
        # 4. 从 content 队列中取出 content 保存
        t_save = Thread(target=self.save_content_list)
        thread_list.append(t_save)
        # 开启多线程
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        # 结束队列
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()

if __name__ == '__main__':
    a = time.clock()
    qiushi = QiuShiSpider()
    qiushi.threading_run()
    b = time.clock()
    print('耗时: %f' %b)
