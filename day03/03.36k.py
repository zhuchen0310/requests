# coding = utf-8

import re
import requests
import json
from utils import pares_url
# headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
# response = requests.get('http://36kr.com/',headers=headers)
# ret_html = response.content.decode()
#
# ret = re.findall(r'<script>var props={\"activeInvestors\|investor\":(.*?)locationnal=',ret_html,re.S)
# temp = ret[0] if len(ret)>0 else None
# if temp is not None:
#     with open('a.json','w',encoding='utf8') as f:
#         f.write(temp)

headers ={'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'}
url = 'http://m.neihanshequ.com/?is_json=1&app_name=neihanshequ_web&min_time=&csrfmiddlewaretoken=f73967dfde3e717f8bd337713bcce775'
data = {}

response = requests.get(url,headers)
print(response.content.decode())
