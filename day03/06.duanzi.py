# import requests
#
# headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
#
# url = 'http://www.neihanshequ.com'
#
# response = requests.get(url,headers)
# with open('a.html','a',encoding='utf8') as f:
#     f.write(response.content.decode())



# coding=utf-8


import requests
from retrying import retry
import re
import json


class NeihanSpider(object):
    def __init__(self):
        self.start_url = "http://neihanshequ.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
        self.next_url_tmep = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"
        self.proxies = {
            'https': 'https://177.92.19.238:53281'
        }
    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):  # 发送请求,获取响应
        response = requests.get(url, headers=self.headers, proxies=self.proxies,timeout=5)
        assert response.status_code == 200
        return response.content.decode()

    def parse_url(self, url):  # 捕捉网络请求异常
        print("now parsing",url)
        try:
            return self._parse_url(url)
        except Exception as e:
            print(e)
            return None

    def get_content_list(self, html_str):  # 提取数据
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>", html_str, re.S)
        max_time = re.findall(r"max_time: '(.*?)',",html_str)
        return content_list,max_time[0]

    def save_content_lsit(self, content_list,index):  # 保存数据
        file_path = "./duanzi.text"
        with open(file_path, "a", encoding='utf-8') as f:
            for content in content_list:
                f.write(str(index)+content)
                f.write("\n")
                index += 1


    def get_next_page_content(self,url):
        json_response = self.parse_url(url)
        dict_response = json.loads(json_response)
        content_list = dict_response["data"]["data"]
        content_list = [i["group"]["text"] for i in content_list]
        max_time = str(int(dict_response["data"]["max_time"])+100000000.0)
        has_more = dict_response["data"]["has_more"]
        return content_list,max_time,has_more


    def run(self):
        # 1.start url
        # 2.发送请求,获取响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据
        index = 1
        if html_str is not None:
            content_list,max_time = self.get_content_list(html_str)
            # 4.保存
            self.save_content_lsit(content_list,index)
            #5.获取下一页的内容
            has_more = True

            while has_more:
                next_url = self.next_url_tmep.format(max_time)
                content_list, max_time, has_more = self.get_next_page_content(next_url)
                self.save_content_lsit(content_list,index)



if __name__ == '__main__':
    neihan = NeihanSpider()
    neihan.run()