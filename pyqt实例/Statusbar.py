#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QAction,qApp,QMessageBox
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('christmass_star_2.png'),'退出',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar().showMessage('准备')

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('退出')
        self.toolbar.addAction(exitAction)



        self.resize(300,300)
        self.center()
        self.setWindowTitle('menubar')
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'提醒','确定要退出吗?',QMessageBox.Yes |
                                     QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())