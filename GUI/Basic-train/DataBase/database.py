#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import time
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget,
                             QMessageBox, QTableView)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
# 导入数据库
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from mainwidget import Ui_Form
from mainwindow import Ui_MainWindow

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWidget(QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(MyMainWidget, self).__init__(parent)
        self.setupUi(self)

        self.setLayout(self.gridLayout)

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)

        # 链接sql与查询
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('table/test.db')
        self.db.open()
        if not self.db.open():
            QMessageBox.critical(None, ("无法打开数据库"), ("SQlite支持"), QMessageBox.Cancel)
            return False

        self.model = QSqlTableModel()

        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.query)
        self.pushButton_3.clicked.connect(self.insert_oneline)
        self.pushButton_4.clicked.connect(self.del_oneline)
        self.pushButton_5.clicked.connect(self.find_row)

    # 打印行列号
    def find_row(self):
        print(self.view.currentIndex().row() + 1, self.view.currentIndex().column() + 1)

    # 删除一行
    def del_oneline(self):
        self.model.removeRow(self.view.currentIndex().row())
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.view.setModel(self.model)
        self.view.show()       

    # 插入一行
    def insert_oneline(self):
        self.model.insertRows(self.model.rowCount(), 1)
        # print(str(ret))

    def query(self):
        self.model.setTable("people")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # self.model.setFilter("id > 1")
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Address")
        self.view.setModel(self.model)
        self.view.show()

    def insert(self):
        query = QSqlQuery()
        # query.exec_("create table people(id int primary key, name varchar(20), address varchar(30))")
        # query.exec_("insert into people values(1, 'one', 'test1')")
        # query.exec_("insert into people values(2, 'two', 'test2')")
        # query.exec_("insert into people values(3, 'three', 'test3')")
        # query.exec_("insert into people values(4, 'four', 'test4')")
        for i in range (6, 100):
            query.exec_("insert into people values({}, 'test', 'test{}')".format(i, i))

    def quit_act(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text() + '键被按下')
        qApp = QApplication.instance()
        self.db.close()
        qApp.quit()


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.q = MyMainWidget()
        self.setCentralWidget(self.q)

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

    def closeEvent(self, e):
        self.q.db.close()


if __name__ == "__main__":
    # 在shell中执行
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    # 开始主循环，直到退出
    sys.exit(app.exec())
