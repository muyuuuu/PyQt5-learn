#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import time
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
# 导入样式
import qdarkstyle
from mainwidget import Ui_Form
from mainwindow import Ui_MainWindow

# 样式的类
class StyleFile:
    def __init__(self):
        pass
    # @staticmethod
    def readQSS(style):
        with open (style, 'r') as f:
            return f.read()

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWidget(QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(MyMainWidget, self).__init__(parent)
        self.setupUi(self)
        # self.resize(1000, 700)

        # 默认的状态栏
        # 可以设置其他按钮点击 参考多行文本显示 然而不行 
        # self.status = self.statusBar()
        # self.status.showMessage("你在主页面～")
        
        # 标题栏
        self.setWindowTitle("建模协会录入信息")

        # 窗口居中
        self.center()

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)

        # 无边框程序
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # 设置为桌面尺寸
        desktop = QApplication.desktop() # 得到桌面控件
        # print(desktop.height(), desktop.width()) # 输出桌面的宽高
        rect = desktop.availableGeometry()
        self.setGeometry(rect)

        # 载入自定义 QSS
        self.quit_btn_3.clicked.connect(self.style_change)

        self.quit_btn_4.clicked.connect(self.style_change1)

        # 换默认主题
        self.quit_btn_5.clicked.connect(self.style_change2)

        # QMainWindow 有自己的布局，所以下列语句无效
        # 只有设置布局，风格切换才有效
        self.setLayout(self.gridLayout)

        # self.setCentralWidget(self)

    def style_change2(self):
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def style_change1(self):
        style_file = 'white.qss'
        self.style = StyleFile.readQSS(style_file)
        self.setStyleSheet(self.style)
        palette = QPalette()
        c = QColor(192,253,123)
        palette.setColor(QPalette.Background, c)
        q = MyMainWindow()
        q.setPalette(palette)
        

    def style_change(self):
        style_file = 'black.qss'
        self.style = StyleFile.readQSS(style_file)
        self.setStyleSheet(self.style)

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

class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        q = MyMainWidget()
        self.setCentralWidget(q)

        # 设置窗口透明
        self.setWindowOpacity(0.9)


if __name__ == "__main__":
    # 在shell中执行
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    # 开始主循环，直到退出
    sys.exit(app.exec())
