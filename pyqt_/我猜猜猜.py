#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)
        print(self.num)

    def initUI(self):
        self.setGeometry(300, 300, 320, 200)
        self.setWindowTitle('我猜猜猜')
        self.setWindowIcon(QIcon('christmass_star_2.png'))

        bt1 = QPushButton('我猜', self)
        bt1.setGeometry(115, 150, 70, 30)
        bt1.setToolTip('猜数字')
        bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):
        guessnumber = int(self.text.text())


        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '你中奖了')
            self.num = randint(1, 100)
            print(self.num)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '确认退出？', '确认退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
