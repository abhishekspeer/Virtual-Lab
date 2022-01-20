from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QDoubleSpinBox, QLabel, QGridLayout,QPushButton, QGroupBox, QHBoxLayout

import random
from ModWidgets import Dial, PushButton, TableMod, VoHGroup, VoHWidget, VolSlider
from common import EXP_PAGE, ImageLabel
from DragNDrop import DragLabel, DropLabel
import cmath

class Exp3_class(EXP_PAGE):

    def __init__(self, stack, imageList = ["media/equi-1.jpg", "media/equi-2.jpg"]):
    
        super().__init__(imageList, "/media/exp3.mp4", stack)
        self.SolsTab = TableMod(5, 8)
        
        self.setUPtable()
        self.SolsTab.setMinimumHeight(280)
        self.retBut = QPushButton("-RETRIEVE-")
        self.retBut.setEnabled(False)

        self.setUPEqui()
        self.dropCount = 0

        self.HclLoad = False
        self.ethLoad = False
        self.AceLoad = False
        self.eacLoad = False
        self.extra = False

        self.timerDis = ImageLabel("60:00")
        self.timerDis.setFont(QFont('Times', 20)) 
        self.timerDis.setStyleSheet("QLabel {border : 3px solid white;}")

        self.min = 60
        self.MINPER = 60
        self.sec = 0
        self.startFlag = False
        self.startBut = QPushButton("-START-")
        self.startBut.clicked.connect(self.START)

        
        
        self.timerTub = QTimer()
        self.timerTub.timeout.connect(self.showTime)

        self.TestMiscW = VoHGroup("V")
        self.TestMiscW.addWidgets([self.timerDis, self.startBut, self.retBut])
        self.TestMiscW.setMaximumWidth(142)
        

        self.RETFLAG = False
        
        self.SUB1.clicked.connect(self.SUBMIT1)
        self.SUB2.clicked.connect(self.SUBMIT2)
        
        self.retReset = ImageLabel("Please Do not reset\nbefore Feeding.\n\nUpload allowed \nonce per session")
        self.SUBFLAG1 = False
        self.SUBFLAG1 = False

        self.SUBGro = VoHGroup("V")
        self.SUBGro.addWidgets([self.SUB1, self.SUB2, self.retReset])
        
        self.InstructLAB1 = QLabel("1.LEFT UPPER HALF\nIS SOLUTION RACK\n\n2.LEFT LOWER HALF\nIS FOR EQUM.\n\n3.RIGTH SECTION\nIS FOR TITRATION")
        
        self.Instruct = VoHGroup("V")
        self.Instruct.addWidgets([self.InstructLAB1]) 
        self.Instruct.setMaximumWidth(171)
        
        self.EquiLAYW = VoHWidget("H")
        self.EquiLAYW.addWidgets([self.DropBox, self.TestMiscW, self.RetLAYW, self.SUBGro, self.Instruct])
        
        self.TitDrop = DropLabel("Bur", "media/bur-min.png",self)
        self.TitDrop.textChanged.connect(self.update3)

        self.FlaDrop = DropLabel("Flask", "media/flaskEm2.png", self)
        self.FlaDrop.textChanged.connect(self.update2)
        
        self.movie = VolSlider()

        self.reset2 = QPushButton("Reset")
        self.reset2.clicked.connect(self.RESET2)
        
        self.DROP2 = QGridLayout()
        self.DROP2.addWidget(self.movie, 0, 0, 3, 1)
        self.DROP2.addWidget(self.TitDrop.getLabel(), 0, 1, 1, 1)
        self.DROP2.addWidget(self.FlaDrop.getLabel(), 1, 1, 1, 1)
        self.DROP2.addWidget(self.reset2, 2, 1, 1, 1)
        self.DROP2W = QGroupBox()
        self.DROP2W.setLayout(self.DROP2)

        self.loadKI = PushButton("Add Indicator")
        self.loadNAOH = PushButton("Load NaOH")
        self.loadNAOH.clicked.connect(self.LoadHypo)
        
        self.loadStart = PushButton("START")
        self.loadStart.clicked.connect(self.START2)
        self.loadStop = PushButton("PAUSE")
        self.loadStop.clicked.connect(self.Pause)
        self.loadRe = PushButton("RESET")
        self.loadRe.clicked.connect(self.RESET2)

        self.volumeDisplay = ImageLabel("0.0")
        self.volumeDisplay.setFont(QFont('Times', 30))
        self.volumeDisplay.setStyleSheet("QLabel {border : 3px solid white;}")
        #self.volumeDisplay.setReadOnly(True)

        self.volumeSpeed = Dial()
        self.volumeSpeedDis = ImageLabel("0")
        self.volumeSpeedDis.setStyleSheet("QLabel {border : 3px}")
        self.volumeSpeed.valueChanged.connect(self.changedSpeed)
        self.setUPTITBOX()
        
        self.errorFlag = 0
        self.volumeDown = 0
        self.burCon = 0
        self.burVol = 0
        self.volFlask = 0
        self.conFlask = 0
        self.burFlag = False
        
        self.start = False
        self.timerTrials = QTimer()
        self.timerTrials.timeout.connect(self.hiddenTimer)
        #self.timerTrials.start(100)
        self.marker = 0
        self.resumeFlag = False
        self.LoadUn = False
        self.LoadedINFLASK = False
        self.loadStop.setEnabled(False)
        self.loadKI.setEnabled(False)
        self.loadKIFLAG = False
        self.LOADMARK = -5000

        self.eacCon = 0
        self.eacVol = 0
        
        self.HclCon = 0
        self.HclVol = 0
        self.ethCon = 0
        self.ethVol = 0
        self.aceCon = 0
        self.aceVol = 0
        self.totVol = 0
        self.Notcalculated = True
        self.FinX = 0
        self.time = 3600

        self.Side1W = VoHWidget("V")
        self.Side1W.addWidgets([self.SolsTab])
        self.Side1W.VBOX.addStretch()
        self.Side1W.addWidgets([self.EquiLAYW])
        
        self.pageBox3 = QHBoxLayout()
        self.pageBox3.addWidget(self.Side1W)
        self.pageBox3.addStretch()
        self.pageBox3.addWidget(self.MISCBOX)
        self.pageBox3.addWidget(self.DROP2W)
        self.pageBox3.addStretch()
        
        self.tab2.setLayout(self.pageBox3)

        self.UNKNOWNERROR = "-Unidentified-"

    def setUPEqui(self):

        self.EquiLab = DropLabel("TestTube", "media/emptytest.png", self)
        self.EquiLab.textChanged.connect(self.update)

        self.resetBUT = QPushButton("Reset")
        self.resetBUT.clicked.connect(self.RESET)

        self.RetLab = ImageLabel("RETRIEVE FLASK:")
        self.RetLab.setMaximumHeight(20)
        self.RetFlask = DragLabel(" HCl ", "media/empty2.png",res=True, parent=self)
        self.RetFlask.setCol(1)

        self.DropBox = VoHGroup("V")
        self.DropBox.addWidgets([self.EquiLab.getLabel(), self.resetBUT])
        self.DropBox.setMaximumWidth(142)
        self.RetLAYW = VoHGroup("V")
        self.RetLAYW.addWidgets([self.RetLab, self.RetFlask])
        self.RetLAYW.setMaximumWidth(170)

        self.retBut.clicked.connect(self.RETRIEVE)

        self.SUB1 = PushButton("Feed On-going\n reaction as\nTrial 1")
        self.SUB2 = PushButton("Feed On-going\n reaction as\nTrial 2")


    def SUBMIT1(self):

        if(self.totVol != 0):
            for i in [self.aceCon*self.aceVol/self.totVol, self.ethCon*self.ethVol/self.totVol,
                     self.eacCon*self.eacVol/self.totVol, (self.aceCon*self.aceVol-self.FinX)/self.totVol,
                     (self.ethCon*self.ethVol-self.FinX)/self.totVol, (self.eacCon*self.eacVol+self.FinX)/self.totVol]:
                self.dataGEN.append(round(i,3))

            self.SUBFLAG1 = True
            msg = QMessageBox()
            msg.setText("Feeding Success")
            msg.setInformativeText("Make sure both trials are fed in system before upload")
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Total Volume zero")
            msg.setWindowTitle("Zero Volume")
            msg.exec_()
        
    def SUBMIT2(self):
        
        if(self.totVol != 0 and self.SUBFLAG1 == True):
            for i in [self.aceCon*self.aceVol/self.totVol, self.ethCon*self.ethVol/self.totVol,
                     self.eacCon*self.eacVol/self.totVol, (self.aceCon*self.aceVol-self.FinX)/self.totVol,
                     (self.ethCon*self.ethVol-self.FinX)/self.totVol, (self.eacCon*self.eacVol+self.FinX)/self.totVol]:
                self.dataGEN.append(round(i, 3))

            self.SUBFLAG2 = True
            msg = QMessageBox()
            msg.setText("Feeding Success")
            msg.setInformativeText("Make sure both trials are fed in system before submit")
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Trial-1 is not fed or Total Volume zero")
            msg.setWindowTitle("Feed Trial-1 first/Zero Volume")
            msg.exec_()
        
    def update2(self):
        try:

            if(self.FlaDrop.text() == "Flask"):
                return
            if(self.start):
                self.errorFlag = 2
                self.errorMessage()
            else:
                 
                if(self.FlaDrop.name() == " NaOH "):
                    self.errorFlag = 10
                    self.errorMessage()
                
                elif(self.FlaDrop.name() == " Phenolphthalein "):
                    self.loadKIFLAG = True
                        
                elif(self.FlaDrop.col() == 1):
                    self.FlaDrop.setImage("media/flaskB2.png")
                    #self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskB2.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    self.LoadedINFLASK = True
                    self.volFlask = self.FlaDrop.vol()*self.FlaDrop.con()
                    self.conFlask += self.volFlask
                       
                    '''   
                    else :
                        self.errorFlag = 8
                        self.errorMessage()
                    '''
                    
                else:
                    self.errorFlag = 11
                    self.errorMessage()   
            self.FlaDrop.setText("Flask")
            
        except:
            self.UNKNOWNERROR = "Updating Flask parameters"
            self.errorMessage()
            self.FlaDrop.setText("Flask")
        
    def update3(self):	
        try:
            if(self.TitDrop.text() == "Bur"):
                return
            if(self.resumeFlag):
                if(self.TitDrop.name() == " NaOH "):
                   try:
                       self.burVol = self.TitDrop.vol()
                       self.movie.setValue(int((self.burVol*100)-5000))
                       self.LOADMARK = (self.burVol*100)-5000
                       self.marker = 0
                       if(self.resumeFlag):
                           self.resumeFlag = False
                   except:
                        self.UNKNOWNERROR = "Refilling Burette through drag and drop"
                        self.errorMessage()
                   self.TitDrop.setText("Bur")
                   return
                   
                else:
                   self.errorFlag = 10
                   self.errorMessage()
                   self.TitDrop.setText("Bur") 
                   return         

            if(self.start):
                self.errorFlag = 2
                self.errorMessage()
            else:
                if(self.TitDrop.name() == " NaOH "):
                    
                    self.burCon = self.TitDrop.con()
                    self.burVol = self.TitDrop.vol()
                    self.movie.setValue(int((self.burVol*100)-5000))
                    self.LOADMARK = (self.burVol*100)-5000
                    self.burFlag = True

                else:
                    self.errorFlag = 10
                    self.errorMessage()
            self.TitDrop.setText("Bur")
        except Exception as e:
            self.UNKNOWNERROR = "Updating Burette parameters and "+str(e)
            self.errorMessage()
            self.TitDrop.setText("Bur")
    def RESET2(self):
        try:
            self.timerTrials.stop()
            self.burFlag = False
            self.start = False
            self.volFlask = 0
            self.conFlask = 0
            self.burCon = 0
            self.burVol = 0
            self.LoadedINFLASK = False
            self.volumeDown = 0
            self.marker = 0
            self.resumeFlag = False
            self.FlaDrop.setImage("media/flaskEm2.png")
            #self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskEm2.png); background-repeat: no-repeat;background-position: 0% 0%;}")
            self.loadKIFLAG = False
            self.RESETDROP(self.FlaDrop, "Flask")
            self.RESETDROP(self.TitDrop, "Bur")
            self.start = False
            self.loadNAOH.setEnabled(True)
            self.LOADMARK = -5000
            self.movie.setValue(-5000)
            self.timerTrials.stop()
            self.loadStop.setText("PAUSE")
            self.loadStart.setEnabled(True)
            self.loadStop.setEnabled(False)
        except:
            self.UNKNOWNERROR = "Reseting Titration parameters"
            self.errorMessage()
            
    def RESETDROP(self, drop, name):
        drop.setCon(0)
        drop.setVol(0)
        drop.setCol(0)
        drop.setName(name)
        drop.setText(name)
        
    def changedSpeed(self):
        try:
            speed = self.volumeSpeed.value()
            self.timerTrials.start(100-speed)
        except Exception as e:
            self.UNKNOWNERROR = "Changing Titration Speed and " + str(e)
            self.errorMessage()

    def Pause(self):
        try:
            if(self.loadStop.text() == "PAUSE"):
                self.timerTrials.stop()
                self.loadStop.setText("RESUME")

            else :
                self.timerTrials.start(100-self.volumeSpeed.value())
                self.loadStop.setText("PAUSE")
        except Exception as e:
            self.UNKNOWNERROR = "Starting/Pausing the titration and " + str(e)
            self.errorMessage()
            
    def LoadHypo(self):
        try:
            self.marker = 0
            self.movie.setValue(int(self.LOADMARK))
            #self.loadNAOH.setEnabled(False)
            if(self.resumeFlag):
                self.resumeFlag = False
        except Exception as e:
            self.UNKNOWNERROR = "Refilling Burette and " +str(e)
            self.errorMessage()

    def START2(self):
        try:
            if(self.LoadedINFLASK and  self.burFlag):
                if(self.loadKIFLAG):
                    
                    self.volumeDown = (100*self.conFlask)/self.burCon
                    self.marker = 0
                    self.volumeDown = int(self.volumeDown)
                    #print(self.volumeDown)

                    self.start = True    
                    self.timerTrials.start(100-self.volumeSpeed.value())
                    self.loadStart.setEnabled(False)
                    self.loadStop.setEnabled(True)
                else:
                    self.errorFlag = -1
                    self.errorMessage()
            else :
                self.errorFlag = -2
                self.errorMessage()
        except:
            self.UNKNOWNERROR = "Starting the reaction"
            self.errorMessage()
        
    def hiddenTimer(self):
        try:
            if self.start and self.resumeFlag == False:
                
                self.volumeDown -= 1
                self.marker += 1
                
                if (self.volumeDown <= 20 and self.volumeDown >= -20):
                    self.FlaDrop.setImage("media/flaskE2.png")
                    #self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskE2.png); background-repeat: no-repeat;background-position: 0% 0%;}")

                elif(self.volumeDown <= -20 and self.volumeDown >= -25):
                    self.FlaDrop.setImage("media/flaskC2.png")
                    #self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskC2.png); background-repeat: no-repeat;background-position: 0% 0%;}")

            if self.start:
                #text = (self.volumeDown/100)
                self.movie.setValue(int(self.LOADMARK-self.marker))
                self.volumeDisplay.setText(str(round(self.marker/100, 1)))
                
                if(self.LOADMARK-self.marker <= -4999):
                    self.timerTrials.stop()
                    #self.RESETDROP(self.TitDrop, "Bur")
                    #print(self.volumeDown)
                    self.loadStop.setText("RESUME")
                    self.loadNAOH.setEnabled(True)
                    self.resumeFlag = True
                    self.errorFlag = 12
                    self.errorMessage()
                    
                
            
        except Exception as e:
            #print(e)
            self.UNKNOWNERROR = "Starting/Stoping Timer and " + str(e)
            self.errorMessage()
    def update(self):
        try:
            if(self.EquiLab.text() == "EquiLab"):
                return

            PASS = False
            if(self.startFlag == False):
                if(self.EquiLab.name()==" HCl "):
                    if(self.HclLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.HclCon = self.EquiLab.con()
                        self.HclVol = self.EquiLab.vol()
                        self.HclLoad = True
                        
                elif(self.EquiLab.name()==" Acetic Acid "):
                    if(self.AceLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.aceCon = self.EquiLab.con()
                        self.aceVol = self.EquiLab.vol()
                        self.AceLoad = True
                        
                elif(self.EquiLab.name()==" Ethanol "):
                    if(self.ethLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.ethCon = self.EquiLab.con()
                        self.ethVol = self.EquiLab.vol()
                        self.ethLoad = True
                        
                elif(self.EquiLab.name()==" Ethyl Acetate "):
                    if(self.eacLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.eacCon = self.EquiLab.con()
                        self.eacVol = self.EquiLab.vol()
                        self.eacLoad = True
                        
                else:
                    self.extra = True


                if(PASS == False):   
                    self.dropCount += 1
                    if(self.dropCount == 1):
                        self.EquiLab.setImage("media/l1test.png")
                        #self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l1test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    elif(self.dropCount == 2):
                        self.EquiLab.setImage("media/l2test.png")
                        #self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l2test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    elif(self.dropCount == 3):
                        self.EquiLab.setImage("media/l3test.png")
                        #self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l3test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    elif(self.dropCount == 4):
                        self.EquiLab.setImage("media/l4test.png")
                        #self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l4test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    else:
                        self.errorFlag = 5
                        self.errorMessage()
            else:
                self.errorFlag = 2
                self.errorMessage()
                      
            self.EquiLab.setText("EquiLab")
        except:
            self.UNKNOWNERROR = "Updating Flask parameters"
            self.errorMessage()
        
    def CHANGERESET(self):
        self.RESETDROP(self.EquiLab, "EquiLab")
        self.EquiLab.setImage("media/emptytest.png")
        self.RESETDROP(self.RetFlask, "flask")
        self.RetFlask.setImage("media/empty2.png")
        self.retBut.setEnabled(False)


    def RESET(self):
        try:
            self.dropCount = 0
            #self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/emptytest.png); background-repeat: no-repeat;background-position: 0% 0%;}")
            self.HclLoad = False
            self.ethLoad = False
            self.AceLoad = False
            self.eacLoad = False
            self.extra = False
            self.sec = 0
            self.min = self.MINPER
            self.startFlag = False
            self.timerTub.stop()
            self.timerDis.setText(str(self.MINPER)+":00")
            self.HclCon = 0
            self.HclVol = 0
            self.ethCon = 0
            self.ethVol = 0
            self.aceCon = 0
            self.aceVol = 0
            self.totVol = 0
            self.eacCon = 0
            self.eacVol = 0
            self.FinX = 0
            self.time = 3600
            self.CHANGERESET()
        except:
            self.UNKNOWNERROR = "Reseting Equilibrium Flask"
            self.errorMessage()
            
    def RETRIEVE(self):
        timeSpent = (60-self.min)*60 + (60-self.sec)
        if( timeSpent >= self.time):
            x = self.FinX
        else:
            x = (self.FinX*timeSpent)/self.time
            x = round(x, 3)


        y2 = self.aceVol*self.aceCon - x
        con = (y2+ self.HclCon*self.HclVol)/self.totVol
        self.RetFlask.setCon(con)
        self.RetFlask.setVol(self.totVol)
        self.RetFlask.setCol(1)
        self.RetFlask.setImage("media/fill2.png")
    
    def START(self):
        if(self.startFlag == False):
            if(self.HclLoad and self.ethLoad and self.AceLoad):
                if(self.extra == False):
                    self.startFlag = True
                    self.errorFlag = 6
                    self.errorMessage()
                    y1 = self.ethCon*self.ethVol
                    y2 = self.aceVol*self.aceCon
                    y3 = self.eacVol*self.eacCon
                    a = 3.33
                    b = -4.33*(y1+y2) - y3
                    c = 4.33*(y1*y2)
                    # calculate the discriminant
                    d = (b**2) - (4*a*c)
                    # find two solutions
                    sol1 = (-b-cmath.sqrt(d))/(2*a)
                    sol2 = (-b+cmath.sqrt(d))/(2*a)
                    self.totVol = self.ethVol + self.aceVol + self.HclVol
                    if(sol1.imag == 0):
                        self.time = 3600 + ((15-self.HclCon*self.HclVol)*10)
                        if(y1-sol1.real >= 0 and y2-sol1.real >= 0 and y3+sol1.real >= 0):
                            self.FinX = round(sol1.real, 3)
                        elif(y1-sol2.real >= 0 and y2-sol2.real >= 0 and y3+sol2.real >= 0):
                            self.FinX = round(sol2.real, 3)
                        #if(self.FinX):
                            #print("Calculation of equilibrium concetraion done")
                            #print(str(self.time)+" : "+str(self.FinX))
                    else:
                        self.errorMessage()
                    self.retBut.setEnabled(True)
                    self.timerTub.start(1000)
                else :
                    self.errorFlag = 3
                    self.errorMessage()
                    return
            else :
                self.errorFlag = 4
                self.errorMessage()
                return
        else:
            self.errorFlag = 2
            self.errorMessage()
            return
        
    def showTime(self):
        if(self.startFlag):
            if(self.sec <= 0):
                
                if(self.min <= 0):
                    self.timerTub.stop()
                    self.startFlag = False
                    self.errorFlag = 9
                    self.errorMessage()
                else:
                    self.sec = 60
                    self.min = self.min -1
            else :
                self.sec = self.sec-1

            if(self.sec >= 10):
                second = str(self.sec)
            else:
                second = "0"+str(self.sec)
            if(self.min >= 10):
                minute = str(self.min)
            else:
                minute = "0"+str(self.min)
            self.timerDis.setText(minute+":"+second)
        
        
    def VolEntry(self):
        column = self.SolsTab.currentColumn()
        val = self.SolsTab.cellWidget(4, column).value()
        valAva = self.SolsTab.cellWidget(2, column).value()
        if(val > valAva):
            self.errorFlag = 1
            self.errorMessage()
            self.SolsTab.cellWidget(4, column).setValue(0)
            return
        #valAva = valAva-val
        #self.SolsTab.cellWidget(2, column).setValue(valAva)
        self.SolsTab.cellWidget(3, column).setVol(val)
        
    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        title  = "Unknown Error"
        text = "Unidentified error. Try reset or restarting the program.Report a bug.\nPotential Error:>" + self.UNKNOWNERROR
        textMain ="Instrument Error!"
        
        if(self.errorFlag == 1):
            text = "Please Enter the Volume within the available Amount"
            textMain = "Volume is not available"
            title = "VOLUME UNAVAILABLE ERROR"
        elif(self.errorFlag == 2):
            title  = "ONGOING REACTION ERROR"
            text = "Previous reaction is already in progess. Reset and try again."
            textMain ="Reaction in progress"
        elif(self.errorFlag == 3):
            title = "EXTRA COMPONENTS ERROR"
            text = "Reset recommended. Extra components are present, which will hamper reaction and equilibrium"
            textMain ="Extra components in test tube."
        elif(self.errorFlag == 4):
            text = "Some Components are missing from the reaction mixture. Plese reverify and try again."
            textMain = "Missing Components"
            title = "ERROR"
        elif(self.errorFlag == -1):
            text = "Indicator is missing from the reaction mixture. Plese add indicator."
            textMain = "Missing Indicator"
            title = "NO INDICATOR"
        elif(self.errorFlag == -2):
            text = "Titrant is missing from the Flask. Plese Drag and drop a Titrant."
            textMain = "Missing Solution"
            title = "NO TITRANT"

        elif(self.errorFlag == 5):
            text = "Warning! Exceeding test tube volume. No More solutions can be added."
            textMain = "Overflow !"
            title = "ATTENTION Overflow"
        elif(self.errorFlag == 6):
            text = "ATTENTION !! Reaction in Flask will now start. Please keep your Timer handy."
            title = "ATTENTION ! Reaction start"
            textMain = "REACTION START"
        elif(self.errorFlag == 7):
            text = "ATTENTION !! Nothing is Loaded. Drag and drop a Flask."
            title = "ATTENTION ! Empty Test tube"
            textMain = "EMPTY Test tube"
            
        elif(self.errorFlag == 8):
            text = "ATTENTION !!This solution is already loaded. Load another sample or Reset"
            title = "ATTENTION ! Solution Loaded"
            textMain = "Solution is already loaded."
        elif(self.errorFlag == 9):
            text = "ATTENTION !! Reaction in Flask has reached it's end. You May retrieve your solution."
            title = "ATTENTION ! Reaction COMPLETE"
            textMain = "REACTION COMPLETE"
            
        elif(self.errorFlag == 10):
            text = "Please add NaOH in burette. It is preffered that NaOH is added in Burrete instead of any other solution ."
            textMain = "NaOH preffered in burette"
            title = "Attention !"
            
        elif(self.errorFlag == 11):
            text = "The Solution added is not titrable. Please reverify and add another solution in flask."
            textMain = "Non titrable solution added"
            title = "Attention !"

        elif(self.errorFlag == 12):
            title = "NaOH"
            text = "Warning! Load NaOH in Burrete to Resume. Load and then Resume"
            textMain = "LOAD NaOH"

        if(self.errorFlag >= 5):
            self.w.setIcon(QMessageBox.Information)
        else:
            self.w.setIcon(QMessageBox.Critical)
        self.w.setText(textMain)
        self.w.setInformativeText(text)
        self.w.setWindowTitle(title)
        self.w.exec()
        self.errorFlag = 0
        self.UNKNOWNERROR = "Unidentified"
        
    def setUPtable(self):
        names = ["Sols->"," HCl ", " NaOH ", " Acetic Acid ", " Ethanol ", " Oxalic Acid ", " Ethyl Acetate ", " Phenolphthalein "]
        for i in range(8) :
            self.SolsTab.setCellWidget(0, i, ImageLabel(names[i]))

            if(i):
                self.SolsTab.setCellWidget(3, i, DragLabel(names[i], "media/light2.png", True, self))
                self.SolsTab.setCellWidget(4, i, QDoubleSpinBox())
                self.SolsTab.cellWidget(4, i).valueChanged.connect(self.VolEntry)
                temp2 = ImageLabel("")
                temp2.setFont(QFont('Times'))
                self.SolsTab.setCellWidget(1, i, temp2)
                self.SolsTab.setCellWidget(2, i, QDoubleSpinBox())
                self.SolsTab.cellWidget(2, i).setReadOnly(True)
            else:
                self.SolsTab.setCellWidget(1, i, ImageLabel("Conc->"))
                self.SolsTab.setCellWidget(2, i, ImageLabel("Vol->"))
                self.SolsTab.setCellWidget(3, i, ImageLabel("Flask->"))
                self.SolsTab.setCellWidget(4, i, ImageLabel("Vol Taken (ml)->"))
                
        self.SolsTab.cellWidget(3, 1).setCon(3+(random.randint(-99, 99)/100))

        self.SolsTab.cellWidget(1, 1).setText("~3N")
        self.SolsTab.cellWidget(3, 1).setCol(2)
        self.SolsTab.cellWidget(2, 1).setValue(15)
        self.SolsTab.cellWidget(3, 2).setCon(1+(random.randint(-99, 99)/100))

        self.dataGEN.append(self.SolsTab.cellWidget(3, 1).con())
        self.dataGEN.append(self.SolsTab.cellWidget(3, 2).con())

        self.SolsTab.cellWidget(1, 2).setText("~1N")
        self.SolsTab.cellWidget(2, 2).setValue(50)
        self.SolsTab.cellWidget(3, 2).setCol(1)

        self.SolsTab.cellWidget(3, 3).setCon(17.5)
        self.SolsTab.cellWidget(1, 3).setText("~17.5M")
        self.SolsTab.cellWidget(2, 3).setValue(5)
        self.SolsTab.cellWidget(3, 3).setCol(1)
        self.SolsTab.cellWidget(3, 4).setCon(17.1)
        self.SolsTab.cellWidget(1, 4).setText("~17.1M")
        self.SolsTab.cellWidget(2, 4).setValue(15)
        self.SolsTab.cellWidget(3, 5).setCon(0.3)
        self.SolsTab.cellWidget(1, 5).setText("0.3N")
        self.SolsTab.cellWidget(2, 5).setValue(30)
        self.SolsTab.cellWidget(3, 5).setCol(2)

        self.SolsTab.cellWidget(3, 6).setCon(10.2)
        self.SolsTab.cellWidget(1, 6).setText("~10.2M")
        self.SolsTab.cellWidget(2, 6).setValue(10)
        self.SolsTab.cellWidget(3, 7).setCon(4.1)
        self.SolsTab.cellWidget(3, 7).setCol(0)
        self.SolsTab.cellWidget(1, 7).setText("~4.1M")
        self.SolsTab.cellWidget(2, 7).setValue(4)
        
        self.SolsTab.resizing()

        self.SolsTab.cellWidget(3, 7).setImage("media/pink2.png")

    def setUPTITBOX(self):
        
        self.ButtonBox = VoHGroup("V")
        self.ButtonBox.addWidgets([self.loadNAOH, self.loadStart, self.loadStop, self.loadRe])

        self.SPEEDLAB = ImageLabel("-SPEED-")
        self.SPEEDLay = QVBoxLayout()
        self.SPEEDBOX = VoHGroup("V")
        self.SPEEDBOX.addWidgets([self.volumeSpeed,self.SPEEDLAB])
            
        self.MISCBOX = VoHGroup("V")
        self.MISCBOX.addWidgets([self.volumeDisplay, self.ButtonBox, self.SPEEDBOX])