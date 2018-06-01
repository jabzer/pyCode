# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 248)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 201))
        self.groupBox.setObjectName("groupBox")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(30, 50, 441, 141))
        self.resultText.setObjectName("resultText")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(30, 20, 105, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        self.queryBtn.clicked.connect(Form.queryWeather)
        self.clearBtn.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "城市："))
        self.comboBox.setItemText(0, _translate("Form", "上海"))
        self.comboBox.setItemText(1, _translate("Form", "北京"))
        self.comboBox.setItemText(2, _translate("Form", "东莞"))
        self.comboBox.setItemText(3, _translate("Form", "广州"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))

