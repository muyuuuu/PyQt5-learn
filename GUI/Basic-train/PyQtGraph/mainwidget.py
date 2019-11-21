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
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 100, 731, 451))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pyqtgraph = GraphicsLayoutWidget(self.widget)
        self.pyqtgraph.setMinimumSize(QtCore.QSize(100, 50))
        self.pyqtgraph.setObjectName("pyqtgraph")
        self.horizontalLayout.addWidget(self.pyqtgraph)
        self.pyqtgraph2 = GraphicsLayoutWidget(self.widget)
        self.pyqtgraph2.setMinimumSize(QtCore.QSize(100, 50))
        self.pyqtgraph2.setObjectName("pyqtgraph2")
        self.horizontalLayout.addWidget(self.pyqtgraph2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(self.widget)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "单条线绘图"))
        self.pushButton_2.setText(_translate("Form", "多条线绘图"))
        self.quit_btn.setText(_translate("Form", "退出"))
from pyqtgraph import GraphicsLayoutWidget
