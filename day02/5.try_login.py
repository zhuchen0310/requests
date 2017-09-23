# coding = utf-8
import re

import requests

Cookie = "anonymid=j3jxk555-nrn0wh; _r01_=1; _ga=GA1.2.1274811859.1497951251; depovince=GW; JSESSIONID=abcR4Hb6q8UvJgS4-gv5v; jebecookies=f02f07fd-4785-4e76-8863-8bc43b4caa05|||||; ick_login=86b4009c-dcff-45f6-8e65-85c52051eee6; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=3e3722ea3698e4b19244ec00f663d0749; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=1afbedd2801096fa4a70e0d447da4a029; societyguester=1afbedd2801096fa4a70e0d447da4a029; id=327550029; xnsid=a9c19747; loginfrom=syshome; ch_id=10016; wp_fold=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",

}

# 把cookie 转换为字符串形式
dict_cookie = {
   i.split('=')[0]:i.split('=')[1] for i in Cookie.split(';')
}
# 添加cookie参数来接收字典形式的cookie
responses = requests.get('http://www.renren.com/327550029/profile',headers=headers)
html = responses.content.decode()

print(re.findall('毛',html))