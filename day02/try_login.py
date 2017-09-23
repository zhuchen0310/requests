# coding=utf-8

import requests
import json
headers = {

}
url = ''
data = {

}
# 发送网页请求,获取网页源码
responses = requests.get(url,headers=headers)
html = responses.content.decode()
json_html = json.loads(html)