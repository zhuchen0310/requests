# conding = utf-8

import requests
import re
import json
from retrying import retry


class NeiHanDuanZi(object):
    """爬取内涵段子"""

    def __init__(self):
        self.headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

        self.proxies = {
            'https':'https://177.92.19.238:53281'
        }
        self.url = 'http://www.neihanshequ.com'
        self.next_url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"

    @retry(stop_max_attempt_number=3)
    def _pares_url(self, url):
        response = requests.get(url, headers=self.headers,proxies=self.proxies,timeout=5)
        assert response.status_code == 200
        return response.content.decode()

    def pares_url(self, url):
        try:
            return self._pares_url(url)
        except:
            return None

    def get_content(self, html):
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>", html, re.S)
        max_time = re.findall(r'max_time: \'(\d+)\',',html)
        return content_list,max_time[0]

    def save_content(self, content_list):
        # 保存数据
        with open('./duanzi.txt', 'a', encoding='utf8') as f:
            for content in content_list:
                f.write(content)
                f.write('\n')


    def get_next_page_content(self,next_url):
        #todo
        print(next_url)
        json_response = self.pares_url(url=next_url)
        dict_response = json.loads(json_response)
        content_list = dict_response['data']['data']
        content_list = [i['group']['text'] for i in content_list]
        max_time = dict_response.get('data').get('max_time')
        has_more = dict_response.get('data').get('has_more')
        return content_list,max_time,has_more


    def run(self):  # 主程序
        # 1.构造url
        url = self.url
        # 2.发送请求
        html_str = self.pares_url(url)
        # 3.提取数据
        if html_str is not None:
            content_list,max_time = self.get_content(html_str)
        # 4.保存数据
            self.save_content(content_list)
        # 5.获取下一页的数据
            has_more = True
            while has_more:
                next_url= self.next_url.format(max_time)
                content_list,max_time,has_more = self.get_next_page_content(next_url)
                self.save_content(content_list)


if __name__ == '__main__':
    duanzi = NeiHanDuanZi()
    duanzi.run()
