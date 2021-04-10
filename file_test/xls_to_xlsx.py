# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/12/11 14:16
import os
import win32com.client as win32


def test_script(curr_path):
    # curr_path = r'G:\社区误检\误检器上线后误检数据\badcase'
    # for i in l:
    #     path = os.path.join(curr_path, i)
    for root, dirs, files in os.walk(curr_path):
        for file in files:
            if os.path.splitext(file)[-1] == '.xls':
                fname = os.path.join(root, file)
                excel = win32.DispatchEx('Excel.Application')
                wb = excel.Workbooks.Open(fname)
                wb.SaveAs(fname + "x", FileFormat=51)  # FileFormat = 51 is for .xlsx extension
                wb.Close()  # FileFormat = 56 is for .xls extension
                excel.Application.Quit()
                print(fname + "x")

