
# coding=utf-8
from lxml import etree


# 组成字典{title:,href:}
text = ''' <div> <ul> 
            <li class="item-1"><a >first item</a></li> 
            <li class="item-1"><a href="link2.html">second item</a></li> 
            <li class="item-inactive"><a href="link3.html">third item</a></li> 
            <li class="item-1"><a href="link4.html">fourth item</a></li> 
            <li class="item-0"><a href="link5.html">fifth item</a> 
            </ul> </div> '''


#1. 先将字符串转换为emelent对象
html = etree.HTML(text)

#2. 对html进行xpath操作取值
# li_list = html.xpath('//li[@class="item-1"]')
# print(html.xpath('//li/a/text()'))
# for li in li_list:
#     temp = {}
#     temp['title'] = li.xpath('./a/text()')[0]  if len(html.xpath('./a/text()')) > 0 else None
#     temp['href'] = li.xpath('./a/@href')[0] if len(html.xpath('./a/@href')) > 0 else None
#     print(temp)
#
li_list = html.xpath('//li')
for li in li_list:
    # print(li.xpath('./a/text()'))
    # print(li.xpath('./a/@href'))
    temp = {}
    temp['title'] = li.xpath('./a/text()')[0] if len(li.xpath('./a/text()')) > 0 else None
    temp['href'] = li.xpath('./a/@href')[0] if len(li.xpath('./a/@href')) > 0 else None
    print(temp)