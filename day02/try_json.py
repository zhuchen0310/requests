# coding=utf-8

import requests
import json
from pprint import pprint
url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1504692320027"
response = requests.get(url=url)
json_response = response.content.decode()
# filr_path = 'json.json'
# pprint(json_response,indent=2)
dic_json = json.loads(json_response)
# file_path = 'json1.json'
# with open(file_path,'w',encoding='utf8') as f:
#     f.write(str(dic_json))