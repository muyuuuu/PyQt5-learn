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