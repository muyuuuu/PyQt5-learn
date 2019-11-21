# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(903, 678)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = MatplotlibWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(200, 200))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = MatplotlibWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 200))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 3, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 2, 0, 1, 1)
        self.widget.raise_()
        self.widget_2.raise_()
        self.widget_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "静态绘图"))
        self.pushButton.setText(_translate("Form", "动态绘图"))
        self.quit_btn.setText(_translate("Form", "退出"))
from MatplotlibWidget import MatplotlibWidget
