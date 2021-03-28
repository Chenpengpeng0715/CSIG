# -*- coding:utf-8 -*-
# author:
# datetime:2019/8/29 19:21
# -*- coding:utf-8 -*-
# author:
# datetime:2019/8/29 16:29
import csv
import random
import requests
from pyquery import PyQuery as pq

headers = {
    'Host': 'www.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/535.19',
    'Accept-Encoding': 'gzip',
}
# 请求头
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"]
head = {
    'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
}


def spiderDazhong(ID):
    try:
        html = requests.get("http://www.dianping.com/shop/%s" % (ID), headers=headers)
        doc = pq(html.text)
        # print(doc)
        if doc:
            item = doc(".photos").items()
            for i in item:
                # print(i)
                pic = i('img').items()
                for j in pic:
                    # print(j)
                    s = str(j.attr("data-lazyload"))
                    print(j.attr("data-lazyload"))
                    ft.write(s + '\n')
                    print("write successful")
    except Exception as e:
        print("error", str(e))


if __name__ == '__main__':
    # 代表各大商铺ID，可通过商铺列表页回去
    with open(r'E:\大众点评\pingjia2.txt', 'a') as ft, open(r"E:\大众点评\id.txt", 'r') as f:
       
        lines = f.readlines()
        # listShop = ["2972056", "91018291", "69952338"]
        # list_id = dazhongdianpin.test()
        # # print(list_id)
        for shop in lines:
            shop = shop.strip('\n')
            # print(shop)
            spiderDazhong(str(shop))
    # id = '131053378'
    # spiderDazhong(id)