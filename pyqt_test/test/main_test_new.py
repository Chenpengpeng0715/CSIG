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
from script.pyqt_5.test.untitled_new import Ui_Form


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

        self.radioButton_6.toggled.connect(self.btnstate)
        self.radioButton_7.toggled.connect(self.btnstate)
        self.radioButton_8.toggled.connect(self.btnstate)
        self.radioButton_9.toggled.connect(self.btnstate)
        self.radioButton_10.toggled.connect(self.btnstate)
        self.radioButton_11.toggled.connect(self.btnstate)
        self.radioButton_12.toggled.connect(self.btnstate)
        self.radioButton_14.toggled.connect(self.btnstate)
        self.radioButton_15.toggled.connect(self.btnstate)
        self.radioButton_16.toggled.connect(self.btnstate)
        self.radioButton_17.toggled.connect(self.btnstate)
        self.radioButton_18.toggled.connect(self.btnstate)
        self.radioButton_19.toggled.connect(self.btnstate)
        self.radioButton_20.toggled.connect(self.btnstate)
        self.radioButton_21.toggled.connect(self.btnstate)
        self.radioButton_22.toggled.connect(self.btnstate)
        self.radioButton_23.toggled.connect(self.btnstate)
        self.radioButton_24.toggled.connect(self.btnstate)
        self.radioButton_26.toggled.connect(self.btnstate)
        self.radioButton_27.toggled.connect(self.btnstate)
        self.radioButton_28.toggled.connect(self.btnstate)
        self.radioButton_30.toggled.connect(self.btnstate)
        self.radioButton_31.toggled.connect(self.btnstate)
        self.radioButton_32.toggled.connect(self.btnstate)
        self.radioButton_2.toggled.connect(self.btnstate)
        self.radioButton_3.toggled.connect(self.btnstate)
        self.radioButton.toggled.connect(self.btnstate)

        self.progressBar.setMinimum(0)
        self.lineEdit.setPlaceholderText("抓拍照")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        # self.lineEdit.setFocus(True)
        self.lineEdit_2.setPlaceholderText("1vn底图")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        # self.lineEdit_3.setPlaceholderText("                                 1v1底图")
        # self.dir_path = os.path.abspath(os.path.dirname(__file__))
        self.dir_path = r'D:\test\1vn_badcsae_202001_202012\1vn_badcsae_202001_202012'
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
        self.radioButton_8.setCheckanle(False)
        # self.radioButton_6.setChecked(False)
        # self.radioButton_7.setChecked(False)
        # self.radioButton_8.setChecked(False)
        # self.radioButton_9.setChecked(False)
        # self.radioButton_10.setChecked(False)
        # self.radioButton_11.setChecked(False)
        # self.radioButton_12.setChecked(False)
        # self.radioButton_14.setChecked(False)
        # self.radioButton_15.setChecked(False)
        # self.radioButton_16.setChecked(False)
        # self.radioButton_17.setChecked(False)
        # self.radioButton_18.setChecked(False)
        # self.radioButton_19.setChecked(False)
        # self.radioButton_20.setChecked(False)
        # self.radioButton_21.setChecked(False)
        # self.radioButton_22.setChecked(False)
        # self.radioButton_23.setChecked(False)
        # self.radioButton_24.setChecked(False)
        # self.radioButton_26.setChecked(False)
        # self.radioButton_27.setChecked(False)
        # self.radioButton_28.setChecked(False)
        # self.radioButton_30.setChecked(False)
        # self.radioButton_31.setChecked(False)
        # self.radioButton_32.setChecked(False)
        # self.radioButton_3.setChecked(False)
        # self.radioButton_2.setChecked(False)
        # self.radioButton.setChecked(False)
        QApplication.processEvents()
        if self.count < self.num:
            self.count += 1
            img_serial = os.path.join(self.dir_path,
                                      self.lines_serial[self.count - 1].strip('\n'))
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
        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(False)
        self.radioButton_8.setChecked(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_12.setChecked(False)
        self.radioButton_14.setChecked(False)
        self.radioButton_15.setChecked(False)
        self.radioButton_16.setChecked(False)
        self.radioButton_17.setChecked(False)
        self.radioButton_18.setChecked(False)
        self.radioButton_19.setChecked(False)
        self.radioButton_20.setChecked(False)
        self.radioButton_21.setChecked(False)
        self.radioButton_22.setChecked(False)
        self.radioButton_23.setChecked(False)
        self.radioButton_24.setChecked(False)
        self.radioButton_26.setChecked(False)
        self.radioButton_27.setChecked(False)
        self.radioButton_28.setChecked(False)
        self.radioButton_30.setChecked(False)
        self.radioButton_31.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_32.setChecked(False)
        self.radioButton.setChecked(False)

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

        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(False)
        self.radioButton_8.setChecked(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_12.setChecked(False)
        self.radioButton_14.setChecked(False)
        self.radioButton_15.setChecked(False)
        self.radioButton_16.setChecked(False)
        self.radioButton_17.setChecked(False)
        self.radioButton_18.setChecked(False)
        self.radioButton_19.setChecked(False)
        self.radioButton_20.setChecked(False)
        self.radioButton_21.setChecked(False)
        self.radioButton_22.setChecked(False)
        self.radioButton_23.setChecked(False)
        self.radioButton_24.setChecked(False)
        self.radioButton_26.setChecked(False)
        self.radioButton_27.setChecked(False)
        self.radioButton_28.setChecked(False)
        self.radioButton_30.setChecked(False)
        self.radioButton_31.setChecked(False)
        self.radioButton_32.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton.setChecked(False)

        QApplication.processEvents()
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
        bangs = [self.radioButton_3,
                 self.radioButton_20,
                 self.radioButton_21,]
        race = [self.radioButton_2,
                self.radioButton_6,
                self.radioButton_7,
                self.radioButton_8,
                self.radioButton_10]
        gender = [self.radioButton_9,
                  self.radioButton_11,
                  self.radioButton_12]
        age = [self.radioButton_14,
               self.radioButton_15,
               self.radioButton_16,
               self.radioButton_17]
        hairstyle = [self.radioButton, self.radioButton_18,
                     self.radioButton_19]
        glass = [self.radioButton_22,
                 self.radioButton_23,
                 self.radioButton_24]
        hat = [self.radioButton_26,
               self.radioButton_27,
               self.radioButton_28]
        makeup = [self.radioButton_30,
                  self.radioButton_31,
                  self.radioButton_32]
        img_serial = os.path.join(self.dir_path,
                                  self.lines_serial[self.count].strip('\n'))
        print(img_serial)
        # with open(os.path.dirname(img_serial) + '.result', 'w') as f:
        result_dict = {}
        with open(os.path.join(os.path.dirname(img_serial), 'serial.json'), 'w', encoding='utf-8') as f:
            result_dict.setdefault('人种', [])
            result_dict.setdefault('年龄', [])
            result_dict.setdefault('性别', [])
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
            for check_box in bangs:
                if str(check_box.isChecked()) == "True":
                    result_dict.setdefault('刘海', []).append(
                        str(check_box.text()))

            for check_box in hat:
                if str(check_box.isChecked()) == "True":
                    result_dict.setdefault('帽子', []).append(
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
                if value == []:
                    QMessageBox.warning(
                        self,
                        "warning",
                        key + "未选择！！请检查后重新保存",
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.Yes)
                    flag = 1
            if flag == 0:
                json.dump(result_dict, f, ensure_ascii=False, indent=4)
                QMessageBox.information(
                    self,
                    "information",
                    "结果已保存",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes)

    def btnstate(self):
        bangs = [self.radioButton_3,
                 self.radioButton_20,
                 self.radioButton_21, ]
        race = [self.radioButton_2,
                self.radioButton_6,
                self.radioButton_7,
                self.radioButton_8,
                self.radioButton_10]
        gender = [self.radioButton_9,
                  self.radioButton_11,
                  self.radioButton_12]
        age = [self.radioButton_14,
               self.radioButton_15,
               self.radioButton_16,
               self.radioButton_17]
        hairstyle = [self.radioButton, self.radioButton_18,
                     self.radioButton_19]
        glass = [self.radioButton_22,
                 self.radioButton_23,
                 self.radioButton_24]
        hat = [self.radioButton_26,
               self.radioButton_27,
               self.radioButton_28]
        makeup = [self.radioButton_30,
                  self.radioButton_31,
                  self.radioButton_32]
        img_serial = os.path.join(self.dir_path,
                                  self.lines_serial[self.count].strip('\n'))
        print(img_serial)
        # with open(os.path.dirname(img_serial) + '.result', 'w') as f:
        result_dict = {}
        with open(os.path.join(os.path.dirname(img_serial), 'serial.json'), 'w', encoding='utf-8') as f:
            result_dict.setdefault('人种', [])
            result_dict.setdefault('年龄', [])
            result_dict.setdefault('性别', [])
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
            for check_box in bangs:
                if str(check_box.isChecked()) == "True":
                    result_dict.setdefault('刘海', []).append(
                        str(check_box.text()))

            for check_box in hat:
                if str(check_box.isChecked()) == "True":
                    result_dict.setdefault('帽子', []).append(
                        str(check_box.text()))

            for check_box in makeup:
                if str(check_box.isChecked()) == "True":
                    result_dict.setdefault('是否化妆', []).append(
                        str(check_box.text()))

            for check_box in hairstyle:
                if str(check_box.isChecked()) == "True":
                    result_dict.setdefault('发型', []).append(
                        str(check_box.text()))
            # print(result_dict)
            self.textEdit_2.append(result_dict)

if __name__ == '__main__':
    s = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(s.exec_())
