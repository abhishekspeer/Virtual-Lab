import random

from PyQt5.QtCore import QTimer
from ModWidgets import Dial, FGroup, PushButton, VoHGroup, VoHWidget, VolSlider
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtWidgets import QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton
from common import EXP_PAGE, ImageLabel
from DragNDrop import DragLabel, DropLabel


class Exp5_class(EXP_PAGE):
    
    def __init__(self, stack):
        super().__init__(["media/hard-1.jpg", "media/hard-2.jpg", "media/hard-3.jpg"], "media/exp5.mp4", stack)
        self.weight = ImageLabel("Wt of CaCO3 taken (mg):")
        self.weightLine = QLineEdit()
        self.weightLine.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ValBut = PushButton("Validate Weight")
        self.MakeUp = PushButton("Make Up Volm to 100 ml", False)
        self.flask = DragLabel("CaCO", "media/hypo_empt.jpg", True, self)
        self.flask.setName("CaCO")
        self.VolLab = ImageLabel("Volm taken for titration:")
        self.Vol4Tit = QDoubleSpinBox()
        self.Vol4Tit.setEnabled(False)
        self.addHCl = PushButton("ADD HCl", False)
        self.dataGEN = [0, 0, 0, 0, 0]
        self.ResetBUT = PushButton("RESET CaCO3")
        def validateWeight():
            try:
                w = float(self.weightLine.text())
                if(w < 0 or w>1000 or w == 0):
                    raise Exception
                con = float(w/10000) + float(random.randint(-5, 5)/100)*float(w/10000)
                self.flask.setCon(con)
                self.addHCl.setEnabled(True)
                self.ValBut.setEnabled(False)
                self.dataGEN[0] = w
                self.dataGEN[1] = con
            except:
                self.errorMessageM(QMessageBox.Critical, "Invalid Entry!", "Invalid Weight entered or out of range.", "Invalid")

        def resetCACO3():
            self.weightLine.setText("")
            self.ValBut.setEnabled(True)
            self.flask.setImage("media/hypo_empt.jpg")
            self.addHCl.setEnabled(False)
            self.Vol4Tit.setEnabled(False)
            self.Vol4Tit.setValue(0.00)
            self.MakeUp.setEnabled(False)
            self.errorMessageM(QMessageBox.Information, "RESET DONE", "Previous sample data is still saved untill you validate weight.", "Please Note")
        self.ResetBUT.clicked.connect(resetCACO3)
        def changeFlaskHCl():
            self.flask.setImage("media/hypo1.jpg")
            self.MakeUp.setEnabled(True)
            self.addHCl.setEnabled(False)

        def changeFlaskFull():
            self.flask.setImage("media/hypo.jpg")
            self.MakeUp.setEnabled(False)
            self.Vol4Tit.setEnabled(True)

        def volEntered():
            self.flask.setVol(self.Vol4Tit.value())

        self.ValBut.clicked.connect(validateWeight)
        self.addHCl.clicked.connect(changeFlaskHCl)
        self.MakeUp.clicked.connect(changeFlaskFull)
        self.Vol4Tit.valueChanged.connect(volEntered)

        self.Group1 = FGroup("G")
        self.Group1.addWidgets([[self.weight, self.weightLine], [self.ValBut], [self.addHCl],[self.MakeUp], [self.VolLab, self.Vol4Tit],[self.ResetBUT]])

        self.Group1Enc = VoHWidget("H")
        self.Group1Enc.addWidgets([self.Group1.Box, self.flask])

        self.EDTALab = ImageLabel("EDTA SOLn:")
        self.EDTAFlask = DragLabel("EDTA", "media/hypo.jpg", True, self)
        self.EDTAFlask.setName("EDTA")
        con = float(random.randint(90, 399))
        con = con/10000
        self.EDTAFlask.setCon(con)
        self.dataGEN[2] = con

        self.EDTAVol = QLabel("Vol Taken->")
        self.EDTALine = QDoubleSpinBox()

        def VolEDTAEntered():
            self.EDTAFlask.setVol(self.EDTALine.value())

        self.EDTALine.valueChanged.connect(VolEDTAEntered)

        def REGEN2():
            con = float(random.randint(90, 399))
            con = con/10000
            self.EDTAFlask.setCon(con)
            self.dataGEN[2] = con

        self.ReGen2 = QPushButton("REGENERATE")
        self.ReGen2.clicked.connect(REGEN2)

        self.Group2 = FGroup("G")
        self.Group2.addWidgets([[self.EDTALab], [self.EDTAFlask], [self.EDTAVol, self.EDTALine], [self.ReGen2]])

        self.UnknownLab = ImageLabel("Unknown Tap Water Sample:")
        self.Unknown = DragLabel("CaCO", "media/hypo.jpg", True, self)
        
        
        con = float(random.randint(99, 999))
        con = con/10000
        self.Unknown.setCon(con)
        vol = float(random.randint(15, 30))
        self.Unknown.setVol(vol)
        self.UnknownVolLab = ImageLabel("Volm : "+str(vol))
        self.dataGEN[3] = vol
        self.dataGEN[4] = con
        

        def REGEN():
            con = float(random.randint(99, 999))
            con = con/10000
            self.Unknown.setCon(con)

            vol = float(random.randint(15, 30))
            self.Unknown.setVol(vol)
            self.UnknownVolLab.setText("Volm : "+str(vol))
            self.dataGEN[3] = vol
            self.dataGEN[4] = con*0.1
        self.ReGen = QPushButton("REGENERATE")
        self.ReGen.clicked.connect(REGEN)

        self.Group3 = FGroup("G")
        self.Group3.addWidgets([[self.UnknownLab], [self.Unknown], [self.UnknownVolLab], [self.ReGen]])

        self.Group2Enc = VoHWidget("H")
        self.Group2Enc.addWidgets([self.Group2.Box, self.Group3.Box])

        self.GroupENC = VoHGroup("V")
        self.GroupENC.addWidgets([self.Group1Enc, self.Group2Enc])

        self.VolTit = VolSlider()
        self.Burr = DropLabel("Bur", "media/bur-min.png",self)
        self.Burr.textChanged.connect(self.update3)
        self.Conical = DropLabel("Flask", "media/flaskEm2.png", self)
        self.Conical.textChanged.connect(self.update2)

        self.DROP2 = QGridLayout()
        self.DROP2.addWidget(self.VolTit, 0, 0, 2, 1)
        self.DROP2.addWidget(self.Burr.getLabel(), 0, 1, 1, 1)
        self.DROP2.addWidget(self.Conical.getLabel(), 1, 1, 1, 1)
        self.DROP2W = QGroupBox()
        self.DROP2W.setLayout(self.DROP2)

        self.loadKI = PushButton("Add Eriochrome Black T ")
        self.loadKI.clicked.connect(self.loadEBT)
        self.loadNAOH = PushButton("Load EDTA")
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
        
        self.ButtonBox = VoHGroup("V")
        self.ButtonBox.addWidgets([self.loadKI, self.loadNAOH, self.loadStart, self.loadStop, self.loadRe])

        self.SPEEDLAB = ImageLabel("-SPEED-")
        self.SPEEDBOX = VoHGroup("V")
        self.SPEEDBOX.addWidgets([self.volumeSpeed,self.SPEEDLAB])
            
        self.MISCBOX = VoHGroup("V")
        self.MISCBOX.addWidgets([self.volumeDisplay, self.ButtonBox, self.SPEEDBOX])

        self.TITAREA = VoHWidget("H")
        self.TITAREA.addWidgets([self.DROP2W, self.MISCBOX])

        self.tab2Lay = QHBoxLayout()
        self.tab2Lay.addWidget(self.GroupENC)
        self.tab2Lay.addStretch()
        self.tab2Lay.addWidget(self.TITAREA)

        self.tab2.setLayout(self.tab2Lay)

        

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

    def changedSpeed(self):
        try:
            speed = self.volumeSpeed.value()
            self.timerTrials.start(100-speed)
        except Exception as e:
            self.UNKNOWNERROR = "Changing Titration Speed and " + str(e)
            self.errorMessageM(text=self.UNKNOWNERROR)

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
            self.Conical.setImage("media/flaskEm2.png")
            #self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskEm2.png); background-repeat: no-repeat;background-position: 0% 0%;}")
            self.loadKIFLAG = False
            self.loadKI.setEnabled(False)
            self.RESETDROP(self.Conical, "Flask")
            self.RESETDROP(self.Burr, "Bur")
            self.start = False
            self.loadNAOH.setEnabled(True)
            self.LOADMARK = -5000
            self.VolTit.setValue(-5000)
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
            self.errorMessageM(text=self.UNKNOWNERROR)
            
    def LoadHypo(self):
        try:
            self.marker = 0
            self.VolTit.setValue(int(self.LOADMARK))
            #self.loadNAOH.setEnabled(False)
            if(self.resumeFlag):
                self.resumeFlag = False
        except Exception as e:
            self.UNKNOWNERROR = "Refilling Burette and " +str(e)
            self.errorMessageM(text=self.UNKNOWNERROR)

    def loadEBT(self):
        if(self.start):
            self.errorFlag = 2
            self.errorMessage()
            
        if(self.LoadedINFLASK):
            if(self.loadKIFLAG):
                self.errorFlag = 8
                self.errorMessage()
            else:
                self.Conical.setImage("media/winered.png")
                self.loadKIFLAG=True
                self.loadKI.setEnabled(False)
        else:
            self.errorFlag = -2
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
                
                if (self.volumeDown <= 5 and self.volumeDown >= -5):
                    self.Conical.setImage("media/bright.png")
                    
            if self.start:
                self.VolTit.setValue(int(self.LOADMARK-self.marker))
                self.volumeDisplay.setText(str(round(self.marker/100, 1)))
                
                if(self.LOADMARK-self.marker <= -4999):
                    self.timerTrials.stop()
                    self.loadStop.setText("RESUME")
                    self.loadNAOH.setEnabled(True)
                    self.resumeFlag = True
                    self.errorFlag = 12
                    self.errorMessage()
    
        except Exception as e:
            self.UNKNOWNERROR = "Starting/Stoping Timer and " + str(e)
            self.errorMessage()

    def update2(self):
        try:

            if(self.Conical.text() == "Flask"):
                return
            if(self.start):
                self.errorFlag = 2
                self.errorMessage()

            else:
                 
                if(self.Conical.name() == "EDTA"):
                    self.errorFlag = 10
                    self.errorMessage()
                
                elif(self.Conical.name() == " Phenolphthalein "):
                    self.loadKIFLAG = True
                        
                elif(self.Conical.name() == "CaCO"):
                    self.Conical.setImage("media/flaskB2.png")
                    self.LoadedINFLASK = True
                    self.loadKI.setEnabled(True)
                    self.conFlask = self.Conical.vol()*self.Conical.con()
                    
                else:
                    self.errorFlag = 11
                    self.errorMessage()

            self.Conical.setText("Flask")
            
        except:
            self.UNKNOWNERROR = "Updating Flask parameters"
            self.errorMessage()
            self.Conical.setText("Flask")
        
    def update3(self):	
        try:
            if(self.Burr.text() == "Bur"):
                return
            if(self.resumeFlag):
                if(self.Burr.name() == "EDTA"):
                   try:
                       self.burVol = self.Burr.vol()
                       self.VolTit.setValue(int((self.burVol*100)-5000))
                       self.LOADMARK = (self.burVol*100)-5000
                       self.marker = 0
                       if(self.resumeFlag):
                           self.resumeFlag = False
                   except:
                        self.UNKNOWNERROR = "Refilling Burette through drag and drop"
                        self.errorMessage()
                   self.Burr.setText("Bur")
                   return
                   
                else:
                   self.errorFlag = 10
                   self.errorMessage()
                   self.Burr.setText("Bur") 
                   return         

            if(self.start):
                self.errorFlag = 2
                self.errorMessage()
            else:
                if(self.Burr.name() == "EDTA"):
                    
                    self.burCon = self.Burr.con()
                    self.burVol = self.Burr.vol()
                    self.VolTit.setValue(int((self.burVol*100)-5000))
                    self.LOADMARK = (self.burVol*100)-5000
                    self.burFlag = True

                else:
                    self.errorFlag = 10
                    self.errorMessage()
            self.Burr.setText("Bur")
        except Exception as e:
            self.UNKNOWNERROR = "Updating Burette parameters and "+str(e)
            self.errorMessage()
            self.Burr.setText("Bur")

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
        
        elif(self.errorFlag == -1):
            text = "Indicator is missing from the reaction mixture. Plese add indicator."
            textMain = "Missing Indicator"
            title = "NO INDICATOR"
        elif(self.errorFlag == -2):
            text = "Titrant is missing from the Flask. Plese Drag and drop a Titrant."
            textMain = "Missing Solution"
            title = "NO TITRANT"
            
        elif(self.errorFlag == 8):
            text = "ATTENTION !!This solution is already loaded. Load another sample or Reset"
            title = "ATTENTION ! Solution Loaded"
            textMain = "Solution is already loaded."
            
        elif(self.errorFlag == 10):
            text = "Please add EDTA in burette. It is preffered that EDTA is added in Burrete instead of any other solution ."
            textMain = "EDTA preffered in burette"
            title = "Attention !"
            
        elif(self.errorFlag == 11):
            text = "The Solution added is not titrable. Please reverify and add another solution in flask."
            textMain = "Non titrable solution added"
            title = "Attention !"

        elif(self.errorFlag == 12):
            title = "EDTA"
            text = "Warning! Load EDTA in Burrete to Resume. Load and then Resume"
            textMain = "LOAD EDTA"

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
        