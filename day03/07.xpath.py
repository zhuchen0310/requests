# coding=utf-8

from lxml import etree

text = ''' <div> <ul> 
            <li class="item-1"><a >first item</a></li> 
            <li class="item-1"><a href="link2.html">second item</a></li> 
            <li class="item-inactive"><a href="link3.html">third item</a></li> 
            <li class="item-1"><a href="link4.html">fourth item</a></li> 
            <li class="item-0"><a href="link5.html">fifth item</a> 
            </ul> </div> '''

html = etree.HTML(text)
# print(html)

# print(etree.tostring(html).decode())

# print(etree.tostring(html).decode())  #etree.tostring能够把element对象转化为bytes
ret1 = html.xpath('//li[@class="item-1"]/a/@href')
print(ret1)
ret2 = html.xpath('//li[@class="item-1"]/a/text()')
print(ret2)# coding=utf-8
from lxml import etree

text = ''' <div> <ul> 
            <li class="item-1"><a >first item</a></li> 
            <li class="item-1"><a href="link2.html">second item</a></li> 
            <li class="item-inactive"><a href="link3.html">third item</a></li> 
            <li class="item-1"><a href="link4.html">fourth item</a></li> 
            <li class="item-0"><a href="link5.html">fifth item</a> 
            </ul> </div> '''

html = etree.HTML(text)
print(html)

# print(etree.tostring(html).decode())  #etree.tostring能够把element对象转化为bytes

# ret1 = html.xpath("//li[@class='item-1']/a/@href")
# print(ret1)

# ret2 = html.xpath("//li[@class='item-1']/a/text()")
# print(ret2)

# #组合成一个字典
# print("*"*20)
# for i in ret1:
#     item = {}
#     item["href"] = i
#     item["title"] = ret2[ret1.index(i)]
#     print(item)

print("*"*20)
#更完美的方式组合成一个字典
# li_list = html.xpath("//li[@class='item-1']")
# for li in li_list:
#     temp ={}
#     temp["href"]  = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href"))>0 else None
#     temp["title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()"))>0 else None
#     print(temp)

# for i in ret1:
#     item = {}
#     item["href"]=i
#     item['title'] = ret2[ret1.index(i)]
#     print(item)
# ret1 = html.xpath("//li[@class='item-1']/a/@href")
# print(ret1)

# ret2 = html.xpath("//li[@class='item-1']/a/text()")
# print(ret2)

#组合成一个字典
# print("*"*20)
# for i in ret1:
#     item = {}
#     item["href"] = i
#     item["title"] = ret2[ret1.index(i)]
#     print(item)
#
# print("*"*20)
#更完美的方式组合成一个字典
# li_list = html.xpath("//li[@class='item-1']")
# for li in li_list:
#     temp ={}
#     temp["href"]  = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href"))>0 else None
#     temp["title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()"))>0 else None
#     print(temp)

li_list = html.xpath('//li[@class="item-1"]')
for li in li_list:
    temp={}
    temp['href'] = li.xpath('./a/@href')[0] if len(li.xpath('./a/@href'))>0 else None
    temp['title'] = li.xpath('./a/text()')[0] if len(li.xpath('.a/text()'))>0 else None