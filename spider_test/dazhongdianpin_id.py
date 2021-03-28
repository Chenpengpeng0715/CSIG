# -*- coding:utf-8 -*-
# author:
# datetime:2019/8/22 11:03
import requests
from bs4 import BeautifulSoup
import os
# import
# # soup = BeautifulSoup(open('http://www.dianping.com/shanghai/ch10/r801'))
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver import ActionChains
# import re
import json
import requests
import re

# with open(r"D:\faceid\script\爬虫\大众点评.josn", 'w') as f:
#     for i in range(1):
#         base_url = 'http://www.dianping.com/shanghai/ch10/p'
#         url = 'http://www.dianping.com/mylist/ajax/shoprank?rankId=fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0'
#         header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#
#         # request = ur.Request(url, headers=header)
#         # response = ur.urlopen(request)
#         html = requests.get(base_url, headers=header)
#         data = str(html.text)
#         for data in json.loads(data)["shopBeans"]:
#             print(data["shopId"])
        # soupIn = BeautifulSoup(response, 'html.parser')
        # f.write(str(soupIn))
        #
        # print(soupIn)
        # a = soupIn.find_all(id='shop-all-list')
        # print(a)
        # json.loads(list(soupIn))
        # r = requests.post(url, headers=header)
        # result = json.loads(r.text)
        # print(result)
        # for k in soupIn.find_all("a"):
        #     print(k)


# driver = webdriver.Chrome(r'D:\faceid\chromedriver.exe')
# driver.get('http://www.baidu.com/')
# a = ActionChains(driver)
# driver.implicitly_wait(5)
# print("----")
# # target = driver.find_element_by_id("yodaBox").click()
# driver.find_element_by_name('tj_trnews').click()
# # a.click_and_hold(target)
# print("======")
# a.move_by_offset(200, 0)
# print('eeeee')
import json
import random
import requests


# 城市列表
list_city = [["上海", "fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0"],
             ["北京", "d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0"],
             ["广州", "e749e3e04032ee6b165fbea6fe2dafab71862f838d1255ea693b953b1d49c7c0"],
             ["深圳", "e049aa251858f43d095fc4c61d62a9ec71862f838d1255ea693b953b1d49c7c0"],
             ["天津", "2e5d0080237ff3c8f5b5d3f315c7c4a508e25c702ab1b810071e8e2c39502be1"],
             ["杭州", "91621282e559e9fc9c5b3e816cb1619c71862f838d1255ea693b953b1d49c7c0"],
             ["南京", "d6339a01dbd98141f8e684e1ad8af5c871862f838d1255ea693b953b1d49c7c0"],
             ["苏州", "536e0e568df850d1e6ba74b0cf72e19771862f838d1255ea693b953b1d49c7c0"],
             ["成都", "c950bc35ad04316c76e89bf2dc86bfe071862f838d1255ea693b953b1d49c7c0"],
             ["武汉", "d96a24c312ed7b96fcc0cedd6c08f68c08e25c702ab1b810071e8e2c39502be1"],
             ["重庆", "6229984ceb373efb8fd1beec7eb4dcfd71862f838d1255ea693b953b1d49c7c0"],
             ["西安", "ad66274c7f5f8d27ffd7f6b39ec447b608e25c702ab1b810071e8e2c39502be1"]]
# 请求头
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)']
head = {
    'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
}
list_id = []


# 解析
def findFood(city, data):
    global flag, code
    for data in json.loads(data)["shopBeans"]:
        # print(data)
        # 商铺图片
        # defaultPic = data["defaultPic"]
        # 分类名称
        shopId = data["shopId"]
        # 商铺网址
        shopUrl = "http://www.dianping.com/shop/" + shopId
        params = (shopUrl, shopId, city)
        try:
            # print(params)
            f.write(params[1]+'\n')
            list_id.append(params[1])
        except:
            # pass
            print("error！")
    # print(list_id)
    # return list_id


# 抓取
def foodSpider(city_list):
    city = city_list[0]
    url = city_list[1]
    base_url = "http://www.dianping.com/mylist/ajax/shoprank?rankId=" + url
    html = requests.get(base_url, headers=head)
    findFood(city=city, data=str(html.text))


if __name__ == '__main__':
    with open(r"E:\大众点评\id.txt", 'a') as f:
        for city_data in list_city:
            foodSpider(city_data)
