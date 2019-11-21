#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import time
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget, QDesktopWidget,
                            QFormLayout, QLineEdit, QStackedWidget, QHBoxLayout, QDockWidget,
                            QMdiSubWindow, QMdiArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
from mainwindow import Ui_MainWindow

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.resize(1200, 740)

        # 默认的状态栏
        self.status = self.statusBar()
        self.status.showMessage("你在主页面～")
        
        # 标题栏
        self.setWindowTitle("建模协会录入信息")

        # 窗口居中
        self.center()

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)
        
        # QTabWidget 多窗口使用
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.line = QLineEdit() # line 要在调用之前创建
        self.tabWidget.addTab(self.tab1, "标题1")
        self.tabWidget.addTab(self.tab2, "标题2")
        self.tabWidget.addTab(self.tab3, "标题3")
        self.tab1_()
        self.tab2_()
        self.tab3_()
        # self.line = QLineEdit() 这里不对
        self.quit_btn_2.clicked.connect(self.display_line)

        # QStackedWidget
        self.listWidget.insertItem(0, "标题1")
        self.listWidget.insertItem(1, "标题2")
        self.listWidget.insertItem(2, "标题3")
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack1_()
        self.stack2_()
        self.stack3_()
        self.stackedWidget.addWidget(self.stack1)
        self.stackedWidget.addWidget(self.stack2)
        self.stackedWidget.addWidget(self.stack3)
        self.listWidget.currentRowChanged.connect(self.display_stack)

        # QDockWidget 使用 浮动窗体
        # self.dockWidget = QDockWidget("test", self)
        self.dockWidget.setWidget(self.tabWidget)
        self.quit_btn_3.clicked.connect(self.display_dock)

        # 多文档界面
        self.mdi = QMdiArea()
        self.quit_btn_3.clicked.connect(self.new_win)
        # self.setCentralWidget(self.mdi) # 似乎不太好用

        # ScrollBar 的使用 (选择颜色)
        self.verticalScrollBar.setMaximum(255)
        self.verticalScrollBar_2.setMaximum(255)
        self.verticalScrollBar_3.setMaximum(255)
        self.verticalScrollBar_3.sliderMoved.connect(self.color_change)
        self.verticalScrollBar_2.sliderMoved.connect(self.color_change)
        self.verticalScrollBar.sliderMoved.connect(self.color_change)

    def color_change(self):
        c = QColor(self.verticalScrollBar.value(), self.verticalScrollBar_2.value(), 
                self.verticalScrollBar_3.value())
        palette = QPalette()
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def new_win(self):
        sub = QMdiSubWindow()
        # sub.setWidget(self.listWidget)
        self.mdi.addSubWindow(sub)
        sub.show()

    # 用于关闭之后子按此打开悬浮窗口
    def display_dock(self):
        self.dockWidget.show()

    def display_stack(self, i):
        # print(i)
        self.stackedWidget.setCurrentIndex(i)

    def stack1_(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        self.stack1.setLayout(layout)

    def stack2_(self):
        layout = QFormLayout()
        layout.addRow("年龄", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3_(self):
        layout = QFormLayout()
        layout.addRow("备注", QLineEdit())
        self.stack3.setLayout(layout)

    def display_line(self):
        print(self.line.text())

    def tab1_(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        self.tab1.setLayout(layout)

    def tab2_(self):
        layout = QFormLayout()
        layout.addRow("年龄", self.line)
        self.tab2.setLayout(layout)

    def tab3_(self):
        layout = QFormLayout()
        layout.addRow("备注", QLineEdit())
        self.tab3.setLayout(layout)

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