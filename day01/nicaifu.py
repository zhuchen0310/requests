# coding=utf-8
import requests

url = 'https://www.nicaifu.com/trans'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
formdata = {
'last_id':388152,
'reqtoken':'8a0589ae9ddbc3a3ad5631f83b9ca1e72a39c3055b53515e17bf5143777911d3',
"type": "AUTO",
"i": "i love python",
"doctype": "json",
"xmlVersion": "1.8",
"keyfrom": "fanyi.web",
"ue": "UTF-8",
"action": "FY_BY_ENTER",
"typoResult": "true"
}

r = requests.post(url=url,data=formdata,headers=headers)
# print(r.content.decode())
print(r.json(h))