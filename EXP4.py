from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLCDNumber, QAbstractSpinBox, QMessageBox, QSizePolicy, QDial, QVBoxLayout, QDoubleSpinBox, QLabel, QGridLayout,QLineEdit, QPushButton,QGroupBox, QHBoxLayout

import random
import math
from DragNDrop import DragLabel, DropLabel
from ModWidgets import FGroup, PushButton, VoHGroup, VoHWidget
from common import EXP_PAGE, ImageLabel

class Exp4_class(EXP_PAGE):

    def __init__(self, stack):
        imageList = [0, 0, 0, 0]
        for i in [0, 1, 2, 3]:
            imageList[i] = "media/discon-"+str(i+1)+".jpg"
        self.dataGEN=[0, 0, 0, 0, 0, 0, 0]
        super().__init__(imageList, "media/exp4.mp4", stack)

        self.GiveLab = QLabel("KCl Solution :")
        self.spin_b = QDoubleSpinBox()
        self.spin_b.setValue(0.1)
        self.spin_b.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin_b.valueChanged.connect(self.NoteValue)
        self.AdjustLabel = ImageLabel("A). Adjust Conductance &\nCalibrate")
        
        self.PipLabel = ImageLabel("")
        self.makLab = ImageLabel("")
        self.UseLab2 = ImageLabel("")
        
        self.TheCon = ImageLabel("B). STOCK (in N):")
        self.ConLine = QLineEdit()
        self.ConLine.setFont(QFont('Times'))
        self.nextBut24 = PushButton("Generate Stock")
        self.nextBut24.setEnabled(False)
        self.nextBut24.clicked.connect(self.validate)
        
        self.grpbo24 = FGroup("G")

        self.grpbo24.addWidgets([[self.GiveLab, self.spin_b], [self.AdjustLabel], [self.PipLabel], [self.makLab], [self.UseLab2], [self.TheCon, self.ConLine], [self.nextBut24]])

        
        self.maklab = QLabel("\nC). Make up the Volm to\n100ml using Stock:")
        self.maklab.setFont(QFont('Times'))
        self.rowTit_1 = QLabel("-CONC-")
        self.rowTit_3 = QLabel("-STOCK-")

        self.n4 = ImageLabel("N/4")
        self.n8 = ImageLabel("N/8")
        self.n16 = ImageLabel("N/16")
        self.n32 = ImageLabel("N/32")
        self.n64 = ImageLabel("N/64")
        self.n128 = ImageLabel("N/128")
        self.spin_n4n = QDoubleSpinBox()
        self.spin_n8n = QDoubleSpinBox()
        self.spin_n16n = QDoubleSpinBox()
        self.spin_n32n = QDoubleSpinBox()
        self.spin_n64n = QDoubleSpinBox()
        self.spin_n128n = QDoubleSpinBox()
        self.validateBut = QPushButton("Generate Solns")

        self.ResetBut = PushButton("RESET")
        self.ResetBut.clicked.connect(self.RESET)

        self.validateBut.setEnabled(False)
        self.validateBut.setFont(QFont('Times'))
        self.validateBut.clicked.connect(self.validate2)
        
        self.grpbo3lay4 = QGridLayout()
        self.grpbo3lay4.addWidget(self.rowTit_1, 1, 0)
        self.grpbo3lay4.addWidget(self.rowTit_3, 1, 1)
        self.grpbo3lay4.addWidget(self.n4, 2, 0)
        self.grpbo3lay4.addWidget(self.spin_n4n, 2, 1)
        self.grpbo3lay4.addWidget(self.n8, 3, 0)
        self.grpbo3lay4.addWidget(self.spin_n8n, 3, 1)
        self.grpbo3lay4.addWidget(self.n16, 4, 0)
        self.grpbo3lay4.addWidget(self.spin_n16n, 4, 1)
        self.grpbo3lay4.addWidget(self.n32, 5, 0)
        self.grpbo3lay4.addWidget(self.spin_n32n, 5, 1)
        self.grpbo3lay4.addWidget(self.n64, 6, 0)
        self.grpbo3lay4.addWidget(self.spin_n64n, 6, 1)
        self.grpbo3lay4.addWidget(self.n128, 7, 0)
        self.grpbo3lay4.addWidget(self.spin_n128n, 7, 1)

        self.temp1 = QGroupBox()
        self.temp1.setLayout(self.grpbo3lay4)

        self.grpbo24.addWidgets([[self.maklab],[self.temp1], [self.validateBut], [self.ResetBut]])
        
        self.side1box4 = VoHGroup("V")
        self.side1box4.addWidgets([self.grpbo24.Box])

        self.Titlelab4 = ImageLabel("DISSOCIATION CONSTANT")

        self.StockSol = DragLabel("Stock", "media/emptyflask.jpg", False, self)
        self.StockSolLab = ImageLabel("Stock")

        self.KCLSol = DragLabel("KCl", "media/smallflask.jpg", False, self)
        self.KCLSol.setVol("%.3f" %(12.01 + (((float(random.randint(-200, 200)))/10000)*12.01)))
        self.KCLSolLab = ImageLabel("KCl")

        self.N4Sol = DragLabel("N/4", "media/emptyflask.jpg", False, self)
        self.N4SolLab = ImageLabel("N/4")
        self.N8Sol = DragLabel("N/8", "media/emptyflask.jpg", False, self)
        self.N8SolLab = ImageLabel("N/8")
        self.N16Sol = DragLabel("N/16", "media/emptyflask.jpg", False, self)
        self.N16SolLab = ImageLabel("N/16")
        self.N32Sol = DragLabel("N/32", "media/emptyflask.jpg", False, self)
        self.N32SolLab = ImageLabel("N/32")
        self.N64Sol = DragLabel("N/64", "media/emptyflask.jpg", False, self)
        self.N64SolLab = ImageLabel("N/64")
        self.N128Sol = DragLabel("N/128", "media/emptyflask.jpg", False, self)
        self.N128SolLab = ImageLabel("N/128")

        self.SolRack1_wid = VoHWidget("V")
        self.SolRack1_wid.addWidgets([self.StockSol, self.StockSolLab, self.N4Sol, self.N4SolLab, self.N16Sol, self.N16SolLab, self.N64Sol, self.N64SolLab])

        self.SolRack2_wid = VoHWidget("V")
        self.SolRack2_wid.addWidgets([self.KCLSol, self.KCLSolLab, self.N8Sol, self.N8SolLab, self.N32Sol, self.N32SolLab, self.N128Sol, self.N128SolLab])

        self.solRackWid = VoHGroup("H")
        self.solRackWid.addWidgets([self.SolRack1_wid, self.SolRack2_wid])

        self.SolRackBoxLay = QVBoxLayout()
        self.SolRackBoxLay.addWidget(self.solRackWid)

        self.SolRackBox = QGroupBox()
        self.SolRackBox.setLayout(self.SolRackBoxLay)
        
        self.meterLabel = DropLabel("Drop_here", "media/con_meter.jpg", self)
        self.meterLabel.textChanged.connect(self.update)
        self.meterLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.conLab = ImageLabel("Equivalent Conductance")
        self.conLCD = QLCDNumber()

        self.conLCD.setSmallDecimalPoint(True)
        self.conLCD.setDigitCount(5)
        self.conLCD.display(0.00)
        self.DialCon = QDial()
        self.DialCon.setRange(0, 3000)
        self.DialCon.setNotchesVisible(False)
        self.DialCon.valueChanged.connect(self.changedValue)

        self.UnloadButt = PushButton("UNLOAD")
        self.UnloadButt.setEnabled(False)
        self.UnloadButt.clicked.connect(self.UNLOAD)

        self.calBut = PushButton("CALIBRATE")
        self.calButlab = QLabel("Calibrate")
        self.Display = QLineEdit()
        self.Display.setAlignment(Qt.AlignCenter)
        
        self.resLayW = VoHWidget("V")
        self.resLayW.addWidgets([self.calBut, self.Display, self.UnloadButt])
        self.resLayW.setMaximumWidth(120)
        
        self.calBut.clicked.connect(self.setNext4)

        self.conDisLayww = VoHWidget("V")
        self.conDisLayww.addWidgets([self.DialCon, self.conLab])

        self.conDisLayW = QHBoxLayout()
        self.conDisLayW.addWidget(self.conLCD)
        self.conDisLayWww = QGroupBox()
        self.conDisLayWww.setLayout(self.conDisLayW)

        self.DialTemp = QDial()
        self.DialTemp.setRange(1, 80)
        self.DialTemp.setValue(25)
        #self.DialTemp.setNotchesVisible(True)
        self.DialTemp.valueChanged.connect(self.changedTemp)
        
        self.tempLCD = QLCDNumber()
        self.tempLCD.display(25)

        self.tempLab = QLabel("TEMPERATURE")
        self.tempLab.setAlignment(Qt.AlignCenter)
        
        self.tempLayDW = VoHWidget("V")
        self.tempLayDW.addWidgets([self.DialTemp, self.tempLab])

        self.tempLayW = VoHGroup("H")
        self.tempLayW.addWidgets([self.tempLCD, self.tempLayDW])
        
        self.GroupBOX = VoHGroup("H")
        self.GroupBOX.addWidgets([self.conDisLayWww, self.conDisLayww, self.resLayW, self.tempLayW])
        self.GroupBOX.setMaximumHeight(200)

        self.side2wid4 = VoHWidget("V")
        self.side2wid4.addWidgets([self.Titlelab4, self.meterLabel.getLabel(), self.GroupBOX])
        self.side2wid4.VBOX.addStretch()
        self.side1box4.setMaximumWidth(300)

        self.Page4lay = QHBoxLayout()
        self.Page4lay.addWidget(self.side1box4)
        self.Page4lay.addWidget(self.solRackWid)
        self.Page4lay.addWidget(self.side2wid4)

        self.tab2.setLayout(self.Page4lay)
        
        self.errorAccu = 0
        self.errorFlag = 0
        self.flag = 0
        self.Ka = 0
        self.Display.setText("NONE")
        self.LOADEDFLAG = False

    def update(self):
        if(self.meterLabel.text() == "COND"):
            return

        if(self.LOADEDFLAG == True):
            self.errorFlag = 8
            self.errorMessage()
            return
        try :
            val = float(self.meterLabel.vol())
            self.LOADEDFLAG = True
            self.UnloadButt.setEnabled(True)
        except:
            val = 0
            self.errorMessage(textInFo="Error in updating conductance values")
        self.Display.setText(str(self.meterLabel.name()))
        self.conLCD.display(val)
        self.DialCon.setValue(int(val*100))
        self.meterLabel.setText("COND")
    
    def UNLOAD(self):
        self.UnloadButt.setEnabled(False)
        self.Display.setText("NONE")
        self.LOADEDFLAG = False
        self.DialCon.setValue(0)
        self.conLCD.display(0)
        self.meterLabel.setText("COND")
        
        
    def setNext4(self):
        name = self.meterLabel.name()
        if(name != "KCl"):
            self.errorFlag = 1
            self.errorMessage()
            return
        val = float(self.DialCon.value())/100
        if(val != 12.88):
            self.errorAccu = ((val-12.88)/12.88)
            if(self.errorAccu > 0.3 or self.errorAccu < -0.3):
                self.errorFlag = 3
                self.errorMessage()
                return
        if(val !=  self.KCLSol.vol()):
            self.flag = 0
        self.KCLSol.setVol(val)
        self.PipLabel.setText("1.Pipette out 50 ml 1N Acetic Acid")
        self.makLab.setText("2.Make up the volm to 100 ml")
        self.UseLab2.setText("(Use Conductivity Water !!)")
        
        self.nextBut24.setEnabled(True)

    def NoteValue(self):

        condval = self.spin_b.value()

    def changedValue(self):
        val = float(self.DialCon.value())/100
        self.conLCD.display(val)

    def changedTemp(self):
        self.tempLCD.display(self.DialTemp.value())
    def validate(self):

        try:
            k = float(self.ConLine.text())
            if(k <= 0):
                self.errorFlag = 2
                self.errorMessage()
                return

            self.StockSol.setImage("media/smallflask.jpg")
            Ka = 1.75
            k = float(random.randint(100, 9999))
            error = k/10000
            Ka = Ka + error
            Ka = Ka/100000
            
            c1 = (float(self.ConLine.text())*100)/(100)
            
            alpha1 = (math.sqrt((Ka**2) + (4*c1*Ka))-Ka)/(2*c1)
            kappa1 = "%.3f" %(390.8*alpha1)
            
            self.StockSol.setVol(kappa1)
            self.validateBut.setEnabled(True)

            self.errorFlag = 6
            self.errorMessage()
        except:
            self.errorFlag = 2
            self.validateBut.setEnabled(False)
            self.errorMessage()
    def validate2(self):
        if(True):
            try:
                k = float(self.ConLine.text())
                if(k <= 0):
                    self.errorFlag = 2
                    self.errorMessage()
            except:
                self.errorFlag = 2
                self.errorMessage()
                return
            
        for i in[ self.spin_n4n, self.spin_n8n, self.spin_n16n, self.spin_n32n, self.spin_n64n, self.spin_n128n]:
            try:
                temp = float(i.value())
                
                if temp >= 100 or temp == 0:
                    self.errorFlag = 4
                    self.errorMessage()
                    return
            except:
                self.errorMessage()
                return
        self.CalculateConductivity()

    def CalculateConductivity(self):

        Ka = 1.75
        k = float(random.randint(100, 9999))
        error = k/10000
        Ka = Ka + error
        Ka = Ka/100000
        
        if(self.flag == 0) :
            self.Ka = Ka
            c1 = (float(self.ConLine.text())*self.spin_n4n.value())/(100)
            c2 = (float(self.ConLine.text())*self.spin_n8n.value())/(100)
            c3 = (float(self.ConLine.text())*self.spin_n16n.value())/(100)
            c4 = (float(self.ConLine.text())*self.spin_n32n.value())/(100)
            c5 = (float(self.ConLine.text())*self.spin_n64n.value())/(100)
            c6 = (float(self.ConLine.text())*self.spin_n128n.value())/(100)
            #print("values extracted")
            c1 = c1 + (((float(random.randint(-200, 200)))/10000)*c1)+ self.errorAccu*c1
            c2 = c2 + (((float(random.randint(-200, 200)))/10000)*c2)+ self.errorAccu*c2
            c3 = c3 + (((float(random.randint(-200, 200)))/10000)*c3)+ self.errorAccu*c3
            c4 = c4 + (((float(random.randint(-200, 200)))/10000)*c4)+ self.errorAccu*c4
            c5 = c5 + (((float(random.randint(-200, 200)))/10000)*c5)+ self.errorAccu*c5
            c6 = c6 + (((float(random.randint(-200, 200)))/10000)*c6)+ self.errorAccu*c6
            #print("error added")
            alpha1 = (math.sqrt((Ka**2) + (4*c1*Ka))-Ka)/(2*c1)
            alpha2 = (math.sqrt((Ka**2) + (4*c2*Ka))-Ka)/(2*c2)
            alpha3 = (math.sqrt((Ka**2) + (4*c3*Ka))-Ka)/(2*c3)
            alpha4 = (math.sqrt((Ka**2) + (4*c4*Ka))-Ka)/(2*c4)
            alpha5 = (math.sqrt((Ka**2) + (4*c5*Ka))-Ka)/(2*c5)
            alpha6 = (math.sqrt((Ka**2) + (4*c6*Ka))-Ka)/(2*c6)
            #print("alpha calculated")
            kappa1 = "%.3f" %(390.8*alpha1)
            kappa2 = "%.3f" %(390.8*alpha2)
            kappa3 = "%.3f" %(390.8*alpha3)
            kappa4 = "%.3f" %(390.8*alpha4)
            kappa5 = "%.3f" %(390.8*alpha5)
            kappa6 = "%.3f" %(390.8*alpha6)
            #print("kappa calculated")
            self.flag = 1

            self.N4Sol.setVol(kappa1)
            self.N8Sol.setVol(kappa2)
            self.N16Sol.setVol(kappa3)
            self.N32Sol.setVol(kappa4)
            self.N64Sol.setVol(kappa5)
            self.N128Sol.setVol(kappa6)

            self.dataGEN = [self.ConLine.text()]
            for i in [kappa1, kappa2, kappa3, kappa4, kappa5, kappa6, Ka]:
                self.dataGEN.append(str(i))
            #print("Done calculated")
        if(self.flag == 1):
            for i in [self.N4Sol, self.N8Sol, self.N16Sol, self.N32Sol, self.N64Sol, self.N128Sol]:
                i.setImage("media/smallflask.jpg")

            self.errorFlag = 7
            self.errorMessage()
            
    def RESET(self) :
        for i in [self.N4Sol, self.N8Sol, self.N16Sol, self.N32Sol, self.N64Sol, self.N128Sol]:
            i.setImage("media/emptyflask.jpg")
            i.setVol(0)
        for i in[ self.spin_n4n, self.spin_n8n, self.spin_n16n, self.spin_n32n, self.spin_n64n, self.spin_n128n]:
            i.setValue(0)
        self.flag = 0
        self.meterLabel.setText("COND")
        self.meterLabel.setVol(0)
        self.meterLabel.setName("COND")
        self.Display.setText("NONE")
        self.validateBut.setEnabled(False)
        self.nextBut24.setEnabled(False)
        self.UnloadButt.setEnabled(False)
        self.LOADEDFLAG = False
        
    def errorMessage(self, textInFo=""):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        textM = "Unknown Error"
        text = "Error could not be identified. Report a Bug? Identified Error:\n" + str(textInFo)
        title = "UNKNOWN ERROR !"
        if(self.errorFlag == 1):
            text = "Calibration Data Available for KCl Only."
            title = "CALIBRATION!"
            textM = "Calibration Error!"
        elif(self.errorFlag == 2):
            text = "Invalid Entry ! Please Enter a valid concentration for Stock Solution."
            textM = "Stock Error!"
            title = "STOCK !"
        elif(self.errorFlag == 3):
            title = "CALIBRATION!"
            textM = "Calibration Error!"
            text = "Inaccurate Calibration for KCl.\nRecalibration Recommended.\n(Tip : Use Keyboard arrow keys)"
        elif(self.errorFlag == 4):
            textM = "Solution Concentration Error!"
            title = "SOLUTIONS"
            text = "Inaccurate Solution preparation. Reverification Recommended."
        elif(self.errorFlag == 6):
            title = "STOCK CREATED"
            text = "Stock Solution Now prepared"
            textM = "ATTENTION !"
        elif(self.errorFlag == 7):
            title = "SOLUTIONS CREATED"
            text = "All Solution Now prepared"
            textM = "ATTENTION !"
        elif(self.errorFlag == 8):
            text = "Previous Solution is already Loaded. Please unload first."
            title = "Unloaded Required"
            textM = "Unload Required"
            
        if(self.errorFlag >= 6):
            self.w.setIcon(QMessageBox.Information)
        else :
            self.w.setIcon(QMessageBox.Critical)
        self.w.setText(textM)
        self.w.setInformativeText(text)
        self.w.setWindowTitle(title)
        self.w.exec()
        self.errorFlag = 0