# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/11/19 17:27

import sys
import shutil
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QAction, QFileDialog, QMessageBox, QPushButton)
import os


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.open_btn = QPushButton('open dir')
        self.dest_btn = QPushButton('result dir')
        self.file_num = QPushButton('file num')
        self.start = QPushButton('Start split')


        self.openEdit = QLineEdit()
        self.destEdit = QLineEdit()
        self.fileEdit = QLineEdit()
        self.reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.open_btn, 1, 0)
        grid.addWidget(self.openEdit, 1, 1)

        grid.addWidget(self.dest_btn, 2, 0)
        grid.addWidget(self.destEdit, 2, 1)

        grid.addWidget(self.file_num, 3, 0)
        grid.addWidget(self.fileEdit, 3, 1)

        grid.addWidget(self.start, 4, 0)
        grid.addWidget(self.reviewEdit, 4, 1, 5, 1)

        self.setLayout(grid)

        # openFile = QAction(QIcon('open.png'), 'Open', self)
        self.open_btn.setShortcut('Ctrl+O')
        self.open_btn.setStatusTip('Open new File')
        self.open_btn.clicked.connect(self.showDialog)
        self.dest_btn.clicked.connect(self.showDialog1)
        self.start.clicked.connect(self.split_file)
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(self.open_btn)

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('                                                                 Split File')
        self.show()

    def showDialog(self):
        dir_path = QFileDialog.getExistingDirectory(self, 'Open file', '/home')
        if os.path.exists(dir_path):
            self.openEdit.insert(dir_path)
            self.destEdit.insert(dir_path + '_split')

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