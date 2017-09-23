import time
from selenium import webdriver

# dirver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin')
driver = webdriver.Chrome()
# dirver.get('https://www.nicaifu.com/')
# dirver.find_element_by_name("mobile").
# send_keys('15513979101')
# dirver.find_element_by_id("passwordInput").send_keys('zhuchen@360')
# dirver.find_element_by_id("user_login_submit").click()
# cookies = dirver.get_cookies()
# print({cookie['name']:cookie['value'] for cookie in cookies})

# a = dirver.find_element_by_xpath("//div[contains(@class,'mc')]/ul/li/a[@class]").get_attribute('href')
# b = dirver.find_element_by_xpath('*//a').get_attribute('href')
# print(b)

driver.get("http://www.baidu.com")
# print(driver.find_elements_by_xpath("//a"))
time.sleep(5)
# print(driver.find_element_by_xpath('//*[@id="page"]/a[10]').get_attribute("href"))