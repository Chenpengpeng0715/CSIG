# -*- coding:utf-8 -*-
# author:
# datetime:2019/10/23 15:22
import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os
import random
import hashlib
from PIL import Image


num = 0
numPicture = 0
file = ''
List = []


def Find(url):
    global List
    print('正在检测图片总数，请稍等.....')
    t = 0
    i = 1
    s = 0
    while t < 1000:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            # print(result)
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
            # print('obj'+str(pic_url))
            # pic_url = re.findall('"middleURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
            # print('middle'+str(pic_url_middle))
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t = t + 60
    return s


def recommend(url):
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    Re = []
    try:
        html = requests.get(url)
    except error.HTTPError as e:
        return
    else:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text, 'html.parser')
        div = bsObj.find('div', id='topRS')
        if div is not None:
            listA = div.findAll('a')
            for i in listA:
                if i is not None:
                    Re.append(i.get_text())
        # print(Re)
        return Re


def dowmloadPicture(html, keyword, file):
    global num
    # t =0
    # d = {"政治卡通漫画": "politics_images", "讽刺漫画简笔画": "satire_images",
    #      "肖像漫画": "portrait_images", "手绘钢笔人像": "Hand-painted_images",
    #      "写实油画人物": "realistic_images", "卡通人物头像": "cartoon_images", "中国政治漫画": "politics", "讽刺连环画黑白": "satire",
    #      "夸张肖像画人物": "portrait", "手绘漫画人像": "Hand-painted",
    #      "人物肖像油画": "realistic", "卡通头像人物": "cartoon"}
    # d = {"中国政治漫画": "politics", "讽刺连环画黑白": "satire",
    #      "夸张肖像画人物": "portrait", "手绘漫画人像": "Hand-painted",
    #      "人物肖像油画": "realistic", "卡通头像人物": "cartoon"}
    d = {'q版白雪公主': "111"}
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    # print(html)
    pic_url_middle = re.findall('"middleURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    print(pic_url)
    print(pic_url_middle)
    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    for i in range(len(pic_url)):
        # print(html)
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(pic_url[i]))
        try:
            if pic_url[i] is not None:
                pic = requests.get(pic_url[i], timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            my_md5 = hashlib.md5()  # 获取一个MD5的加密算法对象
            my_md5.update(pic_url_middle[i].encode("utf-8"))  # 得到MD5消息摘要
            my_md5_Digest = my_md5.hexdigest()  # 以16进制返回消息摘要，32位
            # string = file + r'\\' + d[keyword] + '_' + str(num) + '.jpg'
            # print(string)
            # string = file + r'\\' + my_md5_Digest + '.' + str(pic_url[i]).split(".")[-1]
            string = file + r'\\' + my_md5_Digest + '.jpg'
            print(pic)
            try:
                fp = open(string, 'wb')
                fp.write(pic.content)
                fp.close()
                print(pic_url[i])
                print(pic_url_middle[i])
                print('下载完成')
            except Exception as e:
                print(e)

            # # try:
            # #     im = Image.open(string)
            # if not os.path.isfile(string.replace((d[keyword] + '_' + str(num)), str(hash))):
            #     print(string.replace((d[keyword] + '_' + str(num)), str(hash)))
            #     os.rename(string, string.replace((d[keyword] + '_' + str(num)), str(hash)))
                # num += 1
            # else:
            #     continue
                    # os.remove(string)
            # except:
            #     os.remove(string)
            #     continue
            num += 1
        if num >= numPicture:
            return

if __name__ == '__main__':  # 主函数入口
    tm = int(input('请输入每类图片的下载数量 '))
    numPicture = tm
    # line_list = []
    with open('./name.txt', encoding='utf-8') as file:
        line_list = [k.strip() for k in file.readlines()]  # 用 strip()移除末尾的空格

    for word in line_list:
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
        tot = Find(url)
        Recommend = recommend(url)  # 记录相关推荐
        print('经过检测%s类图片共有%d张' % (word, tot))
        # file = word + '文件'
        file = os.path.join(r"G:\images_baidu", word)
        y = os.path.exists(file)
        if y == 1:
            print('该文件已存在，请重新输入')
            file = word + '文件夹2'
            os.makedirs(file)
        else:
            os.makedirs(file)
        t = 0
        tmp = url
        while t < numPicture:
        # while t < tot:
            try:
                url = tmp + str(t)
                result = requests.get(url, timeout=10)
                print(url)
            except error.HTTPError as e:
                print('网络错误，请调整网络后重试')
                t = t + 60
            else:
                dowmloadPicture(result.text, word, file)
                t = t + 60
        numPicture = numPicture + tm
    print('当前搜索结束，感谢使用')
