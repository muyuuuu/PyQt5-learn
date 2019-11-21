# import pyqtgraph.examples
# pyqtgraph.examples.run()

#!/bin/bash
# -*- coding: UTF-8 -*-
import pyqtgraph as pg 
import sys
import numpy as np 
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from mainwidget import Ui_Form
from mainwindow import Ui_MainWindow

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWidget(QWidget, Ui_Form):

    def __init__(self, parent = None):

        super(MyMainWidget, self).__init__(parent)

        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')
        pg.setConfigOptions(antialias = True)

        self.setupUi(self)
        self.setLayout(self.gridLayout)

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)

        # 绘图
        self.pushButton.clicked.connect(self.graph_plot)
        self.pushButton_2.clicked.connect(self.graph_plot1)

    def graph_plot1(self):
        self.pyqtgraph2.clear()
        plt = self.pyqtgraph2.addPlot(title="test")
        x = np.random.normal(size=20)
        y1 = np.sin(x)
        y2 = 1.1 * np.sin(x + 1)
        bg1 = pg.BarGraphItem(x = x, height = y1, width = 2, brush = 'r')
        bg2 = pg.BarGraphItem(x = x, height = y2, width = 2, brush = 'b')
        plt.addItem(bg1)
        plt.addItem(bg2)
        # self.pyqtgraph2.nextColumn()
        self.pyqtgraph2.nextRow()
        plt2 = self.pyqtgraph2.addPlot(title="test1")
        x = np.linspace(1, 20, 20)
        y3 = np.random.normal(size=20)
        plt2.plot(x, y3, pen = pg.mkPen(width = 2, color = 'd'))
        plt2.showGrid(x=True, y=True)


    def graph_plot(self):
        self.pyqtgraph.clear()
        # 两种绘图方式
        # self.pyqtgraph.addPlot(y = np.random.normal(size=100),
            # pen = pg.mkPen(color='b', width=2))
        plt2 = self.pyqtgraph.addPlot(title="multi rules")
        plt2.plot(np.random.normal(size=150),
            pen = pg.mkPen(color='r', width=2))
        plt2.plot(np.random.normal(size=150) + 5,
            pen = pg.mkPen(color='b', width=2))


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
