# coding=utf-8

import requests
import json
from lxml import etree
from threading import Thread
from queue import Queue

import time

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}

data = {
'webwork.token.name':'newsDetele.token',
'newsDetele.token':'85M8310BCRL286UR02X7IMQIMER3I628',
'ec_i':'ec',
'ec_crd':15,
'ec_p':1,
'newsDetele.token':'63QH33WBAPRYW26G8HNP6KDG8ZKRWT6U',
'newsDetele.token':'1KX9QYLRPTAE2WZ86UK3CXH57QNI4D7L',
'webwork.token.name':'newsDetele.token',
'webwork.token.name':'ewsDetele.token',
'subjectid':3657

}

while data['ec_p'] < 250:
    url = 'http://www.yongji.gov.cn/main/newsMore.action'

    response = requests.post(url,data=data,headers=headers)
    print('第 %s 页'%data['ec_p'])
    time.sleep(3)
    html = etree.HTML(response.text)
    tr_list = html.xpath('//*[@id="ec_table"]/tbody/tr')
    content_list = []
    for tr in tr_list:
        item = {}
        item['content'] = tr.xpath('./td[2]/a/text()')[0] if len(tr.xpath('./td[2]/a/text()'))>0 else None
        item['date'] = tr.xpath('./td[3]/text()')[0] if len(tr.xpath('./td[3]/text()'))>0 else None
        item['url'] = 'http://www.yongji.gov.cn/main'+tr.xpath('./td[2]/a/@href')[0] if len(tr.xpath('./td[2]/a/@href'))>0 else None
        content_list.append(item)
    #
    with open('./yongji.txt','a',encoding='utf8') as f:
        for content in content_list:
            f.write(json.dumps(content,ensure_ascii=False,indent=4))
    data['ec_p'] += 1
print('执行结束')