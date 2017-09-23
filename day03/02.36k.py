# coding=utf-8
import re
import requests
import json

headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
response = requests.get("http://36kr.com/",headers=headers)
html_str = response.content.decode()

ret = re.findall(r"<script>var props=({\"activeInvestors\|investor\".*?),locationnal=",html_str,re.S)
temp = ret[0] if len(ret)>0 else None

if temp is not None:
    with open("a.json","w",encoding='utf8') as f:
        f.write(temp)
    temp_dict = json.loads(temp)
    print(temp_dict)