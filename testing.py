import PyQt5
import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.QtGui
from PyQt5.QtGui import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import random
import sys

def Exp1Page(self):
        print("insideClass")
        tabs = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        #tabs.resize(300,200)
        
        # Add tabs
        tabs.addTab(tab1,"Theory")
        tabs.addTab(tab2,"Perform")
        tabs.addTab(tab3, "Video")
        tabs.addTab(tab4, "Question Bank")
        
        # Create first tab
        '''
        tab1.layout = QVBoxLayout(self)
        pushButton1 = QPushButton("PyQt5 button")
        tab1.layout.addWidget(pushButton1)
        tab1.setLayout(tab1.layout)
        
        # Add tabs to widget
        layout.addWidget(tabs)
        setLayout(layout)
        '''
        
        label = QLabel("1.Standarizing Hypo Solution\n with known concentration of CuSO4")
        label2 = QLabel("Process to prepare standard CuSO4.5H2O solution :")

        weight = QLineEdit()
        #weight.setFixedWidth(100)
        init_bur = 50.00
        n2 = QLineEdit()
        n2.setReadOnly(True)
        ans = QLineEdit()
        ans.setReadOnly(True)
        
        
        label3 = QLabel("Enter weight(grm) of CuSO4.5H2O salt\n(Taken in 100 ml of H2O)")
        WeightLine = QLineEdit()
        WeightLine.setFixedWidth(100)
        WeightLine.returnPressed.connect(getWeight)
        
        
        VolLabel = QLabel("Enter Volume(ml) of CuSO4.5H2O salt\n(Taken in conical flask)")
        VolLine = QLineEdit()
        VolLine.setFixedWidth(100)
        VolLine.setReadOnly(True)
        #vol = QLineEdit()
        VolLine.returnPressed.connect(getvol)
        tempLine = QLineEdit()
        tempLine.setReadOnly(True)
        tempLine.textChanged.connect(randomVol)
        
        label4 = QLabel()
        lab45 = QLabel()
        label5 = QLabel()
        label6 = QLabel()
        
        
        
        label7 = QLabel("2. Finding the strength of unknown CuSO4 solution")
        label8 = QLabel("Enter the Volume(ml) of unknown\n CuSO4.5H2O salt taken")
        Unknown = QLineEdit()
        Unknown.setFixedWidth(100)
        Unknown.setReadOnly(True)
        Unknown.returnPressed.connect(calculate)
        lab9 = QLabel()
        
        label9 = QLabel()
        label10 = QLabel()
        
        label11 = QLabel("Calculate the strength of unknown solution\n Put your answer below :")
        ansLine = QLineEdit()
        ansLine.setFixedWidth(100)
        ansLine.setReadOnly(True)
        ansLine.returnPressed.connect(checkAns)
        correctLabel = QLabel()

        HomeLay = QVBoxLayout()
        
        
        for i in[label, label2, label3, WeightLine, VolLabel, VolLine,
                   label4, lab45, label5, label6, label7, label8,
                   Unknown,lab9, label9, label10, label11, ansLine, correctLabel]:
            HomeLay.addWidget(i)
            
        
        Title = QLabel("DETERMINING THE STRENGTH OF UNKNOWN SOLUTION OF CuSO4")
        Title.setAlignment(Qt.AlignCenter)
        movie2 = QMovie("an2.gif")
        
        #movie2.frameChanged.connect(repaint)
        #print("insideClass1")
        movie = QLabel()
        
        movie.setMovie(movie2)
        movie2.start()
        #print("insideClass2")
        
        #print("insideClassMid")
        movieBox = QVBoxLayout()
        movieBox.addWidget(Title)
        movieBox.addWidget(movie)
        group1 = QGroupBox()
        group1.setLayout(movieBox)
        group2 = QGroupBox()
        group2.setLayout(HomeLay)

        pageBox = QHBoxLayout()
        pageBox.addWidget(group2)
        pageBox.addWidget(group1)
        
        tab2.setLayout(pageBox)
        
        #tab1text = QPlainTextEdit()
        
        l1 = QLabel()
        l1.setPixmap(QPixmap("Copper-1.jpg"))
        #l1.setAlignment(Qt.AlignCenter)
        l1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l1.setAlignment(Qt.AlignCenter)
        l1.setStyleSheet("QLabel {background-color: red;}")
        
        l2 = QLabel()
        l2.setPixmap(QPixmap("Copper-2.jpg"))
        l2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l2.setAlignment(Qt.AlignCenter)
        l2.setStyleSheet("QLabel {background-color: red;}")
        
        tab3text = QPlainTextEdit()
        tab4text = QPlainTextEdit()
        
        tab1Lay = QVBoxLayout()
        tab1Lay.addWidget(l1)
        tab1Lay.addWidget(l2)

        scrollWidget = QWidget()
        scrollWidget.setLayout(tab1Lay)

        scrollAr = QScrollArea()
        scrollAr.setWidget(scrollWidget)
        
        tab3Lay = QVBoxLayout()
        tab3Lay.addWidget(tab3text)
        
        tab4Lay = QVBoxLayout()
        tab4Lay.addWidget(tab4text)
        
        tab1Lay2 = QVBoxLayout()
        tab1Lay2.addWidget(scrollAr)
        
        tab1.setLayout(tab1Lay2)
        tab3.setLayout(tab3Lay)
        tab4.setLayout(tab4Lay)

        backHome = QPushButton("Back")

        
        HomePage_lay = QFormLayout()
        HomePage_lay.addRow(tabs, backHome)
        
       
        
        HomePage_widget = QWidget()
        HomePage_widget.setLayout(HomePage_lay)
        #HomePage_widget.setGeometry(100,100,200,200)
        HomePage_widget.setWindowTitle("Experiment 1")
        print("DONE")
