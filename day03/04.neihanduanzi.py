# conding = utf-8

import requests
import re
import json
from retrying import retry


class NeiHanDuanZi(object):
    """爬取内涵段子"""

    def __init__(self):
        self.headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

        self.url = 'http://www.neihanshequ.com'

    @retry(stop_max_attempt_number=3)
    def _pares_url(self, url):
        response = requests.get(url, headers=self.headers)
        assert response.status_code == 200
        return response.content.decode()

    def pares_url(self, url):
        try:
            return self._pares_url(url)
        except:
            return None

    def get_content(self, html):
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>", html, re.S)
        return content_list

    def save_content(self, content_list):
        # 保存数据
        with open('./duanzi.txt', 'w', encoding='utf8') as f:
            for content in content_list:
                        f.write(content)
                        f.write('\n')

    def run(self):  # 主程序
        # 1.构造url
        url = self.url
        # 2.发送请求
        html_str = self.pares_url(url)
        # 3.提取数据
        if html_str is not None:
            content_list = self.get_content(html_str)
        # 4.保存数据

            self.save_content(content_list)


if __name__ == '__main__':
    duanzi = NeiHanDuanZi()
    duanzi.run()
