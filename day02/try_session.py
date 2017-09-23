# coding=utf-8

import requests
import re
session = requests.session()
post_data = {
    "email": "mr_mao_hacker@163.com", "password": "alarmchime"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

session.post('http://www.renren.com/PLogin.do',data=post_data,headers=headers) # 发送post请求
# 使用带cookie 的session 发送请求
response = session.get('http://www.renren.com/327550029/profile')
html = response.content.decode()
# 判断是否登录成功
print(re.findall('毛',html))



