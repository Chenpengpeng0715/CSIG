# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/11/19 18:44

from tools_zhongle import unit, datapre
import os
import shutil

img_path = r'G:\人脸检测_人脸二分类器\result_database_test\FaceDetect_Outdoor_SecureCCTV_20201117'
result_path1 = r'D:\UGit\testset\result\FaceDetect_Outdoor_SecureCCTV_20201117_face.result'
result_path2 = r'D:\UGit\testset\result\noface.output'
badcase = r'D:\UGit\testset\facedetect_badcase'


path = r'G:\test\FaceDetect_Outdoor_SecureCCTV_20201117_noface_similar'
ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
l1 = []
for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[-1] in ext:
            l1.append('/data/workspace/testset/FaceDetect_Outdoor_SecureCCTV_20201117_noface/' +
                      root.split('\\')[-1] + '/' + file)

with open(result_path1, 'r') as f1:
    count1 = 0
    count11 = 0
    count1_error = 0
    count11_error = 0
    count3 = 0
    count3_error = 0
    for line in f1.readlines():
        if 'testset' in line:
            count1 += 1
            score = line.strip('\n').split(' ')[-1]
            if score == '0':
                count1_error += 1
                # if not os.path.exists(os.path.join(badcase, 'face_all')):
                #     os.makedirs(os.path.join(badcase, 'face_all'))
                # shutil.copy(line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\'),
                #             os.path.join(badcase, 'face_all', os.path.basename(line.split(' ')[0])))
                # shutil.copy(
                #     line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\').replace('.jpg',
                #                                                                                                '.pts'),
                # os.path.join(badcase, 'face_all',
                # os.path.basename(line.split(' ')[0]).replace('.jpg',
                # '.pts')))

        if 'testset' in line and 'face_202011' not in line:
            count11 += 1
            score = line.strip('\n').split(' ')[-1]
            if score == '0':
                count11_error += 1
                # if not os.path.exists(os.path.join(badcase, 'face_true')):
                #     os.makedirs(os.path.join(badcase, 'face_true'))
                # shutil.copy(line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\'),
                #             os.path.join(badcase, 'face_true', os.path.basename(line.split(' ')[0])))
                # shutil.copy(line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\').replace('.jpg', '.pts'),
                # os.path.join(badcase, 'face_true',
                # os.path.basename(line.split(' ')[0]).replace('.jpg',
                # '.pts')))

with open(result_path2, 'r') as f2:
    count2 = 0
    count2_error = 0
    for line in f2.readlines():
        if 'testset' in line:
            count2 += 1
            score = line.strip('\n').split(' ')[-1]
            if score == '0':
                count2_error += 1
        # if 'testset' in line and line.strip('\n').split(' ')[0] not in l1:
        #     count3 += 1
        #     score = line.strip('\n').split(' ')[-1]
        #     if score == '0':
        #         count3_error += 1
        #     else:
        #         if not os.path.exists(os.path.join(badcase, 'noface3')):
        #             os.makedirs(os.path.join(badcase, 'noface3'))
        #         # if 'badcase_202011' in line or 'badcase20201124' in line:
        #         name = os.path.basename(line.split(' ')[0])
        #         shutil.copy(line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\'),
        #                     os.path.join(badcase, 'noface3', name))
        #         shutil.copy(os.path.splitext(line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\'))[0] + '.pts',
        #                     os.path.join(badcase, 'noface3', os.path.splitext(name)[0] + '.pts'))
                # else:
                #     shutil.copy(line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\').replace('.jpg', '.png'),
                #                 os.path.join(badcase, 'noface1', os.path.basename(line.split(' ')[0])))
                #     shutil.copy(
                #         line.split(' ')[0].replace('/data/workspace/testset', img_path).replace('/', '\\').replace(
                #             '.jpg', '.pts'),
                #         os.path.join(badcase, 'noface1', os.path.basename(line.split(' ')[0]).replace(
                #             '.jpg', '.pts')))
# with open(r'G:\人脸检测_人脸二分类器\result_database_test\FaceDetect_Outdoor_SecureCCTV_20201117\FaceDetect_Outdoor_SecureCCTV_20201117_noface\FaceDetect_Outdoor_SecureCCTV_20201117_noface-all.list', 'r') as f11, open(r'G:\人脸检测_人脸二分类器\result_database_test\FaceDetect_Outdoor_SecureCCTV_20201117\FaceDetect_Outdoor_SecureCCTV_20201117_noface\FaceDetect_Outdoor_SecureCCTV_20201117_noface-all.list', 'w') as f22:



print('真人包含困难照片 ' + str(count1) + " " +
      str(count1_error) + " " + str(count1_error / count1))
print('真人不包含困难照片 ' + str(count11) + " " +
      str(count11_error) + " " + str(count11_error / count11))
print('非真人 ' + str(count2) + " " + str(count2_error) +
      " " + str(count2_error / count2))
# print('非真人 ' + str(count3) + " " + str(count3_error) +
#       " " + str(count3_error / count3))
'''
ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
for root, dirs, files in os.walk(badcase):
    for file in files:
        if os.path.splitext(file)[-1] in ext:
            file_path = os.path.join(root, file)
            pts_path = os.path.splitext(file_path)[0] + '.pts'
            with open(pts_path, 'r') as f:
                lines = f.readlines()
                l = []
                for i in range(len(lines)):
                    q = (lines[i].strip('\n').split(' ')[0], lines[i].strip('\n').split(' ')[1])
                    l.append(q)
                print(l)
                img = unit.imread(file_path)
                img1 = datapre.draw_point(img, l, r=2, color=(0, 0, 255))
                # result_path = str(os.path.splitext(file_path)) + "_5p" + os.path.splitext(file_path)[-1]
                unit.save_image(img1, file_path)
'''
