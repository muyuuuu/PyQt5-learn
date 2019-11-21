#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import numpy as np
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget,
                                QSizePolicy, QPushButton, QGridLayout)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
from mainwidget import Ui_Form
from mainwindow import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
# 绘图的空白界面
class MymplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111) # 多界面绘图
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, 
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

    def static_plot(self):
        self.axes.clear()
        self.fig.suptitle("static FIG")
        t = np.linspace(1, 10, 10)
        s = np.sin(np.pi * t)
        self.axes.plot(t, s)
        self.axes.grid(True)
        self.draw()

    # 为何要加参数
    def dynamic_plot(self, *args, **kwargs):
        timer = QTimer(self)
        timer.timeout.connect(self.update_fig)
        timer.start(1000)

    def update_fig(self):
        self.axes.clear()
        self.fig.suptitle("dynamic FIG")
        l = np.random.randint(1, 10, 4)
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.grid(True)
        self.draw()

# 实现绘图类
class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        # 封装绘图类
        self.gridLayout = QGridLayout()
        self.mpl = MymplCanvas(self)
        # 添加matplotlib的工具栏
        self.mpl_tool = NavigationToolbar(self.mpl, self)
        # self.quit_btn_2 = QPushButton()
        # self.quit_btn_3 = QPushButton()
        # self.quit_btn_2.clicked.connect(self.static)
        # self.quit_btn_3.clicked.connect(self.dynamic)
        self.setLayout(self.gridLayout)
        self.gridLayout.addWidget(self.mpl)
        self.gridLayout.addWidget(self.mpl_tool)
        # self.gridLayout.addWidget(self.quit_btn_2)
        # self.gridLayout.addWidget(self.quit_btn_3)

    def static(self):
        self.mpl.static_plot()

    def dynamic(self):
        self.mpl.dynamic_plot()
        

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWidget(QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(MyMainWidget, self).__init__(parent)
        self.setupUi(self)

        self.setLayout(self.gridLayout)

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)

        # 没有提升窗口控件
        # q = MatplotlibWidget()
        # self.gridLayout.addWidget(q)

        # 提升前
        # self.widget = MatplotlibWidget()
        self.widget.setVisible(False)
        # self.widget_2 = MatplotlibWidget()
        self.widget_2.setVisible(False)
        # print(type(self.widget_2))

        # 提升后
        # self.gridLayout.addWidget(self.widget)
        # self.gridLayout.addWidget(self.widget_2)
        self.pushButton.clicked.connect(self.dynamic)
        self.pushButton_2.clicked.connect(self.static)

    def static(self):
        self.widget.setVisible(True)
        self.widget.mpl.static_plot()

    def dynamic(self):
        self.widget_2.setVisible(True)
        self.widget_2.mpl.dynamic_plot()

    def quit_act(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text() + '键被按下')
        qApp = QApplication.instance()
        qApp.quit()


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        q = MyMainWidget()
        self.setCentralWidget(q)

        # 设置窗口透明
        self.setWindowOpacity(0.9)

        # self.resize(1000, 700)

        # 默认的状态栏
        # 可以设置其他按钮点击 参考多行文本显示 然而不行 
        self.status = self.statusBar()
        self.status.showMessage("你在主页面～")
        
        # 标题栏
        self.setWindowTitle("建模协会录入信息")

        # 窗口居中
        self.center()

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
