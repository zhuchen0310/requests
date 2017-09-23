# coding=utf-8

import json
listStr = [{"city": "北京"}, {"name": "大刘"}]
json.dump(listStr,open('listStr.json','w'),ensure_ascii=False)
dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr,open('dictStr.json','w'),ensure_ascii=False)

strlist = json.load(open('listStr.json','r'))
print(strlist)