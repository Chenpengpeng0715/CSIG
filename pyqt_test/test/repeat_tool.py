# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/11/26 18:04
import sys
import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from script.pyqt_5.repeat import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_line_edit_info(self):
        file_line = self.textEdit_2.toPlainText()
        l = []
        l1 = []
        for line in file_line.split('\n'):
            if line not in l:
                l.append(line.strip('\n'))
            else:
                # if line not in l1:
                l1.append(line.strip('\n'))
        self.lineEdit_6.clear()
        self.lineEdit_3.clear()
        self.lineEdit.clear()
        self.textEdit_3.clear()
        self.textEdit.clear()
        for i in l:
            self.textEdit_3.append(i)
        for j in l1:
            self.textEdit.append(j)
        self.lineEdit_6.insert(str(len(file_line.split('\n'))))
        self.lineEdit_3.insert(str(len(l)))
        self.lineEdit.insert(str(len(l1)))

    @pyqtSlot()
    def save_result(self):
        now = time.time()
        local_time = time.localtime(now)
        date_format_localtime = time.strftime('%Y-%m-%d-%H-%M-%S', local_time)
        result_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), date_format_localtime + '.txt')
        print(result_path)
        with open(result_path, 'w') as f:
            result_info = self.textEdit_3.toPlainText()
            for i in range(len(result_info.split('\n'))):
                if i < len(result_info.split('\n')) - 1:
                    f.write(result_info.split('\n')[i] + '\n')
                else:
                    f.write(result_info.split('\n')[i])

        QMessageBox.information(self,  # 使用infomation信息框
                                "result",
                                "save file successful : %s" % result_path)





    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出',
                                     "确认关闭窗口？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    s = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(s.exec_())