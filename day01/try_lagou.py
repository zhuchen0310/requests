# coding=utf-8
import requests
import time

class LaGouHtml(object):
    '''lagou'''

    def __init__(self, language_name):  # 初始化
        self.language_name = language_name
        self.headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }
        self.formdata = {
            'last_id': '388152',
            'reqtoken': '8a0589ae9ddbc3a3ad5631f83b9ca1e72a39c3055b53515e17bf5143777911d3'
        }
        self.temp_url = 'https://www.lagou.com/zhaopin/' + language_name + '/{}/'

    def get_url_list(self):  # 构造url_list
        url_list = [self.temp_url.format(i) for i in range(1, 2)]
        print(url_list)
        return url_list

    def send_request(self, url):  # 发送请求
        response = requests.get(url, self.headers)
        return response.content.decode()

    def save_html(self, html, page_index):  # 保存数据
        file_path = self.language_name + '-' + str(page_index) + '.html'
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(html)

    def run(self):  # 主程序
        # 1.构造url_list
        url_list = self.get_url_list()
        # 2.发送请求
        for url in url_list:
            html = self.send_request(url)
            # 3.保存数据
            page_index = url_list.index(url) + 1
            time.sleep(5)
            self.save_html(html, page_index)


if __name__ == '__main__':
    # Todo
    lagou = LaGouHtml('Python')
    lagou.run()
