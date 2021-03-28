# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2021/3/10 10:58
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog
import sys
import json
from PyQt5.QtCore import Qt
from script.pyqt_5.test.untitled_new_old import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 0
        # self.pushButton.clicked.connect(self.showDialog)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.next)
        # self.pushButton_4.clicked.connect(self.skip)
        self.pushButton_5.clicked.connect(self.save)

        self.checkBox_6.stateChanged.connect(self.btnstate)
        self.checkBox_7.stateChanged.connect(self.btnstate)
        self.checkBox_8.stateChanged.connect(self.btnstate)
        self.checkBox_9.stateChanged.connect(self.btnstate)
        self.checkBox_10.stateChanged.connect(self.btnstate)
        self.checkBox_11.stateChanged.connect(self.btnstate)
        self.checkBox_12.stateChanged.connect(self.btnstate)
        self.checkBox_14.stateChanged.connect(self.btnstate)
        self.checkBox_15.stateChanged.connect(self.btnstate)
        self.checkBox_16.stateChanged.connect(self.btnstate)
        self.checkBox_17.stateChanged.connect(self.btnstate)
        self.checkBox_18.stateChanged.connect(self.btnstate)
        self.checkBox_19.stateChanged.connect(self.btnstate)
        self.checkBox_20.stateChanged.connect(self.btnstate)
        self.checkBox_21.stateChanged.connect(self.btnstate)
        self.checkBox_22.stateChanged.connect(self.btnstate)
        self.checkBox_23.stateChanged.connect(self.btnstate)
        self.checkBox_24.stateChanged.connect(self.btnstate)
        self.checkBox_26.stateChanged.connect(self.btnstate)
        self.checkBox_27.stateChanged.connect(self.btnstate)
        self.checkBox_28.stateChanged.connect(self.btnstate)
        self.checkBox_30.stateChanged.connect(self.btnstate)
        self.checkBox_31.stateChanged.connect(self.btnstate)
        self.checkBox_32.stateChanged.connect(self.btnstate)
        self.checkBox.stateChanged.connect(self.btnstate)
        self.checkBox_2.stateChanged.connect(self.btnstate)
        self.checkBox_3.stateChanged.connect(self.btnstate)
        self.progressBar.setMinimum(0)
        self.lineEdit.setPlaceholderText("抓拍照")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        # self.lineEdit.setFocus(True)
        self.lineEdit_2.setPlaceholderText("1vn底图")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        # self.lineEdit_3.setPlaceholderText("                                 1v1底图")
        # self.dir_path = os.path.abspath(os.path.dirname(__file__))
        self.dir_path = r'D:\test\1vn_badcsae_202001_202012\1vn_badcsae_202001_202012_history'
        # print(dir_path)
        img_serial_path = os.path.join(self.dir_path, 'serial.list')
        # img_1v1_path = os.path.join(self.dir_path, '1v1.list')
        img_1vn_path = os.path.join(self.dir_path, '1vn.list')
        # print(img_1vn_path)
        with open(img_serial_path, 'r') as f1, open(img_1vn_path, 'r') as f3:
            self.lines_serial = f1.readlines()
            # self.lines_1v1 = f2.readlines()
            self.lines_1vn = f3.readlines()
            img_serial = os.path.join(
                self.dir_path,
                self.lines_serial[0].strip('\n'))
            # img_1v1 = os.path.join(
            #     self.dir_path,
            #     self.lines_1v1[0].strip('\n'))
            img_1vn = os.path.join(
                self.dir_path,
                self.lines_1vn[0].strip('\n'))
            for serial in self.lines_serial:
                self.textEdit.append(serial.strip('\n'))
            self.textEdit_2.append(img_serial)
            self.textEdit_2.append(img_1vn)
            # self.textEdit_2.append(img_1v1)
            self.textEdit_2.append(
                '------------------------------------------------')
            # print(img_serial, img_1v1, img_1vn)
            self.label.setPixmap(QPixmap(img_serial))
            self.label.setScaledContents(True)
            self.label_2.setPixmap(QPixmap(img_1vn))
            self.label_2.setScaledContents(True)
            # self.label_3.setPixmap(QPixmap(img_1v1))
            # self.label_3.setScaledContents(True)
            self.num = len(self.lines_serial)
            self.lineEdit_5.setPlaceholderText('badcase总数：' + str(self.num))
            self.lineEdit_4.setPlaceholderText('已完成数：' + str(self.count))
            self.lineEdit_5.setAlignment(Qt.AlignCenter)
            self.lineEdit_4.setReadOnly(True)
            self.lineEdit_5.setReadOnly(True)
            self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.progressBar.setMaximum(self.num)
        # return len(lines)

    def next(self):
        if self.count < self.num:

            self.checkBox_6.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_9.setChecked(False)
            self.checkBox_10.setChecked(False)
            self.checkBox_11.setChecked(False)
            self.checkBox_12.setChecked(False)
            self.checkBox_14.setChecked(False)
            self.checkBox_15.setChecked(False)
            self.checkBox_16.setChecked(False)
            self.checkBox_17.setChecked(False)
            self.checkBox_18.setChecked(False)
            self.checkBox_19.setChecked(False)
            self.checkBox_20.setChecked(False)
            self.checkBox_21.setChecked(False)
            self.checkBox_22.setChecked(False)
            self.checkBox_23.setChecked(False)
            self.checkBox_24.setChecked(False)
            self.checkBox_26.setChecked(False)
            self.checkBox_27.setChecked(False)
            self.checkBox_28.setChecked(False)
            self.checkBox_30.setChecked(False)
            self.checkBox_31.setChecked(False)
            self.checkBox_32.setChecked(False)
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            img_serial = os.path.join(self.dir_path,
                                      self.lines_serial[self.count].strip('\n'))
            # with open(os.path.dirname(img_serial) + '.result', 'w') as f:
            result_dict = {}
            result_path = os.path.join(os.path.dirname(img_serial), 'serial.json')
            if not os.path.isfile(result_path):
                QMessageBox.warning(
                    self,
                    "warning",
                    "此case结果未保存！！",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes)
            else:
                self.count += 1
                self.lineEdit_4.setPlaceholderText('已完成：' + str(self.count))
                self.progressBar.setValue(self.count)
                # print(self.count)
                img_serial = os.path.join(self.dir_path,
                                          self.lines_serial[self.count].strip('\n'))
                # img_1v1 = os.path.join(self.dir_path,
                #                        self.lines_1v1[self.count].strip('\n'))
                img_1vn = os.path.join(self.dir_path,
                                       self.lines_1vn[self.count].strip('\n'))
                self.textEdit_2.append(img_serial)
                self.textEdit_2.append(img_1vn)
                # self.textEdit_2.append(img_1v1)
                self.textEdit_2.append(
                    '------------------------------------------------')
                self.label.setPixmap(QPixmap(img_serial))
                self.label.setScaledContents(True)
                self.label_2.setPixmap(QPixmap(img_1vn))
                self.label_2.setScaledContents(True)
                # self.label_3.setPixmap(QPixmap(img_1v1))
                # self.label_3.setScaledContents(True)
        else:
            QMessageBox().information(None, "提示", "已经是最后一张了！", QMessageBox.Yes)

    def back(self):
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        self.checkBox_14.setChecked(False)
        self.checkBox_15.setChecked(False)
        self.checkBox_16.setChecked(False)
        self.checkBox_17.setChecked(False)
        self.checkBox_18.setChecked(False)
        self.checkBox_19.setChecked(False)
        self.checkBox_20.setChecked(False)
        self.checkBox_21.setChecked(False)
        self.checkBox_22.setChecked(False)
        self.checkBox_23.setChecked(False)
        self.checkBox_24.setChecked(False)
        self.checkBox_26.setChecked(False)
        self.checkBox_27.setChecked(False)
        self.checkBox_28.setChecked(False)
        self.checkBox_30.setChecked(False)
        self.checkBox_31.setChecked(False)
        self.checkBox_32.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        if self.count >= 1:
            self.count -= 1
            self.lineEdit_4.setPlaceholderText('已完成：' + str(self.count))
            self.progressBar.setValue(self.count)
            img_serial = os.path.join(self.dir_path,
                                      self.lines_serial[self.count].strip('\n'))
            # img_1v1 = os.path.join(self.dir_path,
            #                        self.lines_1v1[self.count].strip('\n'))
            img_1vn = os.path.join(self.dir_path,
                                   self.lines_1vn[self.count].strip('\n'))
            self.textEdit_2.append(img_serial)
            self.textEdit_2.append(img_1vn)
            # self.textEdit_2.append(img_1v1)
            self.textEdit_2.append(
                '------------------------------------------------')
            self.label.setPixmap(QPixmap(img_serial))
            self.label.setScaledContents(True)
            self.label_2.setPixmap(QPixmap(img_1vn))
            self.label_2.setScaledContents(True)
            # self.label_3.setPixmap(QPixmap(img_1v1))
            # self.label_3.setScaledContents(True)

        else:
            QMessageBox().information(None, "提示", "已经是第一张了！", QMessageBox.Yes)

    def skip(self):
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        self.checkBox_14.setChecked(False)
        self.checkBox_15.setChecked(False)
        self.checkBox_16.setChecked(False)
        self.checkBox_17.setChecked(False)
        self.checkBox_18.setChecked(False)
        self.checkBox_19.setChecked(False)
        self.checkBox_20.setChecked(False)
        self.checkBox_21.setChecked(False)
        self.checkBox_22.setChecked(False)
        self.checkBox_23.setChecked(False)
        self.checkBox_24.setChecked(False)
        self.checkBox_26.setChecked(False)
        self.checkBox_27.setChecked(False)
        self.checkBox_28.setChecked(False)
        self.checkBox_30.setChecked(False)
        self.checkBox_31.setChecked(False)
        self.checkBox_32.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        if self.count < self.num:
            self.count += 1
            self.lineEdit_4.setPlaceholderText('已完成：' + str(self.count))
            self.progressBar.setValue(self.count)
            img_serial = os.path.join(self.dir_path,
                                      self.lines_serial[self.count].strip('\n'))
            # img_1v1 = os.path.join(self.dir_path,
            #                        self.lines_1v1[self.count].strip('\n'))
            img_1vn = os.path.join(self.dir_path,
                                   self.lines_1vn[self.count].strip('\n'))
            self.textEdit_2.append(img_serial)
            # self.textEdit_2.append(img_1v1)
            self.textEdit_2.append(img_1vn)
            self.textEdit_2.append(
                '------------------------------------------------')
            self.label.setPixmap(QPixmap(img_serial))
            self.label.setScaledContents(True)
            self.label_2.setPixmap(QPixmap(img_1vn))
            self.label_2.setScaledContents(True)
            # self.label_3.setPixmap(QPixmap(img_1v1))
            # self.label_3.setScaledContents(True)

        else:
            QMessageBox().information(None, "提示", "已经是最后一张了！", QMessageBox.Yes)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def save(self):
        bangs = [self.checkBox_3,
                 self.checkBox_20,
                 self.checkBox_21]
        race = [self.checkBox_2,
                self.checkBox_6,
                self.checkBox_7,
                self.checkBox_8,
                self.checkBox_10]
        gender = [self.checkBox_9,
                  self.checkBox_11,
                  self.checkBox_12]
        age = [self.checkBox_14,
               self.checkBox_15,
               self.checkBox_16,
               self.checkBox_17]
        hairstyle = [self.checkBox, self.checkBox_18,
                     self.checkBox_19]
        glass = [self.checkBox_22,
                 self.checkBox_23,
                 self.checkBox_24]
        hat = [self.checkBox_26,
               self.checkBox_27,
               self.checkBox_28]
        makeup = [self.checkBox_30,
                  self.checkBox_31,
                  self.checkBox_32]

        img_serial = os.path.join(self.dir_path,
                                  self.lines_serial[self.count].strip('\n'))
        print(img_serial)
        # with open(os.path.dirname(img_serial) + '.result', 'w') as f:
        result_dict = {}

        result_dict.setdefault('人种', [])
        result_dict.setdefault('性别', [])
        result_dict.setdefault('年龄', [])
        result_dict.setdefault('眼镜', [])
        result_dict.setdefault('帽子', [])
        result_dict.setdefault('刘海', [])
        result_dict.setdefault('是否化妆', [])
        result_dict.setdefault('发型', [])

        for check_box in race:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('人种', []).append(
                    str(check_box.text()))

        for check_box in gender:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('性别', []).append(
                    str(check_box.text()))

        for check_box in age:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('年龄', []).append(
                    str(check_box.text()))

        for check_box in glass:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('眼镜', []).append(
                    str(check_box.text()))

        for check_box in hat:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('帽子', []).append(
                    str(check_box.text()))
        for check_box in bangs:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('刘海', []).append(
                    str(check_box.text()))

        for check_box in makeup:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('是否化妆', []).append(
                    str(check_box.text()))

        for check_box in hairstyle:
            if str(check_box.isChecked()) == "True":
                result_dict.setdefault('发型', []).append(
                    str(check_box.text()))
        print(result_dict)
        flag = 0
        for key, value in result_dict.items():
            if value == [] or len(value) >= 2:
                QMessageBox.warning(
                    self,
                    "warning",
                    key + "选择错误！！请检查后重新保存",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes)
                flag = 1
        if flag == 0:
            with open(os.path.join(os.path.dirname(img_serial), 'serial.json'), 'w', encoding='utf-8') as f:
                json.dump(result_dict, f, ensure_ascii=False, indent=4)
                QMessageBox.information(
                    self,
                    "information",
                    "结果已保存",
                    QMessageBox.Ok)

    def btnstate(self):
        chk = str(self.checkBox.text()) + ", isChecked=" + str(
            self.checkBox.isChecked()) + ', chekState=' + str(
            self.checkBox.checkState()) + "\n"
        chk6 = str(self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk7 = str(self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk8 = str(self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk9 = str(self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk10 =str( self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk11 = str(self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk12 =str( self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk14 = str(self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk15 = str(self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk16 =str( self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk17 = str(self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk18 =str( self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk19 = str(self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk20 = str(self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk21 =str( self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk22 =str( self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk23 = str(self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk24 = str(self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk26 =str( self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk27 =str( self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk28 =str( self.checkBox_8.text()) + ", isChecked=" + str(
            self.checkBox_8.isChecked()) + ', checkState=' + str(
            self.checkBox_8.checkState()) + "\n"
        chk30 = str(self.checkBox_6.text()) + ", isChecked=" + str(
            self.checkBox_6.isChecked()) + ', chekState=' + str(
            self.checkBox_6.checkState()) + "\n"
        chk31 =str( self.checkBox_7.text()) + ", isChecked=" + str(
            self.checkBox_7.isChecked()) + ', checkState=' + str(
            self.checkBox_7.checkState()) + "\n"
        chk32 = str(self.checkBox_32.text()) + ", isChecked=" + str(
            self.checkBox_32.isChecked()) + ', checkState=' + str(
            self.checkBox_32.checkState()) + "\n"
        chk2 = str(self.checkBox_2.text()) + ", isChecked=" + str(
            self.checkBox_2.isChecked()) + ', checkState=' + str(
            self.checkBox_2.checkState()) + "\n"
        chk3 = str(self.checkBox_3.text()) + ", isChecked=" + str(
            self.checkBox_3.isChecked()) + ', checkState=' + str(
            self.checkBox_3.checkState()) + "\n"
        # print(chk6 + chk7 + chk8)
        box_list = [chk, chk6,
                    chk7,
                    chk8,
                    chk10, chk9,
                    chk11,
                    chk12, chk14,
                    chk15,
                    chk16,
                    chk17, chk18,
                    chk19,
                    chk20,
                    chk21, chk22,
                    chk23,
                    chk24, chk26,
                    chk27,
                    chk28, chk30,
                    chk31,
                    chk32,
                    chk2,
                    chk3]
        for box in box_list:
            self.textEdit_2.append(box)


if __name__ == '__main__':
    s = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(s.exec_())
