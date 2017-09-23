# coding=utf-8
from pprint import pprint
import json
import requests
from retrying import retry
headers ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

proxies = {
"http": "http://180.118.128.122:900"
}

@retry(stop_max_number=3)
def _parse_url(url):
    response = requests.get(url=url,headers=headers,timeout=5,verify=False)
    assert response.status_code == 200
    return response.content.decode()

def parse_url(url):
    try:
        return _parse_url(url)
    except:
        return  None
if __name__ == '__main__':
    html = parse_url('http://www.12306.cn/mormhweb/')
    pprint(html)



