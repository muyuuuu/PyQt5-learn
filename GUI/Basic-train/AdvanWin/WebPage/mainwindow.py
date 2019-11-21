# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(1100, 650, 91, 34))
        font = QtGui.QFont()
        font.setFamily("苹方")
        font.setPointSize(14)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.quit_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn_2.setGeometry(QtCore.QRect(30, 80, 91, 34))
        font = QtGui.QFont()
        font.setFamily("苹方")
        font.setPointSize(14)
        self.quit_btn_2.setFont(font)
        self.quit_btn_2.setObjectName("quit_btn_2")
        self.quit_btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn_3.setGeometry(QtCore.QRect(170, 80, 91, 34))
        font = QtGui.QFont()
        font.setFamily("苹方")
        font.setPointSize(14)
        self.quit_btn_3.setFont(font)
        self.quit_btn_3.setObjectName("quit_btn_3")
        self.quit_btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn_4.setGeometry(QtCore.QRect(10, 140, 91, 34))
        font = QtGui.QFont()
        font.setFamily("苹方")
        font.setPointSize(14)
        self.quit_btn_4.setFont(font)
        self.quit_btn_4.setObjectName("quit_btn_4")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(0, 180, 1201, 531))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quit_btn.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "显示时间"))
        self.quit_btn_2.setText(_translate("MainWindow", "开始"))
        self.quit_btn_3.setText(_translate("MainWindow", "结束"))
        self.quit_btn_4.setText(_translate("MainWindow", "加载界面"))
from PyQt5 import QtWebEngineWidgets
