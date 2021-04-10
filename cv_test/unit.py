# encoding: utf-8
import cv2
import numpy as np
import os


'''
    function: read image
    input:
        image_path, absolute path of the image;
    output:
        image, cv::mat of image 
'''

def imread(image_path):
    try:
        #image = unicode(image_path, "utf-8")
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
        return image
    except IOError:
        print("image_path is error")
        return -1


'''
    function: create directory
    input:
        path, the path to create
    output:
        None
'''

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return
    else:
        return


'''
    function: save image
    input: 
        image, cv::mat of source-img;
        dirpath, target path to save image
    output:
        None
'''
def save_image(image, dirpath):
    #dirpath = unicode(dirpath, "utf-8")
    geshi = dirpath.split('.')[-1:][0]
    ext = ['jpg', 'png', 'bmp', 'jpeg', 'JPEG', 'PNG', 'JPG']
    try:
        if geshi in ext:
            path = os.path.dirname(dirpath)
            mkdir(path)
            if geshi == 'png':
                cv2.imencode('.'+geshi, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])[1].tofile(dirpath)
            else:
                cv2.imencode('.' + geshi, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])[1].tofile(dirpath)
    except:
        print("save false")
        return -1


'''
    function: create a list of files containing multiple directories
    input: 
        path, the path of parent directory;
        filename, the filename of list result;
        withLabel, default 'False'. If label is 'True', and the name of the directory where the image is located will be label of the image
                    ext, the file type to retrieve;
        ext, the file type to retrieve
    output:
        filelist
'''

def makeFileLists(path, fileName='list.txt', withLabel=False, ext=['jpg', 'bmp', 'png']):
    if not os.path.exists(path):
        print (path, 'IS NOT EXIST, PLEASE CHECK IT!')

    elif os.path.isdir(path):
        subPath = os.listdir(path)
        # subPath.sort(key=lambda x: int(x[:-6]))
        subPath = [os.path.join(path, path) for path in subPath]
        for path in subPath:
            makeFileLists(path, fileName, withLabel)
    else:
        if path[-3:] in ext:
            f = open(fileName, 'a')
            if withLabel:
                line = path + ' ' + (path.split('/'))[-2] + '\n'
            else:
                line = path + '\n'
            f.writelines(line)
            f.close()


def video_extract(video_path, interval, target_path):
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = file_name
        pic_path = os.path.join(target_path, folder_name)
        try:
            os.makedirs(pic_path)
        except:
            None
        vc = cv2.VideoCapture(os.path.join(video_path, video_name))
        c = 1
        k = 0
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            rval, frame = vc.read()
            if (c % interval == 0):
                k += 1
                cv2.imwrite(os.path.join(pic_path, str(file_name) + '_' + str(k) + '.jpg'), frame)
                print(os.path.join(pic_path, str(file_name) + '_' + str(k) + '.jpg'))
            c = c + 1
            cv2.waitKey(1)
        vc.release()
    return