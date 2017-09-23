# coding=utf-8
import json

import time

from selenium import webdriver



class DouYu(object):
    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def get_content_list(self):  # 提取数据
        li_list = self.driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
        content_list = []
        if len(li_list) is not None:
            for li in li_list:
                temp = {}
                title = li.find_element_by_xpath('./a').get_attribute('title')
                temp['title'] = title
                img = li.find_element_by_xpath('.//img').get_attribute('src')
                temp['img'] = img
                game = li.find_element_by_xpath(".//span[@class='tag ellipsis']").text
                temp['game'] = game
                user_name = li.find_element_by_xpath(".//span[contains(@class,'dy-name')]").text
                temp['user_name'] = user_name
                person_num = li.find_element_by_xpath(".//span[contains(@class,'dy-num')]").text
                temp['person_num'] = person_num
                content_list.append(temp)
                print(temp)
            next_page_url = self.driver.find_elements_by_class_name('shark-pager-next')
            next_page_url = next_page_url[0] if len(next_page_url) > 0 else None
            return content_list, next_page_url

    def save_content_list(self, content_list):  # 保存数据
        with open('./douyu.txt', 'a',encoding='utf8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=4))
                f.write('\n')

    def run(self):
        # 1.发送访问请求
        self.driver.get(self.start_url)
        # 2.提取页面数据
        content_list = self.get_content_list()
        # 3.提取数据
        content_list, next_page = self.get_content_list()
        # 4.保存数据
        self.save_content_list(content_list)
        print('执行完一页!')
        while next_page is not None:
            next_page.click()
            time.sleep(3)
            content_list, next_page = self.get_content_list()
            self.save_content_list(content_list)

    def __delete__(self, instance):
        self.driver.quit()

if __name__ == '__main__':
    time.clock()
    douyu = DouYu()
    douyu.run()
    print(time.clock())
