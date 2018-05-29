#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from weather import Ui_Form
import requests

class MainWindow(QMainWindow):
    def __init__(self,parent =None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def queryWeather(self):
        print('* queryWeather')
        cityName = self.ui.comboBox.currentText()
        cityCode = self.transCityName(cityName)
        rep = requests.get('http://www.weather.com.cn/data/sk/{0}.html'.format(cityCode))
        rep.encoding = 'utf-8'
        print('返回结果:%s' % rep.json())
        msg1 = '城市:{0}\n风向:{1}\n温度:{2}度\n风力:{3}\n湿度:{4} \n'\
            .format(rep.json()['weatherinfo']['city'],rep.json()['weatherinfo']['WD'],rep.json()['weatherinfo']['temp'],rep.json()['weatherinfo']['WS'],rep.json()['weatherinfo']['SD'],rep.json()['weatherinfo']['WD'])
        self.ui.resultText.setText(msg1)

    def clearResult(self):
        print('* clearResult')
        self.ui.resultText.clear()



    def transCityName(self,cityName):
        cityCode = ''
        city = {'北京': '101010100', '上海': '101020100', '东莞': '101281601', '广州': '101280101'}
        try:
            cityCode = city[cityName]
        except:
            print('没找到这城市')
        return cityCode

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())