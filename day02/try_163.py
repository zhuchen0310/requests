# coding=utf-8
import requests
import json

class EmailLogin(object):
    def __init__(self):  # 初始化
        self.data = {
          'email':'15513979101',
            'password':'48290415'
        }
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                     '537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

    def send_url(self):
        response = requests.post('https://dl.reg.163.com/l',self.data,self.headers)
        html = response.content.decode()
        # json_info = json.loads(html)
        # print(json_info)
        print(html)

if __name__ == '__main__':
    email = EmailLogin()
    email.send_url()