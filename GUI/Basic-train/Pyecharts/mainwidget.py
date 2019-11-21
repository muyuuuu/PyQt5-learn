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
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 2, 1, 1, 1)
        self.quit_btn_2 = QtWidgets.QPushButton(Form)
        self.quit_btn_2.setObjectName("quit_btn_2")
        self.gridLayout.addWidget(self.quit_btn_2, 2, 0, 1, 1)
        self.web_view = QtWebEngineWidgets.QWebEngineView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_view.sizePolicy().hasHeightForWidth())
        self.web_view.setSizePolicy(sizePolicy)
        self.web_view.setMinimumSize(QtCore.QSize(300, 100))
        self.web_view.setObjectName("web_view")
        self.gridLayout.addWidget(self.web_view, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.quit_btn.setText(_translate("Form", "退出"))
        self.quit_btn_2.setText(_translate("Form", "动态绘图"))
from PyQt5 import QtWebEngineWidgets
