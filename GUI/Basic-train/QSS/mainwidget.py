# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(903, 678)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, -10, 971, 741))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.quit_btn_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit_btn_3.sizePolicy().hasHeightForWidth())
        self.quit_btn_3.setSizePolicy(sizePolicy)
        self.quit_btn_3.setObjectName("quit_btn_3")
        self.gridLayout.addWidget(self.quit_btn_3, 0, 0, 1, 1)
        self.quit_btn_5 = QtWidgets.QPushButton(self.widget)
        self.quit_btn_5.setObjectName("quit_btn_5")
        self.gridLayout.addWidget(self.quit_btn_5, 1, 0, 1, 1)
        self.quit_btn_4 = QtWidgets.QPushButton(self.widget)
        self.quit_btn_4.setObjectName("quit_btn_4")
        self.gridLayout.addWidget(self.quit_btn_4, 2, 0, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(self.widget)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.quit_btn_3.setText(_translate("Form", "黑色主题"))
        self.quit_btn_5.setText(_translate("Form", "默认主题"))
        self.quit_btn_4.setText(_translate("Form", "白色主题"))
        self.quit_btn.setText(_translate("Form", "退出"))
