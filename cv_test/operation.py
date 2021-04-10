# coding: utf-8
# basic image manipulation
import cv2
from math import *
import numpy as np
from scipy.stats import mode



'''
    function: image translate
    input:
        image, cv::mat of source-img;
        x, the distance traveled x;
        y, the distance traveled y;
    output:
        noised_image, cv::mat of image which has been noised
'''

def translate(image, x, y):
    img = image
    mat = np.float32([[1, 0, x], [0, 1, y]])
    img_translate = cv2.warpAffine(img, mat, (img.shape[1], img.shape[0]))
    return img_translate



'''
    function: rotate translate
    input:
        image, cv::mat of source-img;
        angle, 0-360 ,clockwise
        mode, 1: keep size , 2: keep total image
        scale, scaling
    output:
        noised_image, cv::mat of image which has been rotated
'''

def rotate(image, angle, mode=1, scale=1.0):
    img =image
    height, width = img.shape[:2]
    center = (width / 2, height / 2)
    matRotate = cv2.getRotationMatrix2D(center, angle, scale)
    if mode == 1:
        img_rotate = cv2.warpAffine(img, matRotate, (width, height))
    elif mode == 2:
        # cos = np.abs(matRotate[0, 0])
        # sin = np.abs(matRotate[0, 1])
        # new_width = int((height*sin) + (width*cos))
        # new_height = int((height*cos) + (width*sin))
        # matRotate[0, 2] += (new_width) - center[0]
        # matRotate[1, 2] += (new_height) - center[1]
        # img_rotate = cv2.warpAffine(img, matRotate, (new_width, new_height))
        heightNew = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))
        widthNew = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))
        matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        matRotation[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
        matRotation[1, 2] += (heightNew - height) / 2  # 重点在这步
        img_rotate = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
        # borderValue填充颜色
    return img_rotate


# # 旋转图片，图片完整显示，不裁剪
# def Rotate(img, degree):  # degree为旋转角度，比如：90,180,270
#     height, width = img.shape[:2]
#     # 旋转后的尺寸
#     heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
#     widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
#     matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
#     matRotation[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
#     matRotation[1, 2] += (heightNew - height) / 2  # 重点在这步
#     imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
#     return imgRotation


'''
    function: resize image
    input:
        image, cv::mat of source-img;
        width, the width of image after resize
        height, the height of image after resize
        inter,  interpolation method, commend downsampling used cv2.INTER_AREA , upsampling used cv2.INTER_LINEAR
    output:
        resized, cv::mat of image which has been resized
'''

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    img = image
    dim = None
    (h, w) = img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    if height is None:
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=inter)
    # img1 = cv2.resize(img, None, fx=x, fy=x, interpolation=cv2.INTER_CUBIC)  # 放大图像采用INTER_CUBIC
    # img1 = cv2.resize(img, None, fx=x, fy=x, interpolation=cv2.INTER_AREA)  # 缩小图像采用INTER_AREA
    return resized


'''
    function: resize image
    input:
        image, cv::mat of source-img;
        x, cv::mat of image for scaling ratio
    output:
        resized, cv::mat of image which has been resized
'''

def Resize(image, x, mode=1):
    img = image
    if mode == 1:
        resized = cv2.resize(img, None, fx=x, fy=x, interpolation=cv2.INTER_CUBIC)  # 放大图像采用INTER_CUBIC
    if mode == 2:
        resized = cv2.resize(img, None, fx=x, fy=x, interpolation=cv2.INTER_AREA)  # 缩小图像采用INTER_AREA
    return resized



'''
    function: crop the black edge in image
    input:
        image, cv::mat of source-img;
    output:
        crop_img, cv::mat of image which has been cropped the black edge
'''

def crop_black(image):
    img = cv2.copyMakeBorder(image,30,30,30,30,cv2.BORDER_CONSTANT,value=[0,0,0])
    # cv2.imshow("sss",img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    closed_1 = cv2.erode(gray, None, iterations=4)
    closed_1 = cv2.dilate(closed_1, None, iterations=4)
    blurred = cv2.blur(closed_1, (9, 9))
    # get the most frequent pixel
    num = mode(blurred.flat)[0][0] + 1
    # the threshold depends on the mode of your images' pixels
    num = num if num <= 30 else 1
    _, thresh = cv2.threshold(blurred, num, 255, cv2.THRESH_BINARY)

    # you can control the size of kernel according your need.
    kernel = np.ones((13, 13), np.uint8)
    closed_2 = cv2.erode(thresh, kernel, iterations=4)
    closed_2 = cv2.dilate(closed_2, kernel, iterations=4)
    # print cv2.findContours(closed_2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts, _ = cv2.findContours(closed_2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    # draw a bounding box arounded the detected barcode and display the image
    # cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
    # cv2.imshow("Image", img)
    # # cv2.imwrite("pic.jpg", img)
    # cv2.waitKey(0)

    xs = [i[0] for i in box]
    ys = [i[1] for i in box]
    x1 = min(xs)
    x2 = max(xs)
    y1 = min(ys)
    y2 = max(ys)
    height = y2 - y1
    width = x2 - x1
    crop_img = img[y1:y1 + height, x1:x1 + width]
    #
    # cv2.imshow("Image", crop_img)
    # cv2.waitKey(0)
    return crop_img


'''
    function: crop the image 
    input:
        image, cv::mat of source-img;
        X_rate: cutting ratio in X;
        Y_rate: cutting ratio in Y:
    output:
        crop_img, cv::mat of image which has been cropped 
'''
def cut_image(image, X_rate, Y_rate):
    X_rate = int(X_rate*100)
    Y_rate = int(Y_rate*100)
    face = image[image.shape[0] * X_rate/200:image.shape[0]*(1-X_rate)/200, image.shape[1] * Y_rate/200:  image.shape[1] * (1-Y_rate)/200]
    return face
