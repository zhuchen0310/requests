import time
from selenium import webdriver

dirver = webdriver.Chrome()
dirver.maximize_window()
dirver.get('https://www.baidu.com/')
dirver.find_element_by_id('kw').send_keys('北京')
dirver.find_element_by_id('su').click()

cookies = dirver.get_cookies()
print(cookies)
cookie = {cookie['name']:cookie['value'] for cookie in cookies}
print(cookie)
dirver.quit()