# -*- coding:utf-8 -*-
import os
import xml.etree.ElementTree as et
from tools_zhongle import unit
import random

min_pixel_threshold = 128
scale = 2  # set to 1 if not to scale

def main():
    # data path
    path = r"C:\Users\rayegao\Desktop\data_scale2\train_data" 

    # clean up 
    cleanup(path)

    # retrieve face gt information from xml and write it to txt
    xml2txt(path)

    # 扣人脸与非人脸
    square_box = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # to find the full-view image:
            if ".txt" not in file and "crop" not in file and ".xml" not in file and "face" not in file and ".gt" not in file and "DS_Store" not in file and "draw" not in file:
                # full image path
                file_path = os.path.join(root, file)
                txt_path = os.path.splitext(file_path)[0] + ".txt"
                try:
                    with open(txt_path, "r") as f:
                        # txt为分行的情况
                        rect_list = []
                        lines = f.readlines()
                        for line in lines:
                            line = line.strip('\n')
                            rect_list.append(line)
                            rects = [rect_list[i:i + 4] for i in range(0, len(rect_list), 4)]
                        for i in range(len(rects)):
                            print("start")
                            print(i)
                            print(len(rects))
                            # crop face images
                            square_box = crop(file_path, rects[i], rects, i)
                            print("square box:")
                            print(square_box)
                            print("..........................")
                            # crop noface images
                            crop_noface(file_path, square_box, rects, i)
                except:
                    # print("here is an exception")
                    continue

def cleanup(path):
    print("The path to dst folder: %s, cleanup begins ..." %(path))
    for root, dirs, files in os.walk(path):
        for file in files:
            if ".txt" in file or "face" in file or "crop" in file:
                file_full_path = os.path.join(root, file)
                os.remove(file_full_path)
    print("Cleanup Finished!")

def xml2txt(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if ".xml" in file:
                xml_path = os.path.join(root, file)
                txt_path = xml_path.replace(".xml", ".txt")
                try:
                    with open(txt_path, "w") as f:
                        tree = et.parse(xml_path)
                        roots = tree.getroot()
                        for child in roots:
                            for sub in child:
                                if sub.tag == "bndbox":
                                    for a in sub:
                                        # print(a.text)
                                        f.write(a.text + "\n")
                except:
                    continue


# args list:
# image: full image path
# rect: 4-element list [left-top-x, left-top-y, right-bottom-x, right-bottom-y] 
# file_path: full image path
# ls: rect list
# q: # of rect in rect list
def crop(image_path, rect, rects, num):
    # read full image
    img = unit.imread(image_path)

    # square box (gt_left_top_y, gt_left_top_x, edge)
    square = []

    # get face image shape
    gt_left_top_y = int(rect[0])
    gt_left_top_x = int(rect[1])
    gt_width = int(rect[2]) - int(gt_left_top_x)
    gt_height = int(rect[3]) - int(gt_left_top_y)

    # get a square (with side = the longer edge) from the gt-rectangular
    if gt_width > gt_height:
        # change to a square
        gt_height = int(gt_width)
        # relocate the left-top corner
        diff = int((gt_width - gt_height) / 2)
        if (gt_left_top_y > diff) or (gt_left_top_y == diff):
            gt_left_top_y = int(gt_left_top_y - diff)
        else:
            gt_left_top_y = 0
        # scale or not
        if scale > 1:
            gt_left_top_y = gt_left_top_y - int(gt_height / 2)
            if gt_left_top_y < 0:
                gt_left_top_y = 0
            gt_left_top_x = gt_left_top_x - int(gt_width / 2)
            if gt_left_top_x < 0:
                gt_left_top_x = 0
            gt_height = int(gt_height * scale)
            gt_width = int(gt_width * scale)
        # get the cropped img
        cropped_img = img[gt_left_top_y:(gt_left_top_y + gt_height), gt_left_top_x:(gt_left_top_x + gt_width)]
        # save the #num cropped face image
        dir_path = os.path.splitext(image_path)[0] + "_face_" + str(num) + os.path.splitext(image_path)[-1]
        print("is there a square: ")
        print(dir_path)
        unit.save_image(cropped_img, dir_path)
        # save and return    
        square.append(gt_left_top_y)
        square.append(gt_left_top_x)
        square.append(gt_height)
        print(square)
        return square
    elif gt_width < gt_height:
        # change to a square
        gt_width = int(gt_height)
        # relocate the left-top corner
        diff = int((gt_height - gt_width) / 2)
        if (gt_left_top_x > diff) or (gt_left_top_x == diff):
            gt_left_top_x = int(gt_left_top_x - diff)
        else:
            gt_left_top_x = 0
        # scale or not
        if scale > 1:
            gt_left_top_y = gt_left_top_y - int(gt_height / 2)
            if gt_left_top_y < 0:
                gt_left_top_y = 0
            gt_left_top_x = gt_left_top_x - int(gt_width / 2)
            if gt_left_top_x < 0:
                gt_left_top_x = 0
            gt_height = int(gt_height * scale)
            gt_width = int(gt_width * scale)
        # get the cropped img
        cropped_img = img[gt_left_top_y:(gt_left_top_y + gt_height), gt_left_top_x:(gt_left_top_x + gt_width)]
        # save the #num cropped face image
        dir_path = os.path.splitext(image_path)[0] + "_face_" + str(num) + os.path.splitext(image_path)[-1]
        print("is there a square: ")
        print(dir_path)
        unit.save_image(cropped_img, dir_path)
        # save and return    
        square.append(gt_left_top_y)
        square.append(gt_left_top_x)
        square.append(gt_height)
        print(square)
        return square
    else:
        # scale or not
        if scale > 1:
            gt_left_top_y = gt_left_top_y - int(gt_height / 2)
            if gt_left_top_y < 0:
                gt_left_top_y = 0
            gt_left_top_x = gt_left_top_x - int(gt_width / 2)
            if gt_left_top_x < 0:
                gt_left_top_x = 0
            gt_height = int(gt_height * scale)
            gt_width = int(gt_width * scale)
        # get the cropped img
        cropped_img = img[gt_left_top_y:(gt_left_top_y + gt_height), gt_left_top_x:(gt_left_top_x + gt_width)]
        # save the #num cropped face image
        dir_path = os.path.splitext(image_path)[0] + "_face_" + str(num) + os.path.splitext(image_path)[-1]
        print("is there a square: ")
        print(dir_path)
        unit.save_image(cropped_img, dir_path)
        # save and return  
        square.append(gt_left_top_y)
        square.append(gt_left_top_x)
        square.append(gt_height)
        print(square)
        return square

# args list:
# image: full image path
# rect: 4-element list [left-top-x, left-top-y, right-bottom-x, right-bottom-y] 
# file_path: full image path
# ls: rect list
# q: # of rect in rect list
def crop_noface(image_path, square_box, rects, num):

    print("begin to crop noface ")
    # read full image
    img = unit.imread(image_path)

    # read the square box
    left_top_y = square_box[0] 
    left_top_x = square_box[1] 
    edge = square_box[2]

    print("read in the square box")
    print(left_top_y, left_top_x, edge)

    # get full image shape
    sp = img.shape
    y_max = sp[0]
    x_max = sp[1]

    # save all noface image information: (left_top_x, left_top_y, edge, noface_image_path)
    noface_image = []
    noface_image_list = []

    try:
        for crop_left in range(3):
            if left_top_x > min_pixel_threshold:
                dir_path = os.path.splitext(image_path)[0] + "_noface_left_" + str(num) + "_" + str(crop_left) + os.path.splitext(image_path)[-1]
                # obtain the top left corner's coordinates
                x = random.randint(0, left_top_x - min_pixel_threshold)
                y = random.randint(0, y_max - min_pixel_threshold)
                # obtain edge's maximum value
                x_range = left_top_x - x
                y_range = y_max - y
                if x_range < y_range:
                    edge_max = x_range
                else:
                    edge_max = y_range
                if min_pixel_threshold < edge_max < 300:
                    # save a noface image locally
                    edge = random.randint(min_pixel_threshold, edge_max)
                    noface_img = img[y: (y + edge), x: (x + edge)]
                    unit.save_image(noface_img, dir_path)
                    # save a noface image and info to results list
                    noface_image.append(x)
                    noface_image.append(y)
                    noface_image.append(edge)
                    noface_image.append(dir_path)
                    noface_image_list.append(noface_image)
        for crop_top in range(3):
            if left_top_y > min_pixel_threshold:
                dir_path = os.path.splitext(image_path)[0] + "_noface_top_" + str(num) + "_" + str(crop_top) + os.path.splitext(image_path)[-1]
                # obtain the top left corner's coordinates
                x = random.randint(0, x_max - min_pixel_threshold)
                y = random.randint(0, left_top_y - min_pixel_threshold)
                # obtain edge's maximum value
                x_range = x_max - x
                y_range = left_top_y - y
                if y_range < x_range:
                    edge_max = y_range
                else:
                    edge_max = x_range
                if min_pixel_threshold < edge_max < 300:
                    # save a noface image locally
                    edge = random.randint(min_pixel_threshold, edge_max)
                    noface_img = img[y: (y + edge), x: (x + edge)]
                    unit.save_image(noface_img, dir_path)
                    # save a noface image and info to results list
                    noface_image.append(x)
                    noface_image.append(y)
                    noface_image.append(edge)
                    noface_image.append(dir_path)
                    noface_image_list.append(noface_image)
        for crop_right in range(3):
            if (x_max - (left_top_x + edge)) > min_pixel_threshold:
                dir_path = os.path.splitext(image_path)[0] + "_noface_right_" + str(num) + "_" + str(crop_right) + os.path.splitext(image_path)[-1]
                # obtain the top left corner's coordinates
                x = random.randint((left_top_x + edge), (x_max - min_pixel_threshold))
                y = random.randint(0, (y_max - min_pixel_threshold))
                # obtain edge's maximum value
                x_range = x_max - x
                y_range = y_max - y
                if x_range < y_range:
                    edge_max = x_range
                else:
                    edge_max = y_range
                if min_pixel_threshold < edge_max < 300:
                    # save a noface image locally
                    edge = random.randint(min_pixel_threshold, edge_max)
                    noface_img = img[y: (y + edge), x: (x + edge)]
                    unit.save_image(noface_img, dir_path)
                    # save a noface image and info to results list
                    noface_image.append(x)
                    noface_image.append(y)
                    noface_image.append(edge)
                    noface_image.append(dir_path)
                    noface_image_list.append(noface_image)
        for crop_bottom in range(3):
            if (y_max - (left_top_y + edge)) > min_pixel_threshold:
                dir_path = os.path.splitext(image_path)[0] + "_noface_bottom_" + str(num) + "_" + str(crop_bottom) + os.path.splitext(image_path)[-1]
                # obtain the top left corner's coordinates
                x = random.randint(0, x_max - min_pixel_threshold)
                y = random.randint((left_top_y + edge), y_max - min_pixel_threshold)
                # obtain edge's maximum value
                x_range = x_max - x
                y_range = y_max - y
                if y_range < x_range:
                    edge_max = y_range
                else:
                    edge_max = x_range
                if min_pixel_threshold < edge_max < 300:
                    # save a noface image locally
                    edge = random.randint(min_pixel_threshold, edge_max)
                    noface_img = img[y: (y + edge), x: (x + edge)]
                    unit.save_image(noface_img, dir_path)
                    # save a noface image and info to results list
                    noface_image.append(x)
                    noface_image.append(y)
                    noface_image.append(edge)
                    noface_image.append(dir_path)
                    noface_image_list.append(noface_image)
    except:
        print("exception happens")

    err_element = []
    error = []
    # check overlaps between noface images and remove ones with overlap > 0.3
    for i in range(len(noface_image_list)-1):
        if i not in err_element: 
            for j in range(i+1, len(noface_image_list)):
                x1 = noface_image_list[i][0]
                y1 = noface_image_list[i][1]
                edge1 = noface_image_list[i][2]
                x2 = noface_image_list[j][0]
                y2 = noface_image_list[j][1]
                edge2 = noface_image_list[j][2]
                d_path_j = noface_image_list[j][3]
                # case 0: no overlap 
                if (x1 > x2 + edge2) or (x1 == x2 + edge2) or (x1 + edge1 < x2) or (x1 + edge1 == x2):
                    continue
                if (y1 > y2 + edge2) or (y1 == y2 + edge2) or (y1 + edge1 < y2) or (y1 + edge1 == y2):
                    continue
                # case 1: has overlap
                colInt = abs(min(x1 + edge1, x2 + edge2) - max(x1, x2))
                rowInt = abs(min(y1 + edge1, y2 + edge2) - max(y1, y2))
                overlap_area = colInt * rowInt
                area1 = edge1 * edge1
                area2 = edge2 * edge2
                if area1 < area2:
                    overlap_ratio = overlap_area / area1
                    try:
                        if overlap_ratio > 0.3:
                            error.append(d_path_j)
                            err_element.append(j)
                            os.remove(d_path_j)
                    except Exception:
                        #print("ops, exception happens")
                        #print(Exception)
                        continue
                else:
                    overlap_ratio = overlap_area / area2
                    try:
                        if overlap_ratio > 0.3:
                            error.append(d_path_j)
                            err_element.append(j)
                            os.remove(d_path_j)
                    except Exception:
                        #print("ops, exception happened")
                        #print(Exception)
                        continue

    # check overlaps between noface images and all face images, and remove if overlap exists 
    try:
        for i in range(len(noface_image_list)):
            if i not in err_element: 
                for j in range((len(rects))):
                    d_path_i = noface_image_list[i][3]
                    x1 = noface_image_list[i][0]
                    y1 = noface_image_list[i][1]
                    edge1 = noface_image_list[i][2]
                    x2 = int(rects[j][0])
                    y2 = int(rects[j][1])
                    w2 = int(rects[j][2]) - x2
                    h2 = int(rects[j][3]) - y2
                    if (x1 > x2 + w2) or (x1 == x2 + w2) or (x1 + edge1 < x2) or (x1 + edge1 == x2):
                        continue
                    elif (y1 > y2 + h2) or (y1 == y2 + h2) or (y1 + edge1 < y2) or (y1 + edge1 == y2):
                        continue
                    else:
                        try:
                            os.remove(d_path_i)
                            error.append(d_path_i)
                        except Exception:
                            #print("ops, caught an exception")
                            continue
    except Exception as e:
        #print("hmm:")
        print(repr(e))


if __name__ == '__main__':
    main()