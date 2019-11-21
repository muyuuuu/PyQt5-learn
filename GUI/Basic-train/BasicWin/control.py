#!/bin/bash
# -*- coding: UTF-8 -*-
import sys
import time
import PyQt5
# 基本控件都在这里面
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QCalendarWidget, QDateTimeEdit, QAction
from PyQt5.QtGui import QIcon, QIntValidator, QPixmap
from PyQt5.QtCore import QDir, QDate, QDateTime
from mainwindow import Ui_MainWindow

# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.resize(1000, 700)

        # 菜单栏 界面中绘制更容易
        # 捕获菜单栏中的选择 可以具体到某一栏
        self.actionA.triggered.connect(self.proccess)
        # file.triggered[QAction].connect(self.proccess)

        # 工具栏
        # 也不如界面绘制更容易
        # tool_bar = self.addToolBar("展示")
        # plot = QAction("绘图展示", self)
        # tool_bar.addAction(plot)
        # table = QAction("表格展示", self)
        # tool_bar.addAction(table)
        self.action_showpic.triggered.connect(self.proccess)

        # 默认的状态栏
        # 可以设置其他按钮点击 参考多行文本显示 然而不行 
        self.status = self.statusBar()
        self.status.showMessage("你在主页面～")
        
        # 标题栏
        self.setWindowTitle("建模协会录入信息")

        # 窗口居中
        self.center()

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)
        
        # 设置图标, MAC OS 风格会看不到
        self.setWindowIcon(QIcon('icon.jpg'))

        # 设置QlineEdit显示默认的字符
        self.lineEdit.setPlaceholderText("认真工作，录入数据~")

        # 数值检验
        month_validator = QIntValidator(self)
        month_validator.setRange(1, 13)
        self.lineEdit_month.setValidator(month_validator)

        year_validator = QIntValidator(self)
        year_validator.setRange(2000, 3000)
        self.lineEdit_year.setValidator(year_validator)

        # 日期掩码作为输入
        self.lineEdit_datemask.setInputMask('0000-00-00')

        # 登录密码设置为 隐藏字符
        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)

        # 多行文本显示
        self.quit_btn_rstquery.clicked.connect(self.query_click)
        # self.quit_btn_rstquery.clicked.connect(self.show_status)

        # 添加比赛项
        self.comboBox.addItem("全国大学生数学建模竞赛")
        self.comboBox.addItem("美国大学生数学建模竞赛")
        self.comboBox.addItem("深圳杯大学生数学建模竞赛")
        self.comboBox.addItem("华为杯研究生数学建模竞赛")
        self.comboBox.addItem("华北理工大学数学建模竞赛")
        self.comboBox.currentIndexChanged.connect(self.label_change)

        # 水平拉条
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(3)
        # 滑动条下方画刻线 和 设置间隔
        self.horizontalSlider.setTickPosition(self.horizontalSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(5)

        # 消息盒练习
        self.quit_btn_rstquery_2.clicked.connect(self.message_box)

        # 输入比赛, 且这种输入方式更加合理
        self.quit_btn_rstquery_3.clicked.connect(self.input_dia)

        # 打开 图片文件
        self.quit_btn_rstquery_5.clicked.connect(self.open_pic)

        # 打开 文本文件, 适合在另一个对话框内打开，不影响界面
        self.quit_btn_rstquery_4.clicked.connect(self.open_file)

        # 保存 文本文件， 实现保存文件
        self.quit_btn_rstquery_6.clicked.connect(self.save_file)

        # 录入日期
        self.calendarWidget.setMinimumDate(QDate(2015, 1, 1))
        self.calendarWidget.setMaximumDate(QDate(3000, 1, 1))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.clicked.connect(self.show_time)

        # 弹出日历
        self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-1095))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.dateTimeChanged.connect(self.time_change)

    # 捕获菜单栏中的选择
    def proccess(self):
        print("success")

    # 时间变化就改变
    def time_change(self, time):
        time = time.toString()
        print(time)

    # 显示选中的时间
    def show_time(self, date):
        date = date.toString("yyyy年MM月dd日")
        # print(date[0:4]) # 不如对切片命名
        self.textEdit.setText(date)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self,'save file')
        with open(filename[0],'w') as f:
            my_text = self.textEdit.toPlainText()
            f.write(my_text)
        
    def open_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)

        if dlg.exec_():
            filename = dlg.selectedFiles()
            with open(filename[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

    def open_pic(self):
        # 注意到windows下切换路径
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', "Image files (*.jpg *.png)")
        # size = self.label_8.size()
        # 还需要对图片进行重新调整大小
        self.label_8.setPixmap(QPixmap(fname))
        # print(size)

    def input_dia(self):
        # 空格撑开距离，看着舒服
        items = (        
            "      全国大学生数学建模竞赛     ",
            "      美国大学生数学建模竞赛      ",
            "      深圳杯大学生数学建模竞赛      ",
            "      华为杯研究生数学建模竞赛      ",
            "      华北理工大学数学建模竞赛      "
        )
        item, ok = QInputDialog.getItem(self, "从这里面选择比赛哦", "比赛列表", items, 0, False)
        if ok and item:
            # item 需要删除左右两边的空格
            self.label_7.setText(item)

    # 消息盒显示输入错误
    def message_box(self):
        reply = QMessageBox.about(self, "你犯了一个粗误", "请重新检查输入")
        # reply.setWindowIcon() # 更换图片
        # time.sleep(2)
        
    # 下拉列表改变时，label文字跟随变化
    def label_change(self):
        self.label_7.setText(self.comboBox.currentText())

    def query_click(self):
        # 单选框选中 则显示男孩，否则是女孩
        # 判断哪个复选框被选中
        # group 对框画界限
        if self.radioButton.isChecked() == True:
            if self.checkBox_1.isChecked() == True:
                self.textEdit.setHtml("<font color = 'blue' size = 5>hello  boy 1</font>")
            if self.checkBox_2.isChecked() == True:
                self.textEdit.setHtml("<font color = 'blue' size = 5>hello  boy 1</font>")
        else:
            self.textEdit.setHtml("<font color = 'blue' size = 5>hello  girl</font>")
        
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