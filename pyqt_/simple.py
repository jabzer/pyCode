import sys

from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('微软雅黑',10))
        self.setToolTip('这是<b>Qwidget</b>的提醒')
        self.setGeometry(500,500,300,100)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('christmass_star_2.png'))
        self.center()
        btn = QPushButton('退出',self)
        btn.setToolTip('退出')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'提醒','确定要退出吗?',QMessageBox.Yes |
                                     QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())