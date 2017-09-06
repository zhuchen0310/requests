# coding=utf-8
import requests
import json


class BaiDuFanYi(object):
    '''
        百度翻译
    '''

    def __init__(self, query_string):  # 初始化
        self.query_string = query_string
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }
        self.url = 'http://fanyi.baidu.com/v2transapi'

    def get_post_data(self):  # 构造form data
        post_data = {
            'from': self.langdetect(),
            'to': 'en',
            'query': self.query_string,
            'transtype': 'translang',
            'simple_means_flag': 3
        }
        return post_data

    def parse_url(self, data, url='http://fanyi.baidu.com/v2transapi'):  # 发送请求
        responses = requests.post(data=data, url=url, headers=self.headers, timeout=5, verify=False)
        return responses.content.decode()

    def get_trans_ret(self, json_response):  # 提取json数据
        dict_response = json.loads(json_response)
        print(dict_response.get('trans_result').get('data')[0].get('dst'))

    def langdetect(self):  # 检测语言信息
        check_lang_data = {
            'query': self.query_string
        }
        response = self.parse_url(data=check_lang_data,
                                  url='http://fanyi.baidu.com/langdetect')
        form = json.loads(response)
        return form.get('lan')

    def run(self):  # 运行
        # 1.获取url
        # 1.1检测语言
        check_langer = self.langdetect()
        # 2.构造form data
        data = self.get_post_data()
        # 3.发送请求
        json_response = self.parse_url(data=data)
        # 4.提取json数据
        self.get_trans_ret(json_response)


if __name__ == '__main__':
    while True:
        query_string = input('请输入要翻译的文字:')
        fanyi = BaiDuFanYi(query_string)
        fanyi.run()
