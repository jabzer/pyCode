#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QPushButton,QLabel,
                             QLCDNumber,QSlider,QVBoxLayout,QApplication,QMessageBox)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)
        btn1 = QPushButton('按键1',self)
        btn2 = QPushButton('按键2', self)
        self.lb = QLabel(self)


        vbox= QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(self.lb)

        self.setLayout(vbox)
        # self.statusBar()
        sld.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.setGeometry(300,300,300,400)
        self.setWindowTitle('信号')
        self.show()

    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()
    def buttonClicked(self):
        sender = self.sender()
        self.lb.setText(sender.text()+'被按下')
        QMessageBox.about(self,'提醒',sender.text()+'被按下')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())