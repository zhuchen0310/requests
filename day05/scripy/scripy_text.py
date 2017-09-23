# coding=utf-8

import requests
import json

import time
from selenium import webdriver

class YongJinXinWen(object):
    page = 2

    def __init__(self):
        self.start_url = 'http://www.yongji.gov.cn/main/newsMore.action?subjectid=3657'
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        tr_list = self.driver.find_elements_by_xpath('//tbody[@class="tableBody"]/tr')
        content=[]
        for tr in tr_list:
            temp = {}
            temp['title'] = tr.find_element_by_xpath('.//a').text
            content.append(temp)
        next_page = self.driver.find_elements_by_xpath('//*[@id="ec"]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[4]/a')
        next_page = next_page[0] if len(next_page)>0 else None
        return content,next_page

    def save_content(self,content_list):
        if len(content_list) > 0:
            with open('./yongji.txt','a',encoding='utf8') as f:
                f.write('第%s页'%YongJinXinWen.page)
                for content in content_list:
                    f.write(content['title'])
                    f.write('\n')




    def run(self):
        #1. 发送访问请求
        self.driver.get(self.start_url)
        #2. 提取数据
        content_list,next_page = self.get_content_list()
        #4. 存储数据
        self.save_content(content_list)

        while next_page is not None:
            time.clock()
            next_page.click()
            time.sleep(2)
            content_list, next_page = self.get_content_list()
            self.save_content(content_list)
            YongJinXinWen.page += 1
            print('当前页耗时:%s' % (time.clock()))

    def __delete__(self, instance):
        self.driver.quit()


if __name__ == '__main__':
    time.clock()
    yongji = YongJinXinWen()
    yongji.run()
    print('总耗时:%s'%(time.clock()))
