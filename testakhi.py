import PyQt5
import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.QtGui
from PyQt5.QtGui import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import random
import sys
import threading
class akhi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.page()
        self.stackLay= QStackedLayout()
        self.stackLay.addWidget(self.PageBox)
        self.stackLay.setCurrentWidget(self.PageBox)

        
        self.Central_widget = QWidget()
        self.Central_widget.setLayout(self.stackedLay)
        
        self.setCentralWidget(self.Central_widget)
        

    def page(self):
        self.lab1 = QLabel("Akhi's page1")
        
        self.Tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.Tabs.addTab(self.tab1, "a-1")
        self.Tabs.addTab(self.tab2, "a-2")

        self.labtab1 = QLabel("This is tab1")
        self.Labtab2 = QLabel("This is tab2")

        self.lay1 = QVBoxLayout()

        self.lay1.addWidget(self.labtab1)
        self.lay1.addWidget(self.Labtab2)

        self.tab1.setLayout(self.lay1)

        self.lay2 = QHBoxLayout()

        self.but1 = QPushButton("button 1")
        self.but1.clicked.connect(self.printIt)
        
        self.but2 = QPushButton("button 2")

        self.lay2.addWidget(self.but1)
        self.lay2.addWidget(self.but2)

        self.tab2.setLayout(self.lay2)

        self.pageLay = QVBoxLayout()
        self.pageLay.addWidget(self.lab1)
        self.pageLay.addWidget(self.Tabs)

        self.PageBox = QWidget()
        self.PageBox.setLayout(self.pageLay)             
        
    def printIt(self):
        print("Hello there")

def man():
    test = QApplication(sys.argv)
    window = akhi()
    window.show()
    window.exec_()

man()




