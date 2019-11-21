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
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 761, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.quit_btn_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.quit_btn_7.setObjectName("quit_btn_7")
        self.gridLayout.addWidget(self.quit_btn_7, 0, 1, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 0, 2, 1, 1)
        self.widget_2 = DataTableWidget(self.layoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 2, 0, 2, 3)
        self.quit_btn_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.quit_btn_5.setObjectName("quit_btn_5")
        self.gridLayout.addWidget(self.quit_btn_5, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.quit_btn_7.setText(_translate("Form", "保存数据"))
        self.quit_btn.setText(_translate("Form", "退出"))
        self.quit_btn_5.setText(_translate("Form", "导入数据"))
from qtpandas.views.DataTableView import DataTableWidget
