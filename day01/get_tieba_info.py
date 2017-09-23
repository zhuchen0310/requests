# coding=utf-8
import requests


class GetTieBaInfo(object):
    '''爬去贴吧信息'''

    def __init__(self, tieba_name):  # 初始化
        self.tieba_name = tieba_name
        self.hearders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

        }
        self.url = 'http://tieba.baidu.com/f?kw=' + tieba_name + '&pn={}'

    def get_url_list(self):  # 构建url_list
        url_list = [self.url.format(i * 50) for i in range(10)]
        return url_list

    def send_request(self, url):  # 发送请求
        response = requests.get(url, self.hearders)
        return response.content.decode()

    def save_html(self, html, page_index):  # 保存数据
        file_path = str(page_index) + '-' + self.tieba_name + '.html'
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(html)

    def run(self):  # 运行
        # 1.构造url_list
        url_list = self.get_url_list()
        # 2.发送request请求
        for url in url_list:
            response = self.send_request(url)
            page_index = url_list.index(url) + 1
            # 3.保存
            self.save_html(response, page_index)


if __name__ == '__main__':
    one_get = GetTieBaInfo('永济')
    one_get.run()
