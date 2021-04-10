# -*- coding:utf-8 -*-
# author:
# datetime:2019/9/4 15:44
import json

# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# print(test_dict)
# print(type(test_dict))
#
# # dumps 将数据转换成字符串
# json_str = json.dumps(test_dict)
# print(json_str)
# print(type(json_str))
#
# # loads: 将字符串转换为字典
# new_dict = json.loads(json_str)
# print(new_dict)
# print(type(new_dict))

# # dump: 将数据写入json文件中
# with open("../config/record.json", "w") as f:
#     json.dump(new_dict, f)
#     print("加载入文件完成...")
#
# load:把文件打开，并把字符串变换为数据类型
with open(r"D:\test\1vn_badcsae_202001_202012\1vn_badcsae_202001_202012\wx_badcase_202001\new\81.0_caf0d60f-2ec4-430f-b3fd-bab59920b999_20200121205929-7046eda0-90a9-49be-a751-5f95f8b4c6a4\serial.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
