import re
from pprint import pprint

with open('./content.html','r',encoding='utf8') as f:
    html = f.read()
    # content = re.findall(r'"content":.*</p>"',html)
    con = re.findall(r'[\u4e00-\u9fa5]+',html)
    pprint(con)