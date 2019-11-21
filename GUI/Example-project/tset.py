
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget,
                            QGridLayout, QHeaderView, QTableWidgetItem, QMessageBox, QFileDialog,
                            QStackedLayout, QFrame, QLabel, QLineEdit, QPushButton, QTableWidget, QVBoxLayout,
                            QHBoxLayout, QSplitter)
from PyQt5.QtGui import QPalette, QColor, QBrush

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(layout)

        for n, color in enumerate(['red','green','blue','yellow']):
            btn = QPushButton( str(color) )
            btn.pressed.connect( lambda n=n: layout.setCurrentIndex(n) )
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()