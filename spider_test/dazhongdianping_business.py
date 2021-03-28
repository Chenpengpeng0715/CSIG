# -*- coding:utf-8 -*-
# author:
# datetime:2019/8/29 16:29
import csv
import requests
from pyquery import PyQuery as pq


headers = {
    'Host': 'www.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/535.19',
    'Accept-Encoding': 'gzip',
}


def spiderDazhong(ID):
    try:
        for i in range(5):
            # html = requests.get("http://www.dianping.com/shop/%s/review_all" % (ID), headers=headers)
            html = requests.get("http://www.dianping.com/shop/%s/officialphotos?pg=%s" % (ID, str(i)), headers=headers)
            doc = pq(html.text)
            print(doc)
            # if doc:
            #     pinglunLi = doc(".J_list .img a img").items()
            #     print(pinglunLi)
            #     for item in pinglunLi:
            #         # s = "http://www.dianping.com" + item.attr("href")
            #         s = item.attr("src")
            #         print(str(s))
            #         ft.write(s + "\n")
            #         print("successful write txt!")
    except Exception as e:
        print("error", str(e))


if __name__ == '__main__':
    # 代表各大商铺ID，可通过商铺列表页回去
    with open(r'E:\大众点评\shangjia2.txt', 'a') as ft:
        # with open(r"E:\大众点评\id.txt", 'r') as f:
        #     lines = f.readlines()
        #     # print(lines)
        #     # listShop = ["2972056", "91018291", "69952338"]
        #     # list_id = dazhongdianpin.test()
        #     # # print(list_id)
        #     for shop in lines:
        #         shop = shop.strip('\n')
        #         print(shop)
        #         spiderDazhong(shop)
        id = '97792763'
        spiderDazhong(id)