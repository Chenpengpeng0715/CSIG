# encoding: utf-8
# data set preparation assistance
import cv2
import numpy as np
import os
from tools_zhongle import unit, operation, perturbance
import math
import random
import shutil
from pypinyin import lazy_pinyin, Style
from PIL import ImageFont, ImageDraw, Image

'''
    function: replace the Chinese word in name
    input:
        image_path, str ,absolute path of the image
        dictpath , str , absolute path to the dictionary
    output:
        imagename, str , imagename which replaced word in dictionary
'''


def replace_Chinese(image_path, dictpath):
    content = {}
    with open(dictpath) as f:
        for a in f:
            k = a.strip('\r\n').split(' ')
            content[k[0]] = k[1]
    # imagename = unicode(imagename,'utf-8')
    for key, value in content.items():
        imagename = image_path.replace(key, value)
    return imagename


def rename_pinyin(testset_dir):
    for root, dirs, files in os.walk(testset_dir):
        for file in files:
            old_file_path = os.path.join(root, file)
            style = Style.NORMAL
            new_file = ''.join(lazy_pinyin(file, style=style))
            new_file_path = os.path.join(root, new_file)
            print(old_file_path)
            print(new_file_path)
            shutil.move(old_file_path, new_file_path)


'''
    function: replace the Chinese word in name
    input:
        image_path, str ,absolute path of the image
        threshold, above the threshold will be compressed, byte
        quality, the quality of image after compress , 0-100
        dirpath, target path to save the compressed image
    output:
        None
'''


def compress(image_path, threshold, quality, dirpath):
    img = unit.imread(image_path)
    filesize = os.path.getsize(image_path)
    geshi = dirpath.strip('\r\n').split('.')[-1:][0]
    if filesize >= threshold:
        if geshi == 'jpg':
            yasuo_image = cv2.imencode(
                '.' + geshi, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])[1]
        elif geshi == 'png':
            print("png format compression degree is limited, if the size still does not meet the requirements, please convert the image to jpg")
            degree = int(10 - (quality / 10))
            yasuo_image = cv2.imencode(
                '.' + geshi, img, [int(cv2.IMWRITE_PNG_COMPRESSION), degree])[1]
        yasuo_image.tofile(dirpath)
    return


'''
    function: crop a face in image by rect information
    input:
        image, cv::mat of source-img;
        rect, list[left,top,width,height] of rect information;
    output:
        img_crop, cv::mat of image has been crop face area;
'''


def crop(image, rect):
    img = image
    left = int(rect[0])
    top = int(rect[1])
    width = int(rect[2])
    height = int(rect[3])
    # [y0:y1, x0:x1]
    img_crop = img[top:top + height, left:left + width]
    return img_crop


def crop1(image, rect):
    img = image
    left = float(rect[0])
    top = float(rect[1])
    width = float(rect[2])
    height = float(rect[3])
    # [y0:y1, x0:x1]
    img_crop = img[top:top + height, left:left + width]
    return img_crop


'''
    坐标为负数时，可添加黑边裁剪
    function: crop a face in image by rect information
    input:
        image, cv::mat of source-img;
        rect, list[left,top,width,height] of rect information;
    output:
        img_crop, cv::mat of image has been crop face area;
'''


def crop_all(image, rect):
    top, bottom, left, right = (0, 0, 0, 0)
    x = int(rect[0])
    y = int(rect[1])
    width = int(rect[2])
    height = int(rect[3])
    if x < 0:
        left += int(abs(x))
        x = 0
    if y < 0:
        top += int(abs(y))
        y = 0
    # RGB颜色
    BLACK = [0, 0, 0]
    # 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(
        image,
        top,
        bottom,
        left,
        right,
        cv2.BORDER_CONSTANT,
        value=BLACK)
    l = [x, y, width, height]
    crop_image = crop(constant, l)
    return crop_image


'''
    function: get the correct face image by face five points information
    input:
        image, cv::mat of source-img;
        five_point, list[(x1,y1),(x2,y2),...] of face five points information;
    output:
        img_crop, cv::mat of image has been rotate front;
'''


def face_rotate(image, five_point):
    img = image
    left_eye = five_point[0].split(' ')
    right_eye = five_point[1].split(' ')
    # get the direction
    # print left_eye[0],right_eye[0]
    eye_direction = (
        float(
            right_eye[0]) -
        float(
            left_eye[0]),
        float(
            right_eye[1]) -
        float(
            left_eye[1]))
    # calc rotation angle in radians
    rotation_x = math.atan2(
        float(
            eye_direction[1]), float(
            eye_direction[0])) * 180 / 3.14
    # print rotation_x
    img_rotate = operation.rotate(img, rotation_x)
    return img_rotate


'''
    function: draw point on the face image
    input:
        image, cv::mat of source-img;
        point_list, list[(x1,y1),(x2,y2),...] of face points information you want to draw;
        r, radius of draw point;
        color, color of draw point;
    output:
        img_point, cv::mat of image has been drawn points;
'''


def draw_point(image, point_list, r=3, color=(0, 255, 0)):
    for point in point_list:
        img_point = cv2.circle(
            image, (int(
                float(
                    point[0])), int(
                float(
                    point[1]))), r, color, -1, cv2.LINE_AA)
    return img_point


'''
    function: draw rect on the face image
    input:
        image, cv::mat of source-img;
        rect, list[left,top,width,height] of face rect information;
        r, radius of draw rect;
        color, color of draw rect;
    output:
        img_rect, cv::mat of image has been drawn rect;
'''


def draw_rect(image, rect, r=5, color=(0, 0, 255)):
    left = int(rect[0])
    top = int(rect[1])
    width = int(rect[2])
    height = int(rect[3])
    right = left + width
    down = top + height
    image_rect = cv2.rectangle(image, (left, top), (right, down), color, r)
    return image_rect


def video_cut():
    return


'''
    function: extract file from folder proportionally (copy)
    input:
        path, folder path
        rate, extract rate ,mode=1  rate [1,n], at equal intervals; mode=2, rate(0,1] ,random
        target_path, target folder path
        mode, mode=1 at equal intervals ; mode=2 random extract
    output:
        None
'''


def extract_image(path, rate, target_path, mode=1):
    # fileDir = unicode(path, 'utf-8')
    fileDir = path.unicode('utf-8')
    pathDir = os.listdir(fileDir)
    filenumber = len(pathDir)
    if mode == 1 and rate >= 1:
        rate = int(rate)
        sample = []
        for i, name in enumerate(pathDir):
            if i % rate == 0:
                sample.append(name)
    if mode == 2 and rate < 1:
        picknumber = int(filenumber * rate)
        sample = random.sample(pathDir, picknumber)
    for name in sample:
        shutil.copy(fileDir + '/' + name, target_path + '/' + name)
    return


def image_add_text(img_path, text, rects, text_color=(255, 0, 0), text_size=100):
    # 设置字体地址，可以网上下载
    font_path = r'D:\faceid\font\simsun.ttc'
    img = Image.open(img_path)
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # print(rects)
    for i in range(len(rects)):
        # print(rects[i])
        draw.rectangle([rects[i][0], rects[i][3]], outline=(255, 0, 0), width=4)
        # 字体的格式 这里的SimHei.ttf需要有这个字体
        fontStyle = ImageFont.truetype(font_path, text_size, encoding="utf-8")
        # 绘制文本
        left = rects[i][0][0]
        top = rects[i][0][1]-40
        draw.text((left, top), text[i], text_color, font=fontStyle)
    return img
