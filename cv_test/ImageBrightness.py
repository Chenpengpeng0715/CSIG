# -*- coding:utf-8 -*-
# author:
# datetime:2019/10/22 19:23
from PIL import Image, ImageStat
import math
import os
import shutil
import xml.etree.ElementTree as et
from tools_zhongle import unit, perturbance
import cv2
import numpy as np


def main():
    # path = r"E:\测试集\test\test"
    # dest_path = r""
    # li = [[0, 30], [30, 60], [60, 100], [100, 150], [150, 200], [200, 1000]]
    # for n in li:
    # get_pic_light(path, dest_path, n)

    # path = r"E:\测试集\test\test"
    # dest_path = r""
    # li = [[0, 30], [30, 60], [60, 100], [100, 150], [150, 200], [200, 1000]]
    # for n in li:
    #     get_face_light(path, dest_path, n)

    path = r'H:\test\DarkPicDir'
    dest_path = r'H:\test\test'
    b = 1.5
    change_light(path, dest_path, b)

    # path = r"E:\测试集\test\test"
    # dest_path = r"E:\测试集\test\result\result"
    # c = 1
    # b = -10
    # contrast_demo(path, dest_path, c, b)


# 获取图片亮度分布
def get_pic_light(path, dest_path, n):
    list = []
    ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[-1] in ext:
                file_path = os.path.join(root, file)
                light_value = brightness(file_path)
                if int(n[0]) < light_value < int(n[1]):
                    if not os.path.join(dest_path, str(n[0])+"-"+str(n[1])):
                        os.makedirs(os.path.join(dest_path, str(n[0])+"-"+str(n[1])))
                    shutil.copy(file_path, os.path.join(dest_path, str(n[0])+"-"+str(n[1])))
                list.append(int(light_value))
    print(list)


# 获取人脸区域亮度分布
def get_face_light(path, dest_path, n):
    ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
    txt_path = os.path.join(path, "gt_list.txt")
    with open(txt_path, "w") as f:
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[-1] in ext and "crop" not in file and "rotate" not in root:
                    file_path = os.path.join(root, file)
                    # file_path_new = os.path.join(dest_path, str(root.split("\\")[-1]) + "_" + file)
                    file_path_new = os.path.join(dest_path, str(root.split("\\")[-1]) + "_" + file)
                    shutil.copy(file_path, file_path_new)
                    try:
                        img = unit.imread(file_path_new)
                        xml_path = os.path.join(root, os.path.splitext(file)[0] + ".xml")
                        tree = et.parse(xml_path)
                    except:
                        print("error")
                        os.remove(file_path_new)
                        continue
                    roots = tree.getroot()
                    count = 0
                    l = []
                    l.append(file_path_new)
                    for child in roots:
                        for sub in child:
                            if sub.tag == "bndbox":
                                count += 1
                                for i in range(len(sub)):
                                    l.append(str(sub[i].text))
                    l.append(count)
                    if len(l) == 2:
                        f.write(l[1][0] + " ")
                        f.write(l[1][1] + " ")
                        f.write(str(int(l[1][2]) - int(l[1][0])) + " ")
                        f.write(str(int(l[1][3]) - int(l[1][1])) + "\n")
                        x = int(l[1][0])
                        y = int(l[1][1])
                        x1 = int(l[1][2])
                        y1 = int(l[1][3])
                        cropped = img.crop((x, y, x1, y1))
                        face_light_value = brightness(cropped)
                        if int(n[0]) < int(face_light_value) <= int(n[1]):
                            light_path = os.path.join(dest_path, str(n[0] + "--" + str(n[1])))
                            if os.path.exists(light_path):
                                os.makedirs(light_path)
                            shutil.copy(file_path_new, os.path.join(light_path, file))

                    else:
                        d = {}
                        for i in range(1, len(l)):
                            x = int(l[i][2])-int(l[i][0])
                            y = int(l[i][3])-int(l[i][1])
                            p = x * y
                            d[i] = p
                        b = sorted(d.items(), key=lambda item: item[1], reverse=True)
                        for i in range(len(b)):
                            if i == 0:
                                num = int(list(b[0])[0])
                                f.write(l[num][0] + " ")
                                f.write(l[num][1] + " ")
                                f.write(str(int(l[num][2])-int(l[num][0])) + " ")
                                f.write(str(int(l[num][3])-int(l[num][1])) + "\n")
                                # unit.save_image(img1, file_path_new)
                            else:
                                num = int(list(b[i])[0])
                                print("多人脸"+str(num))
                                point = (int(l[num][0]), int(l[num][1]))
                                mask_size = (int(l[num][2])-int(l[num][0]), int(l[num][3])-int(l[num][1]))
                                img1 = perturbance.occlusion(img, point, mask_size)
                                unit.save_image(img1, file_path_new)
                        num = int(list(b[0])[0])
                        x = int(l[num][0])
                        y = int(l[num][1])
                        x1 = int(l[num][2])
                        y1 = int(l[num][3])
                        cropped = img.crop((x, y, x1, y1))
                        face_light_value = brightness(cropped)
                        if int(n[0]) < int(face_light_value) <= int(n[1]):
                            light_path = os.path.join(dest_path, str(n[0] + "--" + str(n[1])))
                            if os.path.exists(light_path):
                                os.makedirs(light_path)
                            shutil.copy(file_path_new, os.path.join(light_path, file))


# 获取感知亮度
def brightness(im_file):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))


# 改变图片亮度和对比度
def contrast_demo(path, dest_path, c, b):  # 亮度就是每个像素所有通道都加上b
    ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[-1] in ext:
                file_path = os.path.join(root, file)
                print(
                    file_path
                )
                # img1 = cv2.imread(file_path, cv2.IMREAD_COLOR)
                img1 = unit.imread(file_path)
                rows, cols, chunnel = img1.shape
                blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
                dst = cv2.addWeighted(img1, c, blank, 1 - c, b)
                new_path = os.path.join(dest_path, str(b)+"_"+file)
                # cv2.imshow("con_bri_demo", dst)
                unit.save_image(dst, new_path)


# 改变图像亮度(变暗)
def change_light(path, dest_path, b):
    # open an image file (.jpg or.png) you have in the working folder
    ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[-1] in ext:
                file_path = os.path.join(root, file)
                im1 = Image.open(file_path)
                # multiply each pixel by 0.9 (makes the image darker)
                # works best with .jpg and .png files, darker < 1.0 < lighter
                # (.bmp and .gif files give goofy results)
                # note that lambda is akin to a one-line function
                im2 = im1.point(lambda p: p * b)
                # brings up the modified image in a viewer, simply saves the image as
                # a bitmap to a temporary file and calls viewer associated with .bmp
                # make certain you have associated an image viewer with this file type
                # im2.show()
                # save modified image to working folder as Audi2.jpg
                im2.save(os.path.join(dest_path, str(b)+"_"+file))


if __name__ == '__main__':
    main()