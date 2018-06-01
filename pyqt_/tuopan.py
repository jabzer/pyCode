#!/usr/bin/python3
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TrayIcon(QSystemTrayIcon):
    def __init__(self,parent = None):
        super(TrayIcon,self).__init__(parent)
        # self.showMenu()
        self.other()

    # def showMenu(self):
    #     self.menu = QMenu()
    #     self.menu1 = QMenu()
    #     #self.showAction1 = QAction(self,"显示消息1",triggered=self.showM)
    #     self.showAction1 = QAction("显示消息1",self)
    #     self.showAction1.triggered.connect(self.showM)
    #     #self.showAction2 = QAction(self,"显示消息2",  triggered=self.showM)
    #     self.showAction2 = QAction("显示消息2", self)
    #     self.showAction2.triggered.connect(self.showM)
    #     #self.quitAction = QAction(self,"退出",triggered=self.quit)
    #     self.showAction = QAction("退出", self)
    #     self.showAction.triggered.connect(self.quit)
    #
    #     self.menu1.addAction(self.showAction1)
    #     self.menu1.addAction(self.showAction2)
    #     self.menu.addAction(self.menu1,)
    #
    #     self.menu.addAction(self.showAction1)
    #     self.menu.addAction(self.showAction2)
    #     self.menu.addAction(self.quitAction)
    #     self.menu1.setTitle("二级菜单")
    #     self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)
        self.messageClicked.connect(self.mClied)
        self.setIcon(QIcon("christmass_star_2.png"))
        self.icon = self.MessageIcon()

    def iconClied(self,reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason ==2 or reason==3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    def mClied(self):
        self.showMessage("提示","你点了消息",self.icon)



    def showM(self):
        self.showMessage("测试","我是消息",self.icon)

    def quit(self):
        self.setVisible(False)
        self.parent().exit()
        qApp.quit()
        sys.exit()

class window(QWidget):
    def __init__(self,parent=None):
        super(window,self).__init__(parent)
        ti = TrayIcon(self)
        ti.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())