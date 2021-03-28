# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/11/30 16:00
import cv2
import numpy as np


def imread(image_path):
    try:
        #image = unicode(image_path, "utf-8")
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
        return image
    except IOError:
        print("image_path is error")
        return -1