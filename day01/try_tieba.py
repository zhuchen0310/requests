import requests
url = 'http://www.sina.com.cn/'
# response.text
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
# r = requests.get(url)
# r.encoding='utf8'
# print(r.text)


# response.content.decode
r = requests.get(url, headers=headers)
# print(r.content.decode())
# r.encoding='utf8'
# print(r.text)

# 获取请求头
print(r.request.headers)
print('*********')
# 请求url
print(r.request.url)
print('*********')
# 响应头
print(r.headers)