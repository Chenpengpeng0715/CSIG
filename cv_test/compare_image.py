# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/3/18 11:23
import os
import cv2
import time
import numpy as np
import shutil


# 均值哈希算法
def aHash(img):
    img = cv2.resize(img, (8, 8))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    np_mean = np.mean(gray)  # 求numpy.ndarray平均值
    ahash_01 = (gray > np_mean) + 0  # 大于平均值=1，否则=0
    ahash_list = ahash_01.reshape(1, -1)[0].tolist()  # 展平->转成列表
    ahash_str = ''.join([str(x) for x in ahash_list])
    return ahash_str


def pHash(img):
    img = cv2.resize(img, (32, 32))  # 默认interpolation=cv2.INTER_CUBIC
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dct = cv2.dct(np.float32(gray))
    dct_roi = dct[0:8, 0:8]  # opencv实现的掩码操作

    avreage = np.mean(dct_roi)
    phash_01 = (dct_roi > avreage) + 0
    phash_list = phash_01.reshape(1, -1)[0].tolist()
    phash_str = ''.join([str(x) for x in phash_list])
    return phash_str


def dHash(img):

    # resize_width = 9
    #
    # resize_height = 8

    # 1. resize to (9,8)
    # try:
    smaller_image = cv2.resize(img, (9, 8))
    gray = cv2.cvtColor(smaller_image, cv2.COLOR_BGR2GRAY)

    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    hash_str0 = []
    for i in range(8):
        hash_str0.append(gray[:, i] > gray[:, i + 1])

    hash_str1 = np.array(hash_str0) + 0
    hash_str2 = hash_str1.T
    hash_str3 = hash_str2.reshape(1, -1)[0].tolist()
    dhash_str = ''.join([str(x) for x in hash_str3])
    return dhash_str
    # except Exception as e:
    #     print(e)


def hammingDist(s1, s2):
    assert len(s1) == len(s2)
    return sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])


# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree

