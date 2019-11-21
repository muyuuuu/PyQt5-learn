#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import time
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget)
from PyQt5.QtCore import QTimer, QDateTime, Qt, QUrl, QThread
# from PyQt5.QtGui import QColor, QPalette
from mainwindow import Ui_MainWindow

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.resize(1200, 740)

        # 默认的状态栏
        self.status = self.statusBar()
        self.status.showMessage("你在主页面～")
        
        # 标题栏
        self.setWindowTitle("建模协会录入信息")

        # 窗口居中
        self.center()

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)

        # 定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.quit_btn_2.clicked.connect(self.start_time)
        self.quit_btn_3.clicked.connect(self.end_time)

        # 加载网络界面
        self.quit_btn_4.clicked.connect(self.show_page) # 加载外部的界面
        # 加载本地的页面
        # url = rE:/index.html'
        # self.webEngineView.load(Qurl(url))

        # pyqt 与 JavaScript 可以相互调用

    def show_page(self):
        self.webEngineView.load(QUrl('https://muyuuuu.github.io/'))

    def start_time(self):
        self.timer.start() # 不设置间隔时间
    
    def end_time(self):
        self.timer.stop()

    def show_time(self):
        time = QDateTime.currentDateTime()
        time = time.toString("yyyy-MM-dd hh : mm : ss dddd")
        self.label.setText(time)

    def quit_act(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text() + '键被按下')
        qApp = QApplication.instance()
        qApp.quit()

    def center(self):
        '''
        获取桌面长宽
        获取窗口长宽
        移动
        '''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == "__main__":
    # 在shell中执行
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    # 开始主循环，直到退出
    sys.exit(app.exec())