# Introduction

- The Basic-train floder
  - AdvanWin
    - Container: QStackedWidget, QTabWidget, QDockWidget, verticalScrollBar.
    - ViewWidget: tableview, listview, tableWidget, combox, treeWidget.
    - WebPage: webEngineView(It is recommended to call the system browser to open the webpage instead of the software.)
  - BasicWin
  - DataBase
  - MatplotWidget
  - Pyecharts
  - PyQtGraph
  - QSS
  - QtPandas

# Basic-train floder

- QtPandas: Using pyqt5's window to view and edit data with pandas. (Attention: pandas version 0.23 will be needed not the latest version)

![](3.png)

- QSS: Using Qt style sheet to beautify the interface. (Suggestion: Using qss written by others, such as qdarkstyle)
- PyQtGraph: A simple and fast way to draw in a window.

![](3.gif)

- Pyecahrts: Integrating web page drawing in the window.

![](4.gif)

- MatplotWidget: Integrating Matplotlib to draw in the window.(more powerful)

![](5.gif)

- DataBase: Connecting database by pyqt. (Not recommended, it is recommended to connect to the database directly with python)
- BasicWin: Contains basic controls such as buttons, calendars, input boxes, comboBox, label, etc.(recommending learn it carefully)

![](4.png)

- AdvanWin:
  - Container: tabwidget, listwidget to hold control
  - ViewWidget: To view and edit table conveniently, also can show result which from query of database.
  - WebPage: To load and show web page in a window.

# Attention

Some `.py` file based on `.ui` file, the software qtdesigner can open and edit `.ui` file and generate the same name `.py` file correspondingly.

So, don't change `.ui` file unless you know what you are doing.

#　Ｍore detailed description:

If you know chinese, the following website is a good choice.

About basic and advanced control(tabwidget and button, etc.): https://muyuuuu.github.io/2019/10/06/pyqt5-basic/

Matplotlib, qtpandas, database, etc: https://muyuuuu.github.io/2019/10/11/pyqt-pit/

Layout and beautify window: https://muyuuuu.github.io/2019/10/19/pyqt-layout/

A beautiful and applicable interface: https://github.com/muyuuuu/A-Beautiful-PyQt5-Interface

![](1.gif)