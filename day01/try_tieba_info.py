# coding=utf-8
import requests


class TieBaInfo():
    ''' 
    贴吧类
    '''

    def __init__(self, tieba_name):  # 初始化
        self.tieba_name = tieba_name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }
        self.temp_url = 'http://tieba.baidu.com/f?kw=' + tieba_name + '&pn={}'

    def get_url_list(self):  # 构造url_list
        url_list = [self.temp_url.format(i * 5) for i in range(100)]
        return url_list

    def parse_url(self, url):  # 获取响应
        response = requests.get(url, self.headers)
        return response.content.decode()

    def save_html(self, html, page_num):  # 保存数据
        file_path = self.tieba_name + '_' + str(page_num) + '.html'
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(html)

    def run(self):
        # 1.url_list
        url_list = self.get_url_list()
        # 2.发送请求
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.保存数据
            page_num = url_list.index(url) + 1
            self.save_html(html=html_str, page_num=page_num)
        print('保存成功')
if __name__ == '__main__':
    tieba = TieBaInfo(tieba_name='永济')
    tieba.run()