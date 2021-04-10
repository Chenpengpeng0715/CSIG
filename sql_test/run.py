#!/user/bin/env python
# coding=utf-8

# @project : project_tools
# @author  : kalifun
# @file   : run.py
# @ide    : PyCharm
# @time   : 2020/6/12 11:14

import os
import xlwt
import pymysql
import csv


conn = pymysql.connect(
    host="9.134.2.181",
    port=3306,
    user="root",
    password="",
    database="abtest",
    charset="utf8")
cursor = conn.cursor()


def save_file(filepath, task):
    # save_sql = "select url_id, uniq_attribute_name, url_a, attribute_evaluate_result,count(*) into outfile '%s' fields terminated by ',' from view_last_info_record where evaluate_id=%s group by url_id,uniq_attribute_name, url_a, attribute_evaluate_result order by url_id" % (path, task)
    # save_sql = "select url_id, uniq_attribute_name, url_a, attribute_evaluate_result,count(*) from view_last_info_record where evaluate_id=%s group by url_id,uniq_attribute_name, url_a, attribute_evaluate_result order by url_id" % (
    #     task)

    save_sql = 'select * from view_last_info_record where evaluate_id=%s' % task
    # cursor.execute(sql)
    # results = cursor.fetchall()
    # for row in results:
    #     print(row)

    print(save_sql)
    result_list = []
    try:
        # 执行SQL语句
        cursor.execute(save_sql)
        results = cursor.fetchall()

        for row in results:
            line = []
            url_id = str(row[0])
            uniq_attribute_name = str(row[1]).replace("是否同人", 'same or no')
            url_a = str(row[2]).replace('"', '')
            attribute_evaluate_result = str(row[3])
            count = str(row[4])
            line.append(url_id)
            line.append(uniq_attribute_name)
            line.append(url_a)
            line.append(attribute_evaluate_result)
            line.append(count)
            result_list.append(line)
        # 提交到数据库执行
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    # write_excel_xls(filepath, result_list)
    write_csv(filepath, result_list)


def write_csv(filepath, value):
    with open(filepath, 'w', newline='') as fi:
        csv_write = csv.writer(fi)
        for i in value:
            csv_write.writerow(i)


def write_excel_xls(filepath, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet("sheet")  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(filepath)  # 保存工作簿
    print("xls格式表格写入数据成功！")


if __name__ == '__main__':
    now_path = r'D:\faceid\abtest\result'
    task_list = [541, 542]
    for task in task_list:
        filename = "test_" + str(task) + ".csv"
        filepath = os.path.join(now_path, filename)
        save_file(filepath, task)
    conn.close()
