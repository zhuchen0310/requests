# coding=utf-8
import requests
import time
from lxml import etree
from retrying import retry


class TieBaSpider(object):
    INDEX = 1
    # 百度贴吧  爬去所有帖子标题 url 和图片
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'

        }
        self.url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---1/m?kw=' + self.tieba_name + '&pn={}'
        self.proxies = {
            'https': 'https://177.92.19.238:53281'
        }

    def get_url_list(self): # 构造 url_list
        url_list = [self.url.format(i*20) for i in range(0,101)]
        return url_list

    @retry(stop_max_attempt_number=3)
    def _pares_url(self, url):
        response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=5)
        assert response.status_code == 200
        html = etree.HTML(response.content)
        return html

    def pares_url(self, url):  # 发送url请求
        try:
            return self._pares_url(url)
        except Exception as e:
            print(e)
            return None

    def get_html_content(self, html):
        # 1.将response转换为emelent格式
        # 2.获取所有div节点
        div_list = html.xpath('//div[contains(@class,"i")]')
        # 3.遍历div_list
        content_list = []  # 用来保存数据字典[{title:,href:},{}]
        if len(div_list) > 0:
            for div in div_list:
                temp = {}
                temp['title'] = div.xpath('./a/text()')[0] if len(div.xpath('./a/text()')) > 0 else None
                print(temp['title'])
                temp['href'] = 'http://tieba.baidu.com' + div.xpath('./a/@href')[0] if len(
                    div.xpath('./a/@href')) > 0 else None
                content_list.append(temp)
            return content_list

    def get_content_img_url(self, img_html):  # 提取图片
        img_list = img_html.xpath('//img[@class="BDE_Image"]/@src')
        if len(img_list) > 0:
            img_url_list = [requests.utils.unquote(i).split('src=')[-1] for i in img_list]
            return img_url_list

    def save_content(self, content_list):
        # 保存数据
        if len(content_list) > 0:
            with open('./tie.txt', 'a', encoding='utf8') as f:
                f.write('第 '+str(self.INDEX)+'页:\n')
                for content in content_list:
                    f.write('主题:'+content['title'] + '\n')
                    f.write('链接:'+content['href'] + '\n\n', )
                    f.write('图片:'+str(content['img_url']) + '\n\n\n')
                    f.write('\n\n\n\n')


    def run(self):
        # 1. 构造url
        url = self.url
        # 2. 发送请求
        html = self.pares_url(url)
        # 3. 提取数据
        content_list = self.get_html_content(html)
        # 4. 发送详情页请求 获得图片url
        for content in content_list:  # 用来保存数据字典[{title:,href:},{}]
            img_html = self.pares_url(content['href'])
            # 4.1 提取img url
            img_list = self.get_content_img_url(img_html)
            content['img_url'] = img_list
        # 4. 保存数据
        self.save_content(content_list)

        # 5. 执行结束
        print('下一页')


    def run_try(self):
        url_list = self.get_url_list()
        for url in url_list:
            # 2. 发送请求
            html = self.pares_url(url)
            # 3. 提取数据
            content_list = self.get_html_content(html)
            # 4. 发送详情页请求 获得图片url
            for content in content_list:  # 用来保存数据字典[{title:,href:},{}]
                img_html = self.pares_url(content['href'])
                # 4.1 提取img url
                img_list = self.get_content_img_url(img_html)
                content['img_url'] = img_list
            # 4. 保存数据
            self.save_content(content_list)

            # 5. 执行结束
            print('执行结束')
            self.INDEX += 1


if __name__ == '__main__':
    tieba = TieBaSpider('李毅')
    tieba.run_try()
