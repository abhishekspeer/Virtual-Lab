from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QMovie, QIcon
from PyQt5.QtWidgets import QSizePolicy, QFileDialog, QPlainTextEdit, QMainWindow, QApplication, QMessageBox, QStackedLayout, QWidget, QLabel, QGridLayout,QLineEdit, QPushButton, QTabWidget, QGroupBox
from datetime import datetime
from common import EXP_BUTTON, EXP_PAGE
from ModWidgets import TableMod
from EXP1 import Exp1_class
from EXP2 import Exp2_class
from EXP3 import Exp3_class
from EXP4 import Exp4_class
from EXP5 import Exp5_class
from EXP6 import Exp6_class
import sys
import os
import sheets
remark = []
k = 0
exp2 = 0

class VlabWindow(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Chem-labs")
        
        ret = sheets.getValidity()
        if(ret == False):
            for i in [self.Submit1, self.Submit2, self.submit3, self.submit4] :
                i.setEnabled(False)
        self.stacked_layout = QStackedLayout()
        self.DefPage()
        self.stacked_layout.addWidget(self.DefPage_widget)
        self.stacked_layout.setCurrentIndex(0)
        self.Central_widget = QWidget()
        #self.Central_widget.setMaximumHeight(720)
        self.Central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.Central_widget)
        self.setWindowIcon(QIcon(EXP_PAGE.resource_path(self, 'media/icon.ico')))
        
    def DefPage(self):
        self.head = QLabel("VIRTUAL LABORATORY")
        self.head.setAlignment(Qt.AlignCenter)

        self.but1 = EXP_BUTTON(" Experiment 1 ", self.stacked_layout, "Iodometery", Exp1_class(self.stacked_layout), self)
        self.but2 = EXP_BUTTON(" Experiment 2 ", self.stacked_layout, "Photometery", Exp2_class(self.stacked_layout), self)
        self.but3 = EXP_BUTTON(" Experiment 3 ", self.stacked_layout, "Equilibrium", Exp3_class(self.stacked_layout), self)
        self.but4 = EXP_BUTTON(" Experiment 4 ", self.stacked_layout, "Conductometery", Exp4_class(self.stacked_layout), self)
        self.but5 = EXP_BUTTON(" Experiment 5 ", self.stacked_layout, "Hardness", Exp5_class(self.stacked_layout), self)
        self.but6 = EXP_BUTTON(" Experiment 6 ", self.stacked_layout, "Saponification", Exp6_class(self.stacked_layout), self)
        self.defLab = QLabel("Estimation of Cu by Iodometry")
        self.defLab2 = QLabel("Iodination using photometry")
        self.defLab3 = QLabel("Equilibrium Constant calculation")
        self.defLab4 = QLabel("Dissociation Constant by conductometry") 
        self.defLab5 = QLabel("Total Hardness of Water") 
        self.defLab6 = QLabel("Saponification Value of Oil") 

        self.defLay = QGridLayout()

        for i, j,k in zip([self.but1, self.but2, self.but3, self.but4, self.but5, self.but6],
                        [self.defLab, self.defLab2, self.defLab3, self.defLab4, self.defLab5, self.defLab6],
                        [1, 2, 3, 4,5,6]):
            self.defLay.addWidget(i, k, 0, 1, 1)
            self.defLay.addWidget(j, k, 1, 1, 2)
            i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.cb = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget() 
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.cb.addTab(self.tab1,"Exp 1")
        self.cb.addTab(self.tab2,"Exp 2")
        self.cb.addTab(self.tab3,"Exp 3")
        self.cb.addTab(self.tab4,"Exp 4")
        self.cb.addTab(self.tab5,"Exp 5")
        self.cb.addTab(self.tab6,"Exp 6")
        self.createSUB()
        #self.cb.setFont(QFont('Times', 12))
        
        self.defGr1 = QGroupBox()
        self.defGr1.setLayout(self.defLay)

        self.defLab5 = QLabel("Last performed remarks :")

        self.defLab5.setAlignment(Qt.AlignLeft)
        self.TEXT_BOX_H = QLabel("USER_ID_NO :" + remark[1]+"\n")
        flag2 = 0
        flag = 1
        
        self.RemarkTab = TableMod(2, 5) 
        for i in remark:
            if(flag2 < 4):
                flag2 +=1
                continue
            self.RemarkTab.setCellWidget(0, flag-1, QPushButton("Exp-"+str(flag)))
            self.RemarkTab.setCellWidget(1, flag-1, QLabel(i))
            flag += 1

        if(flag == 1):
            self.RemarkTab = QPlainTextEdit()
            self.RemarkTab.setPlainText("Login Time :\n"+str(datetime.now()))
            self.RemarkTab.setReadOnly(True)
        
        self.defPageLay = QGridLayout()

        self.welComeUser = QLabel("Welcome "+remark[0])
        self.welComeUser.setFont(QFont('Times', 15))

        self.defPageLay.addWidget(self.head, 0, 1, 2, 8)
        self.defPageLay.addWidget(self.welComeUser, 2, 0, 1, 5)

        self.defPageLay.addWidget(self.defGr1, 4, 0, 8, 10)

        self.defPageLay.addWidget(self.defLab5, 12, 0, 1, 10)
        self.defPageLay.addWidget(self.TEXT_BOX_H, 13, 0, 1, 10)
        self.defPageLay.addWidget(self.RemarkTab, 14, 0, 3, 10)
        self.defPageLay.addWidget(self.cb, 17, 0, 8, 10)

        self.sideAni = QMovie(EXP_PAGE.resource_path(self, "media/ani1.gif"))
        
        self.sideAni.frameChanged.connect(self.repaint)
        self.sideAniLab = QLabel()
        self.sideAniLab.setMovie(self.sideAni)
        self.sideAniLab.setAlignment(Qt.AlignCenter)
        self.sideAni.start()

        self.defGr2 = QGroupBox()
        self.defGr2.setLayout(self.defPageLay)

        self.DefBox = QGridLayout()
        self.DefBox.addWidget(self.defGr2, 0,0, 1, 10)
        self.DefBox.addWidget(self.sideAniLab, 0, 11, 1, 30)

        self.Data = 0

        self.DefPage_widget = QWidget()
        
        self.DefPage_widget.setLayout(self.DefBox)

        self.DefPage_widget.setWindowTitle("WELCOME "+remark[1])        

    def createSUB(self):
        weight = QLabel("Wt of CuSO4.5H20 (in gm) used for stock:")
        self.weightLine = QLineEdit()
        mm = QLabel("Moles of CuSO4 in stock soln.")
        self.mmLine = QLineEdit()
        
        st = QLabel("Str. of CuSO4  Stock Soln (M):")
        self.stLine = QLineEdit()

        volume = QLabel("Vol of CuSO4 (ml) taken in conical flask:")
        self.volumeLine = QLineEdit()

        molesInCon = QLabel("Moles of CuSO4 taken in flask")
        self.molesInConLine = QLineEdit()

        self.BuNext = QPushButton("Next>")

        form1 = QGridLayout()

        for i, j, k in zip([0, 1, 2, 3], [weight, mm, st, volume], [self.weightLine, self.mmLine, self.stLine, self.volumeLine]):
            form1.addWidget(j,i, 0, 1, 2)
            form1.addWidget(k, i, 2, 1, 1)

        form1.addWidget(molesInCon,4, 0, 1, 1)
        form1.addWidget(self.molesInConLine, 4, 1, 1, 1)
        form1.addWidget(self.BuNext, 4, 2, 1, 1)

        vol = QLabel("Vol of Hypo (titrated for Std. Cu)")
        self.volLine = QLineEdit()
        
        StHy = QLabel("St. of Hypo (M) calculated:")
        self.StHyLine = QLineEdit()

        VolUn = QLabel("Vol of Unknown Cu soln. Generated")
        self.VolUnLine = QLineEdit()
        

        vol2 = QLabel("Vol of Hypo (titrated for Unknown Cu sol)")
        self.volLine2 = QLineEdit()

        StUn = QLabel("St. of Unknown Cu Soln. (M) ")
        self.StUnLine = QLineEdit()

        self.BuPrev = QPushButton("<Prev")
        
        self.Submit1 = QPushButton("Submit")
        self.Submit1.clicked.connect(self.SUBMIT1)

        form12 = QGridLayout()

        for i, j, k in zip([0, 1, 2, 3], [vol, StHy, VolUn, vol2], [self.volLine, self.StHyLine, self.VolUnLine, self.volLine2]):
            form12.addWidget(j, i, 0, 1, 2)
            form12.addWidget(k, i, 2, 1, 2)

        form12.addWidget(StUn, 4, 0, 1, 1)
        form12.addWidget(self.StUnLine, 4, 1, 1, 1)
        form12.addWidget(self.BuPrev,4, 2, 1, 1)
        form12.addWidget(self.Submit1, 4, 3, 1, 1)
        
        tempLayout = QStackedLayout()
        tempBox1 = QWidget()
        tempBox2 = QWidget()

        tempBox1.setLayout(form1)
        tempBox2.setLayout(form12)

        tempLayout.addWidget(tempBox1)
        tempLayout.addWidget(tempBox2)
        tempLayout.setCurrentWidget(tempBox1)

        self.tab1.setLayout(tempLayout)

        def nextAction():
            tempLayout.setCurrentWidget(tempBox2)

        def prevAction():
            tempLayout.setCurrentWidget(tempBox1)

        self.BuNext.clicked.connect(nextAction)
        self.BuPrev.clicked.connect(prevAction)

        stockLab = QLabel("Stock(M):")
        aceLab = QLabel("Acetone")
        self.aceLine = QLineEdit()
        hclLab = QLabel("HCl")
        self.hclLine = QLineEdit()
        IodLab = QLabel("Iodine")
        self.IodLine = QLineEdit()

        Url = QLabel("Pdf for Plots and Calculations:")
        self.urlLine = QLineEdit()
        self.urlLine.setReadOnly(True)

        self.choose1 = QPushButton("Browse")
        self.Up1 = QPushButton("Upload")

        self.choose1.clicked.connect(self.ChooseFile)
        self.Up1.clicked.connect(self.UploadImageONdrive)
        self.Submit2 = QPushButton("Submit")
        self.Submit2.clicked.connect(self.SUBMIT2)

        gridLay = QGridLayout()
        gridLay.addWidget(stockLab, 0, 0, 1, 1)

        for i, j, k in zip([1, 2, 3], [aceLab, hclLab, IodLab], [self.aceLine, self.hclLine, self.IodLine]):
            gridLay.addWidget(j, 0, i, 1, 1)
            gridLay.addWidget(k, 1, i, 1, 1)

        gridLay.addWidget(self.Submit2, 2, 0, 1, 4)
        gridLay.addWidget(Url, 3, 0, 1, 4)
        gridLay.addWidget(self.urlLine, 4, 0, 1, 2)
        gridLay.addWidget(self.choose1, 4, 2, 1, 1)
        gridLay.addWidget(self.Up1, 4, 3, 1, 1)
        
        self.tab2.setLayout(gridLay)

        stHCL = QLabel("St. of HCl(M)")
        stNaOH = QLabel("St. of NaOH(M)")
        self.stHCLLine = QLineEdit()
        self.stNAOHLine = QLineEdit()
        
        aceLab2 = QLabel("Acetic Acid(M)")
        ethLab2 = QLabel("Ethanol(M)")
        eacLab2 = QLabel("Ethylacetate(M)")

        aceLab3 = QLabel("Acetic Acid(M)")
        ethLab3 = QLabel("Ethanol(M)")
        eacLab3 = QLabel("Ethylacetate(M)")
        self.submit3 = QPushButton("Submit")
        self.submit3.clicked.connect(self.SUBMIT3)
        
        trial1 = QLabel("TRIAL -1")
        trial2 = QLabel("TRIAL -2")

        initial = QLabel("Ini Con >")
        equi = QLabel("Equ Con >")
        initial2 = QLabel("Ini Con >")
        equi2 = QLabel("Equ Con >")

        self.aceLine2 = QLineEdit()
        self.ethLine2 = QLineEdit()
        self.eacLine2 = QLineEdit()

        self.aceLine3 = QLineEdit()
        self.ethLine3 = QLineEdit()
        self.eacLine3 = QLineEdit()

        self.aceLine4 = QLineEdit()
        self.ethLine4 = QLineEdit()
        self.eacLine4 = QLineEdit()

        self.aceLine5 = QLineEdit()
        self.ethLine5 = QLineEdit()
        self.eacLine5 = QLineEdit()

        Kc = QLabel("KC")
        self.KcLine = QLineEdit()
        gridLay2 = QGridLayout()
        gridLay2.addWidget(stHCL, 0, 0, 1, 1)
        gridLay2.addWidget(self.stHCLLine, 0, 1, 1, 1)
        
        gridLay2.addWidget(stNaOH, 0, 2, 1, 1)
        gridLay2.addWidget(self.stNAOHLine, 0, 3, 1, 1)

        for i, j, k, l, m in zip([1,2,3], [trial1, initial, equi], [aceLab2, self.aceLine2, self.aceLine3], [ethLab2, self.ethLine2, self.ethLine3], [eacLab2, self.eacLine2, self.eacLine3]):
            gridLay2.addWidget(j, i, 0, 1, 1)
            gridLay2.addWidget(k, i, 1, 1, 1)
            gridLay2.addWidget(l, i, 2, 1, 1)
            gridLay2.addWidget(m, i, 3, 1, 1)
        
        NextButton = QPushButton("Next>")
        gridLay2.addWidget(NextButton, 4, 3, 1, 1)

        gridLay23 = QGridLayout()
        gridLay23.addWidget(trial2, 0, 0, 1, 4)
        gridLay23.addWidget(initial2, 1, 0, 1, 1)
        gridLay23.addWidget(equi2, 2, 0, 1, 1)
        for i, j, k, l in zip([0, 1, 2], [aceLab3, self.aceLine4, self.aceLine5],[ethLab3, self.ethLine4, self.ethLine5], [eacLab3, self.eacLine4, self.eacLine5]):
            gridLay23.addWidget(j, i, 1, 1, 1)
            gridLay23.addWidget(k, i, 2, 1, 1)
            gridLay23.addWidget(l, i, 3, 1, 1)

        

        gridLay23.addWidget(Kc, 3, 0, 1, 1)
        gridLay23.addWidget(self.KcLine, 3, 1, 1, 2)

        PrevButton = QPushButton("<Prev")
        gridLay23.addWidget(PrevButton, 3, 3, 1, 1)
        gridLay23.addWidget(self.submit3, 4, 0, 1, 4)

        tempLayout2 = QStackedLayout()
        tempBox13 = QWidget()
        tempBox23 = QWidget()

        tempBox13.setLayout(gridLay2)
        tempBox23.setLayout(gridLay23)

        tempLayout2.addWidget(tempBox13)
        tempLayout2.addWidget(tempBox23)
        tempLayout2.setCurrentWidget(tempBox13)

        def nextAction2():
            tempLayout2.setCurrentWidget(tempBox23)
            

        def prevAction2():
            tempLayout2.setCurrentWidget(tempBox13)
            

        NextButton.clicked.connect(nextAction2)
        PrevButton.clicked.connect(prevAction2)



        self.tab3.setLayout(tempLayout2)

        gridLay3 = QGridLayout()
        sto = QLabel("Stock(N)")
        tem = QLabel("Temp(C)")
        tempLine = QLineEdit()
        self.stocKLINE = QLineEdit()
        n4 = QLabel("N/4")
        n8 = QLabel("N/8")
        n16 = QLabel("N/16")
        n32 = QLabel("N/32")
        n64 = QLabel("N/64")
        n128 = QLabel("N/128")
        Ka = QLabel("Ka")
        self.n4line = QLineEdit()
        self.n8line = QLineEdit()
        self.n16line = QLineEdit()
        self.n32line = QLineEdit()
        self.n64line = QLineEdit()
        self.n128line = QLineEdit()
        self.KaLine = QLineEdit()
        url = QLabel("Plot Pdf")
        self.urlLine4 = QLineEdit()
        self.urlLine4.setReadOnly(True)
        self.submit4 = QPushButton("Submit")

        self.choose3 = QPushButton("Browse")
        self.Up3 = QPushButton("Upload")

        self.choose3.clicked.connect(self.ChooseFile2)
        self.Up3.clicked.connect(self.UploadImageONdrive2)
        
        for i, j, k, l,m,n in zip([0, 1, 2, 3], [sto, self.stocKLINE, tem, tempLine], [n4, self.n4line, n8, self.n8line], [n16, self.n16line, n32, self.n32line], [n64, self.n64line, n128, self.n128line], [url, self.urlLine4, self.choose3, self.Up3]):
            gridLay3.addWidget(j, 0, i, 1,1)
            gridLay3.addWidget(k, 1, i, 1,1)
            gridLay3.addWidget(l, 2, i, 1,1)
            gridLay3.addWidget(m, 3, i, 1,1)
            gridLay3.addWidget(n, 5, i, 1,1)

        gridLay3.addWidget(Ka, 4, 0, 1, 1)
        gridLay3.addWidget(self.KaLine, 4, 1, 1, 1)
        gridLay3.addWidget(self.submit4, 4, 2, 1, 2)
        self.submit4.clicked.connect(self.SUBMIT4)
        self.tab4.setLayout(gridLay3)

        weightCa = QLabel("Wt of CaCO3 (mg):")
        self.wtLineCa = QLineEdit()

        strCa = QLabel("Str of CaCO3 (M)")
        self.strCa = QLineEdit()

        strEDTA = QLabel("Str of EDTA (M)")
        self.strEDTA = QLineEdit()

        volCa = QLabel("Volm of tap water(ml):")
        self.volCaLine = QLineEdit()

        strCaUn = QLabel("Hardness of water (10^6 ppm)")
        self.strCaUn = QLineEdit()

        self.Submitexp5 = QPushButton("SUBMIT")
        self.Submitexp5.clicked.connect(self.SUBMIT5)
        gridLay5 = QGridLayout()
        flag = 0
        for i,j in zip([weightCa, strCa, strEDTA, volCa, strCaUn], [self.wtLineCa, self.strCa, self.strEDTA, self.volCaLine, self.strCaUn]):
            gridLay5.addWidget(i, flag, 0, 1, 3)
            gridLay5.addWidget(j, flag, 3, 1, 1)
            flag = flag+1
        gridLay5.addWidget(self.Submitexp5, flag, 3, 1, 1)
        self.tab5.setLayout(gridLay5)

        weightCa6 = QLabel("Wt of Oil taken(g):")
        self.wtLineCa6 = QLineEdit()

        strCa6 = QLabel("Str of HCl Soln (N)")
        self.strCa6 = QLineEdit()

        strEDTA6 = QLabel("Volumn of HCl req. to titrate flask-1 (ml)")
        self.strEDTA6 = QLineEdit()

        volCa6 = QLabel("Volumn of HCl req. to titrate flask-2 (ml)")
        self.volCaLine6 = QLineEdit()

        strCaUn6 = QLabel("Saponification Value (mg of KOH) :")
        self.strCaUn6 = QLineEdit()

        self.Submitexp6 = QPushButton("SUBMIT")
        self.Submitexp6.clicked.connect(self.SUBMIT6)
        gridLay56 = QGridLayout()
        flag = 0
        for i,j in zip([weightCa6, strCa6, strEDTA6, volCa6, strCaUn6], [self.wtLineCa6, self.strCa6, self.strEDTA6, self.volCaLine6, self.strCaUn6]):
            gridLay56.addWidget(i, flag, 0, 1, 3)
            gridLay56.addWidget(j, flag, 3, 1, 1)
            flag = flag+1

        gridLay56.addWidget(self.Submitexp6, flag, 3, 1, 1)
        self.tab6.setLayout(gridLay56)

    def SUBMIT1(self):
        if(self.but1.exp1Inst):
            dataGEN = self.but1.expWid.getUnknowns()
            DATA_Misc = ["exp1", remark[1], str(datetime.now()), 1, k]
            labels = ["Wt(grm)", "Moles Stock", "Str. of Cu Soln Stock", "Vol. Cu(in conical)", "moles of CuSo4 in flask", 
                    "Vol. Hypo(titrated for Cu)", "Str. of Hypo(M)", "Vol. Un Generated", "Vol. Hypo(titrated for Un)", 
                    "St. Un(M)"]
            dataIN = []
            for i in [self.weightLine, self.mmLine, self.stLine, self.volumeLine, self.molesInConLine, 
        self.volLine, self.StHyLine, self.VolUnLine, self.volLine2, self.StUnLine]:
                dataIN.append(i.text())
                
            self.SUBMIT(1, DATA_Misc, labels, dataIN, dataGEN)
            return
        else:
            self.notPerform()
                
    def SUBMIT2(self):
        if(self.but2.exp1Inst):
            temp = self.but2.expWid.getUnknowns()
            DATA_Misc = ["exp2", remark[1], str(datetime.now()), 2, k]
            labels = ["Ace. Stock(N)", "Hcl Stock(N)","Iodine Stock(N)"]
            dataIN = [self.aceLine.text(), self.hclLine.text(), self.IodLine.text()]
            
            self.SUBMIT(2, DATA_Misc, labels, dataIN, temp)
            
        else:
            self.notPerform()

    def SUBMIT3(self):
        if(self.but3.exp1Inst):
            temp = self.but3.expWid.getUnknowns()
            DATA_Misc = ["exp3", remark[1], str(datetime.now()), 3, k]
            labels = ["St. HCl(M)", "St. NaOh(M)", "\nTrial", "ACETONE(M)", "Ini", "Equ",
                      "ETHANOL (M)", "Ini", "Equ", "ETHYLACETATE (M)", "Ini", "Equ",
                      "\nTrial", "ACETONE(M)", "Ini", "Equ",
                      "ETHANOL (M)", "Ini", "Equ", "ETHYLACETATE (M)", "Ini", "Equ", "Kc"]

            dataGEN =[temp[0], temp[1], "1\n", "-", str(temp[2]), str(temp[2+3]), "-", str(temp[3]), str(temp[3+3]), "-",str(temp[4]), str(temp[4+3]),
                    2, "-", str(temp[8]), str(temp[8+3]), "-", str(temp[9]), str(temp[9+3]), "-",str(temp[10]), str(temp[10+3]), '3.33']

            
            dataIN = [self.stHCLLine.text(), self.stNAOHLine.text(),
                      "1\n", "-",
                      self.aceLine2.text(),self.aceLine3.text(),"-",
                      self.ethLine2.text(),self.ethLine3.text(),"-",
                      self.eacLine2.text(),self.eacLine3.text(),
                      "2\n", "-",
                      self.aceLine4.text(),self.aceLine5.text(), "-",
                      self.ethLine4.text(),self.ethLine5.text(), "-",
                      self.eacLine4.text(),self.eacLine5.text(),
                      self.KcLine.text()]
            
            self.SUBMIT(3, DATA_Misc, labels, dataIN, dataGEN)
        else:
            self.notPerform()

    def SUBMIT4(self):

        if(self.but4.exp1Inst):
            dataGEN = self.but4.expWid.getUnknowns()
            labels = ["stock(N)", "n/4", "n/8", "n/16", "n/32", "n/64", "n/128", "Ka"]
        
            dataIN= [self.stocKLINE.text(), self.n4line.text(),
                       self.n8line.text(), self.n16line.text(),
                       self.n32line.text(), self.n64line.text(),
                       self.n128line.text(), self.KaLine.text()]
            
            DATA_Misc = ["exp4", remark[1], str(datetime.now()), 4, k]
            
            self.SUBMIT(4, DATA_Misc, labels, dataIN, dataGEN)
        else:
            self.notPerform()

    def SUBMIT5(self):

        if(self.but5.exp1Inst):
            dataGEN = self.but5.expWid.getUnknowns()
            labels = ["Wt (mg)", "St CaCO3 (M)", "Str EDTA (M)", "Vol Unknown (ml)", "Hardness (10^6 ppm)"]
        
            dataIN= [self.wtLineCa.text(), self.strCa.text(),
                       self.strEDTA.text(), self.volCaLine.text(),
                       self.strCaUn.text()]
            
            DATA_Misc = ["exp5", remark[1], str(datetime.now()), 5, k]
            
            self.SUBMIT(5, DATA_Misc, labels, dataIN, dataGEN)
        else:
            self.notPerform()

    def SUBMIT6(self):

        if(self.but6.exp1Inst):
            dataGEN = self.but6.expWid.getUnknowns()
            labels = ["Wt (g)", "St HCl (N)", "V1 (flask-1)", "V2 (flask-2)", "Sap. Val"]
        
            dataIN= [self.wtLineCa6.text(), self.strCa6.text(),
                       self.strEDTA6.text(), self.volCaLine6.text(),
                       self.strCaUn6.text()]
            
            DATA_Misc = ["exp6", remark[1], str(datetime.now()), 6, k]
            
            self.SUBMIT(6, DATA_Misc, labels, dataIN, dataGEN)
        else:
            self.notPerform()
    
    def checkForMissingValues(self, dataIN, labels):
        flag = 0
        for i in dataIN:
            if i != '':
                flag = flag+1
            else:
                self.emptyValue(labels[flag])   
                return 0
        return 1

    def SUBMIT(self, exp, DATA_Misc, labels, dataIN, dataGEN):

        temp = self.checkForMissingValues(dataIN, labels)
        if temp == 0:
            return
        success = sheets.UPLOADONDRIVE2(DATA_Misc, dataGEN, dataIN, labels, folder_id = exp)
        if(success == 0):
            self.MESSAGE(True)
        else:
            self.MESSAGE(False)

    def notPerform(self):
        msg = QMessageBox()
        msg.setText("Experiment Not Performed yet")
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def emptyValue(self, field):
        msg = QMessageBox()
        
        msg.setText("Missing Value")
        msg.setWindowTitle("Invalid")
        msg.setInformativeText("Missing Filed: '"+str(field)+"'.\nPlease enter the required field value.")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def ChooseFile(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Pdf files (*.pdf)")
        if fname[0] == '':
            #self.errorMessage(title = "File Error!", type = QMessageBox.Warning, text = "No File Selected.", textInfo='Please Choose a pdf file with size < 5 MB.')
            return

        size = os.path.getsize(fname[0]) 
        if size>5242880 :
            self.errorMessage(title = "File Size Error!",type = QMessageBox.Warning, text = "File size too large.", textInfo='Please Choose a pdf file with size < 5 MB.')
            return
        self.urlLine.setText(str(fname[0]))

    def ChooseFile2(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Pdf files (*.pdf)")
        if fname[0] == '':
            #self.errorMessage(title = "File Error!", type = QMessageBox.Warning, text = "No File Selected.", textInfo='Please Choose a pdf file with size < 5 MB.')
            return
        
        size = os.path.getsize(fname[0]) 
        if size>5242880 :
            self.errorMessage(title = "File Size Error!", type = QMessageBox.Warning, text = "File size too large.", textInfo='Please Choose a pdf file with size < 5 MB.')
            return
        self.urlLine4.setText(str(fname[0]))

    def errorMessage(self, title = 'Error', type = QMessageBox.Critical, textInfo= 'Application Error! Report a bug?', text= "Unknown Error"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setInformativeText(textInfo)
        msg.setIcon(type)
        msg.exec_()

    def UploadImageONdrive(self):
        location = str(self.urlLine.text()) 
        if location == '':
            self.errorMessage(title = "File Error!", type = QMessageBox.Warning, text = "No File Selected.", textInfo='Please Choose a pdf file with size < 5 MB.')
            return
        
        fID = sheets.UploadImage(["Data2",remark[1]], location, k, 2, 4)
        if fID == '' or fID == None:
            self.errorMessage("Submission Failed", QMessageBox.Warning, "Unable to submit", "Failed !")
        else:
            self.errorMessage("Submission Success", QMessageBox.Information, "Successfully Submitted", "Done !")



    def UploadImageONdrive2(self):
        location = str(self.urlLine4.text()) 
        if location == '':
            self.errorMessage(title = "File Error!", type = QMessageBox.Warning, text = "No File Selected.", textInfo='Please Choose a pdf file with size < 5 MB.')
            return
        
        fID = sheets.UploadImage(["Data4",remark[1]], location, k, 4, 4)
        if fID == '' or fID == None:
            self.errorMessage("Submission Failed", QMessageBox.Warning, "Unable to submit", "Failed !")
        else:
            self.errorMessage("Submission Success", QMessageBox.Information, "Successfully Submitted", "Done !")

    def MESSAGE(self, boo):
        
        if(boo):
            msg = QMessageBox()
            msg.setText("Unable to submit")
            msg.setWindowTitle("Error")
            msg.setInformativeText("Check Internet connection or try Again")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Submitted")
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        
def main(app, user_dets, row, sheetID):
    Vlab = QApplication(sys.argv)
    global remark
    remark = user_dets
    global k
    k = row
    VlabWind = VlabWindow()
    VlabWind.show()
    Vlab.exec_()
    #Vlab.closeAllWindows()
    sys.exit()