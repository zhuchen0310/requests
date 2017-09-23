from pprint import pprint

import requests
from lxml import etree
url = 'https://m.nicaifu.com/'
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
response = requests.get(url,headers)
html = etree.HTML(response.content.decode())
# with open('./nicaifu.html','a',encoding='utf8') as f:
#     f.write(response.content.decode())
#     print('down!')
# <Element html at 0x1f10a43c708>
# <Element html at 0x24676bac708>
a = html.xpath('//title/text()')
print(a)