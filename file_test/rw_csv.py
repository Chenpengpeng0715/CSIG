# -*- coding:utf-8 -*-
# author:
# datetime:2019/9/4 15:51
import csv


# 写csv
def write_csv(csv_path, l_list):
    with open(csv_path, 'w', newline='') as fi:
        csv_write = csv.writer(fi)
        csv_write.writerow(l_list)


# 读csv
def read_csv(csv_path):
    with open(csv_path, 'r', newline='') as fr:
        reader = csv.reader(fr)
        return reader
        # result = {}
        # for item in reader:
        #     # 忽略第一行
        #     if reader.line_num == 1:
        #         continue
        #     result[item[0]] = item[1]