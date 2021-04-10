# coding: utf-8
# Create disturbing images
import cv2
import numpy as np


'''
    function: add noise point to image
    input:
        image, cv::mat of source-img;
        degree, degree of noise;
    output:
        noised_image, cv::mat of image which has been noised
'''

def gaussian_noise(image, degree=None):
    row, col, ch = image.shape
    mean = 0
    if not degree:
        var = np.random.uniform(0.004, 0.01)
    else:
        var = degree
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    cv2.normalize(noisy, noisy, 0, 255, norm_type=cv2.NORM_MINMAX)
    noisy_image = np.array(noisy, dtype=np.uint8)
    return noisy_image



'''
    function: add unfocused blur to image
    input:
        image, cv::mat of source-img;
        degree, degree of blur, must be an odd number;
    output:
        noised_image, cv::mat of image which has been blurred
'''

def duijiao_blur(image, degree=5):
    duijiao_image = cv2.GaussianBlur(image, ksize=(degree, degree), sigmaX=0, sigmaY=0)
    return duijiao_image


'''
    function: add motion blur to image
    input:
        image, cv::mat of source-img;
        degree, degree of blur, recommend beyond 20;
        angle, relative motion angle, 0-360
    output:
        noised_image, cv::mat of image which has been blurred
'''

def motion_blur(image, degree=20, angle=45):
    img = np.array(image)
    M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
    motion_blur_kernel = np.diag(np.ones(degree))
    motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))
    motion_blur_kernel = motion_blur_kernel / degree
    # blurred = cv2.filter2D(img, -1, motion_blur_kernel)
    # convert to uint8
    blurred = cv2.filter2D(img, -1, motion_blur_kernel)
    cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
    motion_image = np.array(blurred, dtype=np.uint8)
    return motion_image


'''
    function: change the light of image
    input:
        image, cv::mat of source-img;
        degree, degree of light, 0-1 is lighter , 1-n is darker;
    output:
        noised_image, cv::mat of image which has been changed light
'''

def light_image(image, degree=1):
    img = np.array(image)
    I_max = np.max(img)
    mean = img/float(np.max(img))
    l_image = np.power(mean, degree)
    l_image = l_image*I_max
    return l_image


'''
    function: create mask on image
    input:
        image, cv::mat of source-img;
        point, (x,y) upper-left coordinate of region
        mask_size (width,height) size of mask area  
    output:
        noised_image, cv::mat of image which has been added mask
'''

def occlusion(image, point, mask_size):
    # mask1 = np.zeros(img.shape, dtype=np.uint8)
    # mask = np.zeros(img.shape,dtype=np.uint8)
    image[point[1]:point[1]+mask_size[1], point[0]:point[0]+mask_size[0]] = 0
    occlusion_image = image
    # mask_inv = cv2.bitwise_not(mask)
    # img1 = cv2.bitwise_and(mask,mask,mask=mask_inv)
    #
    # cv2.imshow("mask", img)
    # cv2.waitKey()
    return occlusion_image
