
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exp2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import random
import sys
class Ui_ScrollArea(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        print("inside")
        #self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("Idonation with Acetone")
        ScrollArea = QtWidgets.QScrollArea()
        #ui = Ui_ScrollArea()
        self.setupUi(ScrollArea)
        print("ok1")
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tab4 = QtWidgets.QWidget()

        self.tabs.addTab(self.tab1,"Theory")
        self.tabs.addTab(self.tab2,"Perform")
        self.tabs.addTab(self.tab3, "Video")
        self.tabs.addTab(self.tab4, "Question Bank")

        self.tab2Lay = QtWidgets.QHBoxLayout()
        self.tab2Lay.addWidget(ScrollArea)

        self.sideAni = QtGui.QMovie("graph2.gif")
        #self.sideAni.frameChanged.connect(self.repaint)
        self.sideAniLab = QtWidgets.QLabel()

        self.sideAni2 = QtGui.QMovie("graph7.gif")
        #self.sideAni.frameChanged.connect(self.repaint)
        self.sideAniLab2 = QtWidgets.QLabel()

        self.grp1Lay = QtWidgets.QVBoxLayout()
        self.grp1Lay.addWidget(self.sideAniLab)
        self.grp1Lay.addWidget(self.sideAniLab2)

        self.grpBox = QtWidgets.QWidget()
        self.grpBox.setLayout(self.grp1Lay)
        
        self.sideAniLab.setMovie(self.sideAni)
        self.sideAni.start()
        
        self.sideAniLab2.setMovie(self.sideAni2)
        self.sideAni2.start()
        self.tab2Lay.addWidget(self.grpBox)
        
        self.tab2.setLayout(self.tab2Lay)

        self.l1 = QtWidgets.QLabel()
        self.l1.setPixmap(QPixmap("Iodination-1.jpg"))
        self.l1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.l2 = QtWidgets.QLabel()
        self.l2.setPixmap(QPixmap("Iodination-2.jpg"))
        self.l2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.l3 = QtWidgets.QLabel()
        self.l3.setPixmap(QPixmap("Iodination-3.jpg"))
        self.l3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.l4 = QtWidgets.QLabel()
        self.l4.setPixmap(QPixmap("Iodination-4.jpg"))
        self.l4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.tab1Lay = QtWidgets.QVBoxLayout()
        self.tab1Lay.addWidget(self.l1)
        self.tab1Lay.addWidget(self.l2)
        self.tab1Lay.addWidget(self.l3)
        self.tab1Lay.addWidget(self.l4)

        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setLayout(self.tab1Lay)

        self.scrollAr = QtWidgets.QScrollArea()
        self.scrollAr.setWidget(self.scrollWidget)
        
        self.tab1Lay2 = QtWidgets.QVBoxLayout()
        self.tab1Lay2.addWidget(self.scrollAr)
        self.tab1.setLayout(self.tab1Lay2)

        self.tab3text = QtWidgets.QPlainTextEdit()
        self.tab4text = QtWidgets.QPlainTextEdit()

        self.tab3Lay = QtWidgets.QVBoxLayout()
        self.tab3Lay.addWidget(self.tab3text)
        
        self.tab4Lay = QtWidgets.QVBoxLayout()
        self.tab4Lay.addWidget(self.tab4text)

        self.tab3.setLayout(self.tab3Lay)
        self.tab4.setLayout(self.tab4Lay)

        self.setCentralWidget(self.tabs)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setGeometry(90,40,1200,600)
        self.show()
        
    def setupUi(self, ScrollArea):
        ScrollArea.setObjectName("ScrollArea")
        ScrollArea.resize(638, 1128)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScrollArea.sizePolicy().hasHeightForWidth())
        ScrollArea.setSizePolicy(sizePolicy)
        ScrollArea.setFrameShape(QtWidgets.QFrame.WinPanel)
        ScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        ScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        ScrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 620, 1124))
        #self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget.setGeometry(QtCore.QRect(27, 61, 498, 92))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_17)
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_18)
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_19)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(45, 42, 194, 17))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(3, 180, 630, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(62, 213, 505, 152))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(4, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setGeometry(QtCore.QRect(163, 242, 100, 32))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(262, 242, 100, 32))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(362, 242, 100, 32))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(463, 243, 100, 32))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(163, 273, 100, 32))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(263, 272, 100, 32))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(363, 273, 100, 32))
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(462, 271, 100, 32))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(163, 301, 100, 32))
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_10.setGeometry(QtCore.QRect(263, 302, 100, 32))
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_11.setGeometry(QtCore.QRect(362, 302, 100, 32))
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_12.setGeometry(QtCore.QRect(462, 301, 100, 32))
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_13.setGeometry(QtCore.QRect(162, 332, 100, 32))
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_14.setGeometry(QtCore.QRect(262, 332, 100, 32))
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_15.setGeometry(QtCore.QRect(363, 331, 100, 32))
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_16.setGeometry(QtCore.QRect(463, 331, 100, 32))
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(2, 401, 631, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(106, 377, 434, 25))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(258, 423, 141, 161))
        self.groupBox.setObjectName("groupBox")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(12, 28, 123, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet("QLCDNumber { background-color: red }")
        self.dial = QtWidgets.QDial(self.groupBox)
        self.dial.setGeometry(QtCore.QRect(49, 55, 50, 64))
        self.dial.setMouseTracking(False)
        self.dial.setMaximum(1000)
        self.dial.setObjectName("dial")
        self.dial.valueChanged.connect(lambda: self.dial_method())
        
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(26, 130, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(91, 51, 44, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setGeometry(QtCore.QRect(0, 605, 631, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea)

    def retranslateUi(self, ScrollArea):
        _translate = QtCore.QCoreApplication.translate
        ScrollArea.setWindowTitle(_translate("ScrollArea", "Experiment 2"))
        self.label_2.setText(_translate("ScrollArea", "Enter weight of Acetone(in grams)"))
        self.label_3.setText(_translate("ScrollArea", "Enter weight of HCl (in grams)"))
        self.label_4.setText(_translate("ScrollArea", "Enter weight of I<sub>2</sub> (in grams)"))
        self.label.setText(_translate("ScrollArea", "Stock Solution preparation:"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("ScrollArea", "Acetoen(in ml)"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("ScrollArea", "HCl(in ml)"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("ScrollArea", "H2O(in ml)"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("ScrollArea", "Iodine(in ml)"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("ScrollArea", "Trial 1"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("ScrollArea", "Trial 2"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("ScrollArea", "Trial 3"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("ScrollArea", "Trial 4"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("ScrollArea", "Click to confirm the readings "))
        self.pushButton.clicked.connect(lambda:self.Perdormexp())
        self.groupBox.setTitle(_translate("ScrollArea", "spectrophotometer"))
        self.pushButton_2.setText(_translate("ScrollArea", "Start"))
        
        self.pushButton_2.clicked.connect(lambda:self.chechValue())

        self.label_7.setText(_translate("ScrollArea", "λ (in nm)"))
        

    def dial_method(self):
        self.lcdNumber.display(self.dial.value())


    def Perdormexp(self):
        #calculate molarity of stock solution
        self.m1_acetone=(self.doubleSpinBox_17.value()/58.08)/0.1
        self.m1_hcl=(self.doubleSpinBox_18.value()/36.46)/0.1
        self.m1_iodine=(self.doubleSpinBox_19.value()/253.8089)/0.1

        #Calculate molarity for volumes used in trial 1
        self.total_volume_trial_1=self.doubleSpinBox.value()+self.doubleSpinBox_2.value()+self.doubleSpinBox_3.value()+self.doubleSpinBox_4.value()
        self.m1_acetone_trial1=(self.m1_acetone*self.doubleSpinBox.value())/self.total_volume_trial_1
        self.m1_hcl_trial1=(self.m1_hcl*self.doubleSpinBox_2.value())/self.total_volume_trial_1
        self.m1_iodine_trial1=(self.m1_iodine*self.doubleSpinBox_4.value())/self.total_volume_trial_1

        #Calculate molarity for volumes used in trial 2
        self.total_volume_trial_2=self.doubleSpinBox_5.value()+self.doubleSpinBox_6.value()+self.doubleSpinBox_7.value()+self.doubleSpinBox_8.value()
        self.m1_acetone_trial2=(self.m1_acetone*self.doubleSpinBox_5.value())/self.total_volume_trial_2
        self.m1_hcl_trial2=(self.m1_hcl*self.doubleSpinBox_6.value())/self.total_volume_trial_2
        self.m1_iodine_trial2=(self.m1_iodine*self.doubleSpinBox_8.value())/self.total_volume_trial_2

        #Calculate molarity for volumes used in trial 3
        self.total_volume_trial_3=self.doubleSpinBox_9.value()+self.doubleSpinBox_10.value()+self.doubleSpinBox_11.value()+self.doubleSpinBox_12.value()
        self.m1_acetone_trial3=(self.m1_acetone*self.doubleSpinBox_9.value())/self.total_volume_trial_3
        self.m1_hcl_trial3=(self.m1_hcl*self.doubleSpinBox_10.value())/self.total_volume_trial_3
        self.m1_iodine_trial3=(self.m1_iodine*self.doubleSpinBox_12.value())/self.total_volume_trial_3

        #Calculate molarity for volumes used in trial 4
        self.total_volume_trial_4=self.doubleSpinBox_13.value()+self.doubleSpinBox_14.value()+self.doubleSpinBox_15.value()+self.doubleSpinBox_16.value()
        self.m1_acetone_trial4=(self.m1_acetone*self.doubleSpinBox_13.value())/self.total_volume_trial_4
        self.m1_hcl_trial4=(self.m1_hcl*self.doubleSpinBox_14.value())/self.total_volume_trial_4
        self.m1_iodine_trial4=(self.m1_iodine*self.doubleSpinBox_16.value())/self.total_volume_trial_4

    
    def chechValue(self):
        if self.dial.value()==545:
            self.Spectoscopy(ScrollArea)
        else:
            msgBox=QMessageBox()
            msgBox.setText("Error No Data available for mentioned Wavelength")
            msgBox.exec()
            


        

    def Spectoscopy(self,ScrollArea):
        _translate = QtCore.QCoreApplication.translate
        self.k=random.randint(-4,5)
        self.k=28+self.k
        self.k=self.k/1000000
        self.k_dash_trial1=self.k*self.m1_acetone_trial1*self.m1_hcl_trial1
        self.k_dash_trial2=self.k*self.m1_acetone_trial2*self.m1_hcl_trial2
        self.k_dash_trial3=self.k*self.m1_acetone_trial3*self.m1_hcl_trial3
        self.k_dash_trial4=self.k*self.m1_acetone_trial4*self.m1_hcl_trial4
        self.t=0
        key=int(1)
        sys.stdout = open("lab_record.txt", "w+")
        print("trial 1")
        print("Time(sec)\tabsorbance")
        while(self.t<1800):
            self.a=0.3636*(self.m1_iodine_trial1-self.k_dash_trial1*t)
            print(self.t,"\t",self.a)
            t=t+30
        self.t=0
        print("trial 2")
        print("Time(sec)\tabsorbance")    
        while(self.t<1800):
            self.a=0.3636*(self.m1_iodine_trial2-self.k_dash_trial2*t)
            print(self.t,"\t",a)
            self.t=self.t+30
        self.t=0
        print("trial 3")
        print("Time(sec)\tabsorbance")
        while(self.t<1800):
            a=0.3636*(self.m1_iodine_trial3-self.k_dash_trial3*t)
            print(t,"\t",a)
            t=t+30
        t=0
        print("trial 4")
        print("Time(sec)\tabsorbance")
        while(t<1800):
            self.a=0.3636*(self.m1_iodine_trial4-self.k_dash_trial4*t)
            print(self.t,"\t",self.a)
            self.t=self.t+30
        msgBox=QMessageBox()
        msgBox.setText("Sucessful, The record has been saved to your pc in the file folder")
        msgBox.exec()
        
        sys.stdout.close()
#if __name__ == "__main__":
    


