# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/11/23 15:43

import sys
import shutil

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QAction, QFileDialog, QMessageBox, QPushButton)
import os


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        # self.img_num = img_num

    def initUI(self):
        self.open_btn = QPushButton('open dir')
        # self.dest_btn = QPushButton('result dir')
        self.Back = QPushButton('上一张')
        self.Next = QPushButton('下一张')
        self.Face = QPushButton('真人')
        self.NoFace = QPushButton('非人脸')
        self.UnCertain = QPushButton('有歧义')

        self.lbl = QLabel(self)
        # self.lbl.setGeometry(0, 0, 400, 400)
        # self.setCentralWidget(self.lbl)

        self.openEdit = QLineEdit()
        # self.destEdit = QLineEdit()
        # self.fileEdit = QLineEdit()
        self.reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        self.setLayout(grid)

        grid.addWidget(self.open_btn, 1, 0)
        grid.addWidget(self.openEdit, 4, 0)

        grid.addWidget(self.Back, 2, 0)
        # grid.addWidget(self.Back, 2, 1)

        grid.addWidget(self.Next, 3, 0)
        # grid.addWidget(self.Next, 3, 1)

        grid.addWidget(self.lbl, 1, 1, 6, 3)

        grid.addWidget(self.reviewEdit, 5, 0, 5, 1)



        # openFile = QAction(QIcon('open.png'), 'Open', self)
        self.open_btn.setShortcut('Ctrl+O')
        self.open_btn.setStatusTip('Open new File')
        self.open_btn.clicked.connect(self.showDialog)
        self.Back.clicked.connect(self.show_img)
        self.Next.clicked.connect(self.show_img)
        # self.dest_btn.clicked.connect(self.showDialog1)
        # self.start.clicked.connect(self.split_file)
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(self.open_btn)

        self.setGeometry(300, 300, 640, 480)
        # self.setMaximumSize(500, 400)
        # self.setMinimumSize(500, 400)
        self.setWindowTitle('                                                                 Split File')
        self.show()

    def showDialog(self):
        ext = ['.jpg', '.png', '.bmp', '.jpeg', '.JPEG', '.PNG', '.JPG']
        dir_path = QFileDialog.getExistingDirectory(self, 'Open file', '/home')
        if os.path.exists(dir_path):
            self.openEdit.insert(dir_path)
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if os.path.splitext(file)[-1] in ext:
                        file_path = os.path.join(root, file)
                        self.reviewEdit.append(file_path)
        # file_text = self.reviewEdit.toPlainText()
        # print(file_text)
        # for line in file_text.split('\t'):
        #     print(line)

    def showDialog1(self):
        dir_path = QFileDialog.getExistingDirectory(self, 'Open file', '/home')
        if os.path.exists(dir_path):
            # self.openEdit.insert(dir_path)
            self.openEdit.setText(dir_path)
            # self.destEdit.insert(dir_path + '_split')

    def split_file(self):
        count = 0
        curr_path = self.openEdit.text()
        # dest_path = self.destEdit.text()
        dest_path = curr_path + '_split'
        # print(dest_path)
        self.destEdit.insert(dest_path)
        key_word = self.fileEdit.text()
        for root, dirs, files in os.walk(curr_path):
            for file in files:
                key = count // int(key_word)
                d_path = str(root).replace(curr_path, os.path.join(dest_path, str(key)))
                if not os.path.exists(d_path):
                    os.makedirs(d_path)
                shutil.copy(os.path.join(root, file), os.path.join(d_path, file))
                # print(os.path.join(root, file))
                self.reviewEdit.append(os.path.join(root, file))
                count += 1
        self.reviewEdit.append("split done !!!")

    def show_img(self):
        file_text = self.reviewEdit.toPlainText()
        file_list = file_text.split('\n')
        # n = len(file_list)
        # global n
        print(file_list)
        if file_list == []:
            self.lbl.setPixmap(QPixmap(""))  # 移除label上的图片
        else:

            pixmap = QPixmap(file_list[0])
            scaredPixmap = pixmap.scaled(400, 400, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(scaredPixmap)
            # self.lbl.resize(300, 200)
            # self.lbl.setScaledContents(True)



    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())