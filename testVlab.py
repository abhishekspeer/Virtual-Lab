from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
#import qdarkstyle
from datetime import datetime
import sys


from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


remark = []
k = 0
exp2 = 0
#print("Ints")
class VlabWindow(QMainWindow):
    def __init__(self, Vlab):
        super().__init__()
        self.opp = Vlab
        #self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        #self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("Virtual Chem-labs")
        self.DefPage(Vlab)
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.DefPage_widget)
        self.stacked_layout.setCurrentIndex(0)
        self.Central_widget = QWidget()
        self.Central_widget.setMaximumHeight(720)
        self.Central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.Central_widget)
        self.setWindowIcon(QIcon('media/icon.ico'))
        #self.resize(1366, 700)
        #self.Central_widget.setGeometry(100,50,1100,600)
        #self.resize(1366, 700)
        #self.showMaximized()
        
    def DefPage(self, Vlab):
        self.head = QLabel("VIRTUAL LABORATORY")
        self.head.setAlignment(Qt.AlignCenter)
        self.head.setFont(QFont('Times', 20))
        self.but1 = QPushButton(" Experiment 1 ")
        self.but1.clicked.connect(self.exp1)
        
        self.but2 = QPushButton(" Experiment 2 ")
        self.but2.clicked.connect(self.exp2)
        
        self.but3 = QPushButton(" Experiment 3 ")
        self.but3.clicked.connect(self.exp3)
        
        self.but4 = QPushButton(" Experiment 4 ")
        self.but4.clicked.connect(self.exp4)
        self.defLab = QLabel("Calculation of strength of ")
        self.defLab2 = QLabel("Idonation using photometry")
        self.defLab3 = QLabel("Equilibrium Constant calculation")
        self.defLab4 = QLabel("Dissociation Constant") 

        self.defLay = QFormLayout()

        for i, j in zip([self.but1, self.but2, self.but3, self.but4],
                        [self.defLab, self.defLab2, self.defLab3, self.defLab4]):
            self.defLay.addRow(i, j)
            i.setFont(QFont('Times', 12))
            j.setFont(QFont('Times', 10))

        self.cb = QTabWidget()
        self.tab1 = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        #self.tabs.resize(300,200)
        # Add tabs
        self.cb.addTab(self.tab1,"Exp 1")
        self.cb.addTab(self.tab2,"Exp 2")
        self.cb.addTab(self.tab3,"Exp 3")
        self.cb.addTab(self.tab4,"Exp 4")
        self.createSUB()
        self.cb.setFont(QFont('Times', 12))
        
        self.defGr1 = QGroupBox()
        self.defGr1.setLayout(self.defLay)
        self.defLab5 = QLabel("Last performed remarks :")
        self.defLab5.setAlignment(Qt.AlignLeft)
        self.TEXT_BOX_H = QPlainTextEdit()
        #self.TEXT_BOX_H.setMaximumWidth(135)
        self.TEXT_BOX_H.setReadOnly(True)
        self.TEXT_BOX_H.setFont(QFont('Times', 10))
        now = datetime.now()
        self.TEXT_BOX_H.setPlainText(str(now)+"\n")
        flag = 1
        self.TEXT_BOX_H.appendPlainText("USER_ID_NO :" + remark[1])
        flag2 = 0
        for i in remark:
            if(flag2 < 4):
                flag2 +=1
                continue
            self.TEXT_BOX_H.appendPlainText("Experiment "+str(flag)+" :>" + i)
            flag += 1
        
        self.defPageLay = QVBoxLayout()
        self.welComeUser = QLabel("Welcome "+remark[0])
        self.welComeUser.setFont(QFont('Times', 10))
        self.defPageLay.addWidget(self.head)
        self.defPageLay.addWidget(self.welComeUser)
        self.defPageLay.addWidget(self.defGr1)
        self.defPageLay.addWidget(self.defLab5)
        self.defPageLay.addWidget(self.TEXT_BOX_H)
        self.defPageLay.addWidget(self.cb)

        self.sideAni = QMovie("ani1.gif")
        
        self.sideAni.frameChanged.connect(self.repaint)
        self.sideAniLab = QLabel()
        self.sideAniLab.setMovie(self.sideAni)
        self.sideAni.start()

        self.defGr2 = QGroupBox()
        self.defGr2.setLayout(self.defPageLay)
        self.defGr2.setMaximumWidth(400)

        self.DefBox = QHBoxLayout()
        self.DefBox.addWidget(self.defGr2)
        self.DefBox.addWidget(self.sideAniLab)

        self.selLab = QLabel("Select Experiment")

        

        self.Data = 0

        self.DefPage_widget = QWidget()
        self.BackButton = QPushButton("  BACK  ")
        self.BackButton.clicked.connect(self.goBackToDef)
        self.BackButton.setFont(QFont('Times', 12))

        self.BackButton2 = QPushButton("  BACK  ")
        self.BackButton2.clicked.connect(self.goBackToDef)
        self.BackButton2.setFont(QFont('Times', 12))

        self.BackButton3 = QPushButton("  BACK  ")
        self.BackButton3.clicked.connect(self.goBackToDef)
        self.BackButton3.setFont(QFont('Times', 12))

        self.BackButton4 = QPushButton("  BACK  ")
        self.BackButton4.clicked.connect(self.goBackToDef)
        self.BackButton4.setFont(QFont('Times', 12))
        
        self.DefPage_widget.setLayout(self.DefBox)
        
        self.simulationBox = QWidget()
        self.expBox = QWidget()
        self.exp4Inst = 0
        self.exp1Inst = 0
        self.exp2Inst = 0
        self.exp3Inst = 0
        self.layPage = QHBoxLayout()
        self.layPage.addWidget(self.expBox)
        self.layPage.addWidget(self.BackButton)

        self.simulationBox.setLayout(self.layPage)
        #self.HomePage_widget.setGeometry(100,100,200,200)
        self.DefPage_widget.setWindowTitle("WELCOME "+remark[1])
        
    def exp4(self):
        if(self.exp4Inst == 0):
            global EXP4
            import EXP4
            
            self.exp4Inst = 1
            self.exp4_wid = EXP4.main_exp4()
            self.exp4_wid.setCornerWidget(self.BackButton4, Qt.TopRightCorner)

            self.stacked_layout.addWidget(self.exp4_wid)
        self.stacked_layout.setCurrentWidget(self.exp4_wid)
        self.setWindowTitle("Conductometery")
        #self.resize(1366, 700)
    def exp1(self):

        if(self.exp1Inst == 0):
            global EXP1_t
            import EXP1_t

            #print("Imported")
            self.exp1Inst = 1
            self.exp1_wid = EXP1_t.main_exp1()
            #print("PAge")

            self.exp1_wid.setCornerWidget(self.BackButton, Qt.TopRightCorner)
            
            self.stacked_layout.addWidget(self.exp1_wid)
            
        self.stacked_layout.setCurrentWidget(self.exp1_wid)
        self.setWindowTitle("Iodometery")
        #print("OKAY HERE")
    def exp2(self):
        
        if(self.exp2Inst == 0):
            global EXP2
            import EXP2
            
            self.exp2Inst = 1
            self.exp2_wid = EXP2.main_exp2()
            
            self.exp2_wid.setCornerWidget(self.BackButton2, Qt.TopRightCorner)

            self.stacked_layout.addWidget(self.exp2_wid)
        self.stacked_layout.setCurrentWidget(self.exp2_wid)
        self.setWindowTitle("Photometery")
        #self.resize(1366, 700)
    def exp3(self):
        
        if(self.exp3Inst == 0):
            global EXP3
            import EXP3
            #print("Imported")
            self.exp3Inst = 1
            self.exp3_wid = EXP3.main_exp3(remark[1], sheets)
            
            self.exp3_wid.setCornerWidget(self.BackButton3, Qt.TopRightCorner)

            self.stacked_layout.addWidget(self.exp3_wid)
        self.stacked_layout.setCurrentWidget(self.exp3_wid)
        self.setWindowTitle("Equilibrium Constant")
        #self.resize(1366, 700)
    def goBackToDef(self):
        ##self.resize(1366, 700)
        self.stacked_layout.setCurrentWidget(self.DefPage_widget)
        self.setWindowTitle("Virtual Chem-labs")
        #self.resize(1366, 700)

    def createSUB(self):
        weight = QLabel("Weight CuSO4")
        self.weightLine = QLineEdit()
        mm = QLabel("Moles CuSO4")
        self.mmLine = QLineEdit()
        
        volume = QLabel("Vol CuSO4")
        self.volumeLine = QLineEdit()
        st = QLabel("St. CuSO4")
        self.stLine = QLineEdit()
        
        StHy = QLabel("St. Hypo")
        self.StHyLine = QLineEdit()
        vol = QLabel("Vol. Hypo(Cu)")
        self.volLine = QLineEdit()

        vol2 = QLabel("Vol. Hypo(Un)")
        self.volLine2 = QLineEdit()


        VolUn = QLabel("Vol. Unknown")
        self.VolUnLine = QLineEdit()
        StUn = QLabel("St. of Unknown")
        self.StUnLine = QLineEdit()
        
        self.Submit1 = QPushButton("Submit")
        self.Submit1.clicked.connect(self.SUBMIT1)
        form1 = QGridLayout()

        form1.addWidget(weight,0, 0, 1, 1)
        form1.addWidget(self.weightLine, 0, 1, 1, 1)
        form1.addWidget(mm,0, 2, 1, 1)
        form1.addWidget(self.mmLine, 0, 3, 1, 1)
        
        form1.addWidget(volume,1, 0, 1, 1)
        form1.addWidget(self.volumeLine, 1, 1, 1, 1)
        form1.addWidget(st,1, 2, 1, 1)
        form1.addWidget(self.stLine, 1, 3, 1, 1)
        
        form1.addWidget(vol,2, 0, 1, 1)
        form1.addWidget(self.volLine, 2, 1, 1, 1)
        form1.addWidget(StHy,2, 2, 1, 1)
        form1.addWidget(self.StHyLine, 2, 3, 1, 1)

        form1.addWidget(VolUn,3, 0, 1, 1)
        form1.addWidget(self.VolUnLine, 3, 1, 1, 1)
        form1.addWidget(vol2,3, 2, 1, 1)
        form1.addWidget(self.volLine2, 3, 3, 1, 1)

        form1.addWidget(StUn,4, 0, 1, 1)
        form1.addWidget(self.StUnLine, 4, 1, 1, 1)
        form1.addWidget(self.Submit1, 4, 2, 1, 2)
        
        self.tab1.setLayout(form1)

        stockLab = QLabel("Stock:")
        aceLab = QLabel("Acetone")
        self.aceLine = QLineEdit()
        hclLab = QLabel("HCl")
        self.hclLine = QLineEdit()
        IodLab = QLabel("Iodine")
        self.IodLine = QLineEdit()

        Url = QLabel("URL for Plots:")
        self.urlLine = QLineEdit()
        Url2 = QLabel("URL for Data:")
        self.urlLine2 = QLineEdit()

        Submit2 = QPushButton("Submit")
        Submit2.clicked.connect(self.SUBMIT2)

        lab = QLabel("Please Note only the Most recently Generated")
        gridLay = QGridLayout()
        gridLay.addWidget(stockLab, 0, 0, 1, 1)
        gridLay.addWidget(aceLab, 0, 1, 1, 1)
        gridLay.addWidget(self.aceLine, 1, 1, 1, 1)
        gridLay.addWidget(hclLab, 0, 2, 1, 1)
        gridLay.addWidget(self.hclLine, 1, 2, 1, 1)
        gridLay.addWidget(IodLab, 0, 3, 1, 1)
        gridLay.addWidget(self.IodLine, 1, 3, 1, 1)
        gridLay.addWidget(Url, 2, 0, 1, 4)
        gridLay.addWidget(self.urlLine, 3, 0, 1, 4)
        gridLay.addWidget(Url2, 4, 0, 1, 4)
        gridLay.addWidget(self.urlLine2, 5, 0, 1, 4)
        gridLay.addWidget(Submit2, 6, 0, 1, 4)
        
        self.tab2.setLayout(gridLay)

        stHCL = QLabel("St. of HCl")
        stNaOH = QLabel("St. of NaOH")
        self.stHCLLine = QLineEdit()
        self.stNAOHLine = QLineEdit()
        
        aceLab2 = QLabel("Acetic Acid")
        ethLab2 = QLabel("Ethanol")
        eacLab2 = QLabel("Ethylacetate")

        aceLab3 = QLabel("Acetic Acid")
        ethLab3 = QLabel("Ethanol")
        eacLab3 = QLabel("Ethylacetate")
        self.submit3 = QPushButton("Submit")
        self.submit3.clicked.connect(self.SUBMIT3)
        
        trial1 = QLabel("Trial 1")
        trial2 = QLabel("Trial 2")
        trial3 = QLabel("Trial 1")
        trial4 = QLabel("Trial 2")

        initial = QLabel("Initial Conc.")
        equi = QLabel("Equilm. Conc.")

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

        Kc = QLabel("  KC ")
        self.KcLine = QLineEdit()
        gridLay2 = QGridLayout()
        gridLay2.addWidget(stHCL, 0, 0, 1, 1)
        gridLay2.addWidget(self.stHCLLine, 0, 1, 1, 1)
        
        gridLay2.addWidget(stNaOH, 0, 2, 1, 1)
        gridLay2.addWidget(self.stNAOHLine, 0, 3, 1, 1)

        gridLay2.addWidget(equi, 4, 0, 1, 4)
        gridLay2.addWidget(trial3, 5, 0, 1, 1)
        gridLay2.addWidget(trial4, 6, 0, 1, 1)
        gridLay2.addWidget(Kc, 7, 0, 1, 1)
        gridLay2.addWidget(self.KcLine, 7, 1, 1, 1)
        gridLay2.addWidget(self.submit3, 7, 2, 1, 2)
    
        gridLay2.addWidget(initial, 1, 0, 1, 1)
        gridLay2.addWidget(trial1, 2, 0, 1, 1)
        gridLay2.addWidget(trial2, 3, 0, 1, 1)

        gridLay2.addWidget(aceLab2, 1, 1, 1, 1)
        gridLay2.addWidget(aceLab3, 4, 1, 1, 1)
        gridLay2.addWidget(self.aceLine2, 2, 1, 1, 1)
        gridLay2.addWidget(self.aceLine3, 3, 1, 1, 1)
        gridLay2.addWidget(self.aceLine4, 5, 1, 1, 1)
        gridLay2.addWidget(self.aceLine5, 6, 1, 1, 1)

        gridLay2.addWidget(ethLab2, 1, 2, 1, 1)
        gridLay2.addWidget(ethLab3, 4, 2, 1, 1)
        gridLay2.addWidget(self.ethLine2, 2, 2, 1, 1)
        gridLay2.addWidget(self.ethLine3, 3, 2, 1, 1)
        gridLay2.addWidget(self.ethLine4, 5, 2, 1, 1)
        gridLay2.addWidget(self.ethLine5, 6, 2, 1, 1)

        gridLay2.addWidget(eacLab2, 1, 3, 1, 1)
        gridLay2.addWidget(eacLab3, 4, 3, 1, 1)
        gridLay2.addWidget(self.eacLine2, 2, 3, 1, 1)
        gridLay2.addWidget(self.eacLine3, 3, 3, 1, 1)
        gridLay2.addWidget(self.eacLine4, 5, 3, 1, 1)
        gridLay2.addWidget(self.eacLine5, 6, 3, 1, 1)

        self.tab3.setLayout(gridLay2)

        gridLay3 = QGridLayout()
        sto = QLabel("Stock")
        tem = QLabel("Temp ")
        tempLine = QLineEdit()
        self.stocKLINE = QLineEdit()
        n4 = QLabel("N/4")
        n8 = QLabel("N/8")
        n16 = QLabel("N/16")
        n32 = QLabel("N/32")
        n64 = QLabel("N/64")
        n128 = QLabel("N/128")

        self.n4line = QLineEdit()
        self.n8line = QLineEdit()
        self.n16line = QLineEdit()
        self.n32line = QLineEdit()
        self.n64line = QLineEdit()
        self.n128line = QLineEdit()


        url = QLabel("URL for Plot")
        self.urlLine4 = QLineEdit()
        self.submit4 = QPushButton("Submit")
        for i in [self.Submit1, Submit2, self.submit3 , self.submit4]:
            i.setFont(QFont('Times', 10))
            
        gridLay3.addWidget(sto, 0, 0, 1,1)
        gridLay3.addWidget(self.stocKLINE, 0, 1, 1,1)
        gridLay3.addWidget(tem, 0, 2, 1,1)
        gridLay3.addWidget(tempLine, 0, 3, 1,1)

        gridLay3.addWidget(n4, 1, 0, 1,1)
        gridLay3.addWidget(self.n4line, 1, 1, 1,1)
        gridLay3.addWidget(n8, 1, 2, 1,1)
        gridLay3.addWidget(self.n8line,1, 3, 1,1)

        gridLay3.addWidget(n16, 2, 0, 1,1)
        gridLay3.addWidget(self.n16line, 2, 1, 1,1)
        gridLay3.addWidget(n32, 2, 2, 1,1)
        gridLay3.addWidget(self.n32line, 2,3, 1,1)

        gridLay3.addWidget(n64, 3, 0, 1,1)
        gridLay3.addWidget(self.n64line, 3, 1, 1,1)
        gridLay3.addWidget(n128, 3, 2, 1,1)
        gridLay3.addWidget(self.n128line, 3, 3, 1,1)
        gridLay3.addWidget(url, 4, 0, 1, 1)
        gridLay3.addWidget(self.urlLine4, 4, 1, 1, 3)

        gridLay3.addWidget(self.submit4, 5, 0, 1, 4)
        self.submit4.clicked.connect(self.SUBMIT4)
        self.tab4.setLayout(gridLay3)
        
    def SUBMIT4(self):

        if(self.exp4Inst):
            dataGEN = EXP4.getUnknowns()
            labels = ["stock: ", "n/4", "n/8", "n/16", "n/32", "n/64", "n/128", "Plot Link"]
            #print("callsuccess")
            dataIN= [self.stocKLINE.text(), self.n4line.text(),
                       self.n8line.text(), self.n16line.text(),
                       self.n32line.text(), self.n64line.text(),
                       self.n128line.text(), self.urlLine4.text()]
            
            DATA_Misc = ["exp4", remark[1], str(datetime.now())]
            #print("DATA GEN")
            success = sheets.UPLOADONDRIVE2(DATA_Misc, dataGEN, dataIN, labels, folder_id = 4)
            if(success == 0):
                #remove(str(remark[1])+".txt")
                self.MESSAGE(True)
            else:
                #self.submit4.setEnabled(False)
                self.MESSAGE(False)
        else:
            self.notPerform()
            
    def SUBMIT3(self):

        if(self.exp3Inst):
            temp = EXP3.getUnknowns()
            DATA_Misc = ["exp3", remark[1], str(datetime.now())]
            labels = ["St. HCl", "St. NaOh", "\nTrial :",
                      "Acetone ", "Ethanol ", "EthyAce. ",
                      "\nTrial :",
                      "Acetone ", "Ethanol ", "EthyAce. ", "Kc"]
            dataGEN =[temp[0], temp[1], "1\n"]
            for i in [2, 3, 4]:
                dataGEN.append(str(temp[i])+"-->"+str(temp[i+3]))

            dataGEN.append("2\n")
            for i in [8, 9, 10]:
                dataGEN.append(str(temp[i])+"-->"+str(temp[i+3]))

            
            dataIN = [self.stHCLLine.text(), self.stNAOHLine.text(),
                      "1\n",
                      str(self.aceLine2.text()+"-->"+self.aceLine4.text()),
                      str(self.ethLine2.text()+"-->"+self.ethLine4.text()),
                      str(self.eacLine2.text()+"-->"+self.eacLine4.text()),
                      "2\n",
                      str(self.aceLine3.text()+"-->"+self.aceLine5.text()),
                      str(self.ethLine3.text()+"-->"+self.ethLine5.text()),
                      str(self.eacLine3.text()+"-->"+self.eacLine5.text()),
                      self.KcLine.text()]
            
            success = sheets.UPLOADONDRIVE2(DATA_Misc, dataGEN, dataIN, labels, folder_id = 3)
            if(success == 0):
                #remove(str(remark[1])+".txt")
                self.MESSAGE(True)
            else:
                self.MESSAGE(False)
        else:
            self.notPerform()
        
    def SUBMIT1(self):
        if(self.exp1Inst):
            self.sub()
            return
        else:
            self.notPerform()

    def sub(self):
        dataGEN = EXP1_t.getUnknowns()
        DATA_Misc = ["exp1", remark[1], str(datetime.now())]
        labels = ["Weight", "Moles", "Vol. Cu", "St. Cu", "Vol. Hypo(Cu)",
                  "St. Hypo", "Vol. Un", "Vol. Hypo(Un)", "St. Un"]
        dataIN = []
        for i in[self.weightLine, self.mmLine, self.volumeLine, self.stLine,self.volLine,
                  self.StHyLine, self.VolUnLine, self.volLine2, self.StUnLine]:
            dataIN.append(i.text())
        
        success = sheets.UPLOADONDRIVE2(DATA_Misc, dataGEN, dataIN, labels, folder_id = 1)
        if(success == 0):
            self.MESSAGE(True)
        else:
            self.MESSAGE(False)
            
    def SUBMIT2(self):
        if(self.exp2Inst):
            temp = EXP2.getUnknowns()
            DATA_Misc = ["exp2", remark[1], str(datetime.now())]
            labels = ["Ace. Stock", "Hcl Stock", "Plot link", "Data Link"]
            dataIN = [self.aceLine.text(), self.hclLine.text(), self.IodLine.text()]
            data = [str(datetime.now()),self.aceLine.text(), temp[0], self.hclLine.text(), temp[1], self.IodLine.text(), temp[2], self.urlLine.text(), self.urlLine2.text()]
            self.SUBMIT(2, data, DATA_Misc, labels, dataIN, temp)
        else:
            self.notPerform()
            
    def SUBMIT(self, exp, data, DATA_Misc, labels, dataIN, dataGEN):
        success = sheets.SUBMITDATA(remark[1], exp, data, k)
        success = sheets.UPLOADONDRIVE2(DATA_Misc, dataGEN, dataIN, labels, folder_id = 2)
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
    #Vlab.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ##print(user_dets)
    global remark
    remark = user_dets
    global k
    k = row
    global sheets
    sheets = sheetID
    ##print(remark)
    VlabWind = VlabWindow(app)
    VlabWind.show()
    #VlabWind.raise_()
    Vlab.exec_()
    Vlab.closeAllWindows()
    sys.exit(1)
    
