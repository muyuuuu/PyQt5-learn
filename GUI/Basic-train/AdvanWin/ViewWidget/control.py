#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import time
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QHeaderView,
                            QMessageBox, QTableWidget, QTableWidgetItem, QAbstractItemView,
                            QComboBox, QMenu, QTreeWidgetItem, QDirModel)
from PyQt5.QtGui import (QStandardItemModel, QStandardItem, QBrush, QColor, QFont, 
                            )
from PyQt5.QtCore import QStringListModel, Qt
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
        
        # table view 更像是之可以查看的视图
        self.model = QStandardItemModel(4, 3) # 绑定了数据模型
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3'])
        for row in range (1, 5):
            for col in range (1, 4):
                item = QStandardItem(str(row) + str(col))
                # 设置单元格文本颜色
                item.setForeground(QBrush(QColor(144, 182, 240)))
                # 设置单元格字体 不如在designer里面设置
                # 设置单元格 水平竖直居中对齐 
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.model.setItem(row - 1, col - 1, item)

        item = QStandardItem("美国大学生数学建模竞赛")
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setForeground(QBrush(QColor(144, 182, 240)))
        self.model.setItem(0, 0, item)
        # 视图仅进行观察，不可修改 tableview可用的，tablewidget也可以用
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 视图整行选中
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 填充满整个窗口， 标题过长会被遮挡
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.model)

        # 表格的高度宽度与内容相匹配, 与填充满相矛盾
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()

        # 设置单元格大小
        self.tableView.setColumnWidth(0, 300) # 第零列的宽度
        self.tableView.setColumnWidth(1, 150)  # 第一列的宽度
        self.tableView.setColumnWidth(2, 150)  # 第一列的宽度
        self.tableView.setRowHeight(0, 50) # 第一行的高度

        # 合并单元格
        # 绑定了数据模型
        self.model = QStandardItemModel(4, 3) 
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3'])
        self.tableView_2.setModel(self.model)
        # 0, 0 表示起始单元格 1, 2 表示1行两列
        self.tableView_2.setSpan(0, 0, 1, 2)
        self.tableView_2.setSpan(1, 1, 2, 1)
        self.model.setItem(0, 0, QStandardItem("0"))
        self.model.setItem(1, 1, QStandardItem("1"))
        self.model.setItem(2, 1, QStandardItem("2"))  # 不存在
        self.model.setItem(2, 2, QStandardItem("3"))  
        self.tableView_2.setModel(self.model)

        # 不显示垂直表头
        self.tableView.verticalHeader().setVisible(False)

        # listview 
        slm = QStringListModel()
        self.qlist = ['标题1', '标题2', '标题3']
        slm.setStringList(self.qlist)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.clicked_)

        # QTableWidget 
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['队员1', '队员2', '队员3', '比赛名称', '比赛级别'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 表头自适应伸缩
        ls = []
        for i in range(8):
            a = str(i + 1)
            ls.append(a)
        self.tableWidget.setVerticalHeaderLabels(ls)

        for row in range (1, 8):
            for col in range (1, 5):
                item = QTableWidgetItem(str(row) + str(col))
                # 设置单元格文本颜色
                item.setForeground(QBrush(QColor(144, 182, 240)))
                # 设置单元格字体 不如在designer里面设置
                self.tableWidget.setItem(row - 1, col - 1, item)

        # 放置控件
        combox = QComboBox()
        combox.addItem("男")
        combox.addItem("女")
        self.tableWidget.setCellWidget(0, 1, combox)

        # 设置单元格排序方式(视图不能排序)
        self.pushButton.clicked.connect(self.sort_ascend)
        self.pushButton_2.clicked.connect(self.sort_decend)

        # 右键支持菜单选项
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.table_menu)

        # TreeView
        # view是父类，widget是子类
        self.treeWidget.setColumnCount(3) # 三列 designer 里面设计
        self.treeWidget.setHeaderLabels(['人员', '比赛情况', '获奖级别']) # 设置标题
        # 设置根节点
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, "比赛人员") # 0 表示位置
        self.treeWidget.setColumnWidth(1, 200) # 设置宽度
        # 设置子节点
        child_16 = QTreeWidgetItem(root)
        child_16.setText(0, "16级")
        child_ljw = QTreeWidgetItem(child_16)
        child_ljw.setText(0, "刘佳玮")
        child_ljw.setText(1, "美国大学生数学建模竞赛")
        child_ljw.setText(2, "一等奖")
        # 设置节点的背景颜色
        root.setBackground(0, QBrush((QColor(144, 182, 240))))
        root.setBackground(1, QBrush((QColor(144, 214, 240))))
        root.setBackground(2, QBrush((QColor(144, 235, 240))))
        # 节点响应事件
        self.treeWidget.clicked.connect(self.treeclick)
        # 定制系统模式 
        model = QDirModel()
        self.treeView.setModel(model)

    def treeclick(self):
        item = self.treeWidget.currentItem()
        print(item.text(1))

    # 右键排序，视图不能进行排序，因此建议使用不可编辑的tablewidget实现视图
    # 且功能更多 
    def table_menu(self, pos):
        menu = QMenu()
        item1 = menu.addAction("升序")
        item2 = menu.addAction("降序")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        # 获取当前行 列
        # row_num = -1
        col_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            # row_num = i.row()
            col_num = i.column()
        if action == item1:
            self.tableWidget.sortItems(col_num, Qt.AscendingOrder)
        if action == item2:
            self.tableWidget.sortItems(col_num, Qt.DescendingOrder)

    # 第 0 列
    def sort_ascend(self):
        self.tableWidget.sortItems(0, Qt.AscendingOrder)

    def sort_decend(self):
        self.tableWidget.sortItems(0, Qt.DescendingOrder)

    def clicked_(self, qModelIndex):
        print("选择结果" + str(self.qlist[qModelIndex.row()]))

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