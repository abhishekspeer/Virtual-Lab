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
class VlabWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("Virtual Chem-labs")
        self.DefPage()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.DefPage_widget)
        self.stacked_layout.setCurrentIndex(0)
        self.Central_widget = QWidget()
        self.Central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.Central_widget)


    def DefPage(self):
        self.head = QLabel("VIRTUAL LABORATORY-1.0.0")
        self.head.setAlignment(Qt.AlignCenter)
        
        self.but1 = QPushButton("Experiment 1")
        self.but1.clicked.connect(self.exp1)
        
        self.but2 = QPushButton("Experiment 2")
        self.but3 = QPushButton("Experiment 3")
        self.but4 = QPushButton("Experiment 4")
        self.defLab = QLabel("Calculation of strength of ")
        self.defLab2 = QLabel("Ph acid - base titration")
        self.defLab3 = QLabel("experiment 3")
        self.defLab4 = QLabel("experiment 4") 

        self.defLay = QFormLayout()

        for i, j in zip([self.but1, self.but2, self.but3, self.but4],
                        [self.defLab, self.defLab2, self.defLab3, self.defLab4]):
            self.defLay.addRow(i, j)

        
        self.defGr1 = QGroupBox()
        self.defGr1.setLayout(self.defLay)
        self.defLab5 = QLabel("Last performed remarks :")
        self.defLab5.setAlignment(Qt.AlignLeft)
        self.TEXT_BOX_H = QPlainTextEdit()
        #self.TEXT_BOX_H.setMaximumWidth(135)
        self.TEXT_BOX_H.setReadOnly(True)
        
        self.defPageLay = QVBoxLayout()
        self.defPageLay.addWidget(self.head)
        self.defPageLay.addWidget(self.defGr1)
        self.defPageLay.addWidget(self.defLab5)
        self.defPageLay.addWidget(self.TEXT_BOX_H)

        self.sideAni = QMovie("ani1.gif")
        self.sideAni.frameChanged.connect(self.repaint)
        self.sideAniLab = QLabel()
        self.sideAniLab.setMovie(self.sideAni)
        self.sideAni.start()

        self.defGr2 = QGroupBox()
        self.defGr2.setLayout(self.defPageLay)

        self.DefBox = QHBoxLayout()
        self.DefBox.addWidget(self.defGr2)
        self.DefBox.addWidget(self.sideAniLab)

        self.DefPage_widget = QWidget()
        self.DefPage_widget.setLayout(self.DefBox)
        #self.HomePage_widget.setGeometry(100,100,200,200)
        self.DefPage_widget.setWindowTitle("Chem OnLine")
        
        
    def exp1(self):
       
        try:
            self.stacked_layout.setCurrentWidget(self.HomePage_widget)
        except:
            self.HomePage()
            self.stacked_layout.addWidget(self.HomePage_widget)
            self.stacked_layout.setCurrentWidget(self.HomePage_widget)



    def HomePage(self):
        
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        #self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Theory")
        self.tabs.addTab(self.tab2,"Perform")
        self.tabs.addTab(self.tab3, "Video")
        self.tabs.addTab(self.tab4, "Question Bank")
        
        # Create first tab
        '''
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        '''
        
        self.label = QLabel("1.Standarizing Hypo Solution\n with known concentration of CuSO4")
        self.label2 = QLabel("Process to prepare standard CuSO4.5H2O solution :")

        self.weight = QLineEdit()
        #self.weight.setFixedWidth(100)
        self.init_bur = 50.00
        self.n2 = QLineEdit()
        self.n2.setReadOnly(True)
        self.ans = QLineEdit()
        self.ans.setReadOnly(True)

        
        self.label3 = QLabel("Enter weight(grm) of CuSO4.5H2O salt\n(Taken in 100 ml of H2O)")
        self.WeightLine = QLineEdit()
        self.WeightLine.setFixedWidth(100)
        self.WeightLine.returnPressed.connect(self.getWeight)
        
        self.VolLabel = QLabel("Enter Volume(ml) of CuSO4.5H2O salt\n(Taken in conical flask)")
        self.VolLine = QLineEdit()
        self.VolLine.setFixedWidth(100)
        self.VolLine.setReadOnly(True)
        #self.vol = QLineEdit()
        self.VolLine.returnPressed.connect(self.getvol)
        self.tempLine = QLineEdit()
        self.tempLine.setReadOnly(True)
        self.tempLine.textChanged.connect(self.randomVol)
        
        self.label4 = QLabel()
        self.lab45 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()
        
        
        
        self.label7 = QLabel("2. Finding the strength of unknown CuSO4 solution")
        self.label8 = QLabel("Enter the Volume(ml) of unknown\n CuSO4.5H2O salt taken")
        self.Unknown = QLineEdit()
        self.Unknown.setFixedWidth(100)
        self.Unknown.setReadOnly(True)
        self.Unknown.returnPressed.connect(self.calculate)
        self.lab9 = QLabel()
        
        self.label9 = QLabel()
        self.label10 = QLabel()
        
        self.label11 = QLabel("Calculate the strength of unknown solution\n Put your answer below :")
        self.ansLine = QLineEdit()
        self.ansLine.setFixedWidth(100)
        self.ansLine.setReadOnly(True)
        self.ansLine.returnPressed.connect(self.checkAns)
        self.correctLabel = QLabel()

        self.HomeLay = QVBoxLayout()
        

        for i in[self.label, self.label2, self.label3, self.WeightLine, self.VolLabel, self.VolLine,
                   self.label4, self.lab45, self.label5, self.label6, self.label7, self.label8,
                   self.Unknown,self.lab9, self.label9, self.label10, self.label11, self.ansLine, self.correctLabel]:
            self.HomeLay.addWidget(i)
            
        
        self.Title = QLabel("DETERMINING THE STRENGTH OF UNKNOWN SOLUTION OF CuSO4")
        self.Title.setAlignment(Qt.AlignCenter)
        self.movie2 = QMovie("an2.gif")
        self.movie2.frameChanged.connect(self.repaint)
        self.movie = QLabel()
        self.movie.setMovie(self.movie2)
        self.movie2.start()

        

        self.movieBox = QVBoxLayout()
        self.movieBox.addWidget(self.Title)
        self.movieBox.addWidget(self.movie)
        self.group1 = QGroupBox()
        self.group1.setLayout(self.movieBox)
        self.group2 = QGroupBox()
        self.group2.setLayout(self.HomeLay)

        self.pageBox = QHBoxLayout()
        self.pageBox.addWidget(self.group2)
        self.pageBox.addWidget(self.group1)
        
        self.tab2.setLayout(self.pageBox)
        
        #self.tab1text = QPlainTextEdit()
        
        self.l1 = QLabel()
        self.l1.setPixmap(QPixmap("Copper-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setStyleSheet("QLabel {background-color: red;}")
        
        self.l2 = QLabel()
        self.l2.setPixmap(QPixmap("Copper-2.jpg"))
        self.l2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l2.setAlignment(Qt.AlignCenter)
        self.l2.setStyleSheet("QLabel {background-color: red;}")
        
        self.tab3text = QPlainTextEdit()
        self.tab4text = QPlainTextEdit()
        
        self.tab1Lay = QVBoxLayout()
        self.tab1Lay.addWidget(self.l1)
        self.tab1Lay.addWidget(self.l2)

        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.tab1Lay)

        self.scrollAr = QScrollArea()
        self.scrollAr.setWidget(self.scrollWidget)
        
        self.tab3Lay = QVBoxLayout()
        self.tab3Lay.addWidget(self.tab3text)
        
        self.tab4Lay = QVBoxLayout()
        self.tab4Lay.addWidget(self.tab4text)
        
        self.tab1Lay2 = QVBoxLayout()
        self.tab1Lay2.addWidget(self.scrollAr)
        
        self.tab1.setLayout(self.tab1Lay2)
        self.tab3.setLayout(self.tab3Lay)
        self.tab4.setLayout(self.tab4Lay)

        self.backHome = QPushButton("Back")
        self.backHome.clicked.connect(self.goBackToDef)
        
        self.HomePage_lay = QFormLayout()
        self.HomePage_lay.addRow(self.tabs, self.backHome)
        
       
        
        self.HomePage_widget = QWidget()
        self.HomePage_widget.setLayout(self.HomePage_lay)
        #self.HomePage_widget.setGeometry(100,100,200,200)
        self.HomePage_widget.setWindowTitle("Experiment 1")

    def goBackToDef(self):
        self.stacked_layout.setCurrentWidget(self.DefPage_widget)
    def getWeight(self):
        try:
            flo = float(self.WeightLine.text())
            #print("ok")
            self.label4.setText("Processing.....")
            #print("ok2")
            self.weight.setText(str(flo))
            #print("ok3")
            self.VolLine.setReadOnly(False)
        except:
            self.WeightLine.setText("")
            self.errorMessage()
        
    def getvol(self):
        try:
            f = float(self.VolLine.text())
            #self.vol = f
            init_bur = 50.00
            
            self.lab45.setText("Following are the burrette readings")
            print("ok1")
            self.label5.setText("Initial Reading : "+str(init_bur)+ " ml")
            print("ok2")
            self.tempLine.setText(str(f))
            print("ok3")
            self.Unknown.setReadOnly(False)
            
        except:
            self.VolLine.setText("")
            self.errorMessage()
            
    def randomVol(self):
        f = float(self.tempLine.text())
        k = float(random.randint(10000, 40000))
        final_bur = k/1000
        we = float(self.weight.text())
        self.label6.setText("Final Reading : "+str(final_bur)+ " ml")
        n1 = we/249.68
        v2 = 50.00-f
        n2 = (n1*f)/v2
        self.n2.setText(str(n2))
            
    def calculate(self):
        try:
            n2 = float(self.n2.text())
            v3 = float(self.Unknown.text())
            k = float(random.randint(9000, 45000))
            v4 = k/1000
            self.lab9.setText("Following are the burrette readings")
            self.label9.setText("Initial Reading : "+str(self.init_bur)+ " ml")
            self.label10.setText("Final Reading : "+str(v4)+" ml")
            vlo4 = 50.00-v4
            n3 = (n2*vlo4)/v3
            self.ans.setText(str(n3))
            self.ansLine.setReadOnly(False)
        except:
            self.Unknown.setTeext("")
            self.errorMessage()
    def checkAns(self):
        try:
            an = float(self.ans.text())
            an = round(an, 3)
            user = float(self.ansLine.text())
            
            if(user >= an*0.95 and user <= an*1.05):
                self.correctLabel.setText("Correct Answer !")
            else:
                self.correctLabel.setText("Incorrect ! Ans = "+str(an))
        except :
            print("error in checkAns")

    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        self.w.setIcon(QMessageBox.Warning)
        self.w.setInformativeText("Invalid entry !")
        self.w.setWindowTitle("Warning")
        self.w.exec()      
    
def main(app):
    Vlab = app
    VlabWind = VlabWindow()
    VlabWind.show()
    VlabWind.raise_()
    Vlab.exec_()


