from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QDoubleValidator, QFont, QMovie
from PyQt5.QtWidgets import QDialog,QMessageBox, QVBoxLayout, QDoubleSpinBox, QWidget, QLabel, QGridLayout,QLineEdit, QPushButton, QGroupBox, QHBoxLayout
import random
from common import EXP_PAGE, ImageLabel
from ModWidgets import PushButton, FGroup, VoHGroup, VoHWidget, VolSlider, Dial

class Exp1_class(EXP_PAGE):
    def __init__(self, stack):
        self.dataGEN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        super().__init__(['media/Copper-1.jpg', 'media/Copper-2.jpg'], "media/exp1.mp4", stack)

        self.setFont(QFont('Times'))
        self.label = QLabel("1.STANDARDIZING HYPO SOLUTION\n(with known concentration of CuSO4)")
        self.label3 = QLabel("Enter wt (in gm) of CuSO4.5H2O:")
        self.label32 = QLabel("Enter volm (ml) of flask for sol:")

        self.WeightLine = QLineEdit()
        self.WeightLine.setText("0.00")
        self.WeightLine.setValidator(QDoubleValidator(0.0, 12.0, 2))
        self.WeightLine.editingFinished.connect(self.getValidate)

        self.VolLine = QLineEdit()
        self.VolLine.setText("100")
        self.VolLine.editingFinished.connect(self.getValidate2)
        self.VolLine.setReadOnly(True)

        self.GetCo = QPushButton("GET SOLUTION")
        self.GetCo.clicked.connect(self.GetSolution)
        self.AddNaCO3 = QPushButton("ADD Na2CO3")
        self.AddNaCO3.clicked.connect(self.GetSolution1)
        self.Addglac = QPushButton("ADD CH3COOH")
        self.Addglac.clicked.connect(self.GetSolution2)
        self.Makeup = QPushButton("MAKE UP VOL\n(100 ml)")
        self.Makeup.clicked.connect(self.GetSolution3)

        self.Loadflask = PushButton("Load in Con. Flask")

        self.loadRESET = PushButton("RESET")

        self.loadRESET.clicked.connect(self.RESET2)
        self.Loadflask.clicked.connect(self.loadInFlask)

        self.conCo = 0.000

        for i in [self.GetCo, self.AddNaCO3, self.Addglac, self.Makeup, self.Loadflask]:
            i.setEnabled(False)

        self.label4 = ImageLabel("Hypo-Standard", "media/hypo_empt.jpg")
        
        self.VolLabel = QLabel("Enter Vol (ml) of CuSO4 soln\n(Taken in conical flask)")
        self.VolTaken = QDoubleSpinBox()

        self.temp = FGroup("G")

        self.temp.addWidgets([[self.label3, self.WeightLine], [self.GetCo], [self.AddNaCO3, self.Addglac], [self.Makeup], [self.VolLabel, self.VolTaken], [self.Loadflask], [self.loadRESET]])
        
        self.form1Box = FGroup("W")
        self.form1Box.addWidgets([[self.label], [self.temp.Box, self.label4]])

        self.label7 = QLabel("2. STANDARDIZE HYPO SOLUTION :")

        self.label8 = ImageLabel("emp", "media/emptyflask.jpg")
        
        self.gethio = PushButton("GET Na2S2O3.5H2O")

        self.gethio.clicked.connect(self.GetSolution4)
        self.getTHIOFLAG = False

        self.stThio = 0.000000001
        self.VolThio = 100
        self.volLabelThio = ImageLabel("Volume Generated :\n-NA-")

        self.label71 = ImageLabel("3. DETERMINE UNKNOWN :")

        self.label81 = ImageLabel("empt2", "media/emptyflask.jpg")

        self.getUn = PushButton("GET UNKNOWN")
        self.getUn.clicked.connect(self.GetSolution5)

        self.load_FlaskUn = PushButton("Load in flask")

        self.volLabelUn = ImageLabel("Volume of Unknown\nsolution:-NA-")

        self.hypoLay = QGridLayout()
        self.hypoLay.addWidget(self.label7, 0, 0, 1, 4)
        self.hypoLay.addWidget(self.volLabelThio, 1, 0, 2, 2)
        self.hypoLay.addWidget(self.label8, 1, 2, 2, 2)
        self.hypoLay.addWidget(self.gethio, 3, 0, 1, 4)

        self.unLay = QGridLayout()
        self.unLay.addWidget(self.label71, 0, 0, 1, 4)
        self.unLay.addWidget(self.volLabelUn, 1, 0, 2, 2)
        self.unLay.addWidget(self.label81, 1, 2, 2, 2)
        self.unLay.addWidget(self.getUn, 3, 0, 1, 4)
        self.unLay.addWidget(self.load_FlaskUn, 4, 0, 1, 4)
        
        self.load_FlaskUn.setEnabled(False)
        self.load_FlaskUn.clicked.connect(self.loadInFlaskUn)
        self.stUn = 0.0
        self.stUn2 = 0.0
        self.VolUn = 0
        
        self.hypoBox = QGroupBox()
        self.hypoBox.setLayout(self.hypoLay)
        self.unBox = QGroupBox()
        self.unBox.setLayout(self.unLay)

        self.rest = QHBoxLayout()
        self.rest.addWidget(self.hypoBox)
        self.rest.addWidget(self.unBox)

        self.restBox = QWidget()
        self.restBox.setLayout(self.rest)

        self.group2 = VoHGroup("V")
        self.group2.addWidgets([self.form1Box.Box, self.restBox])

        for i, j in zip([self.label, self.label3,  self.VolLine, self.AddNaCO3, self.Makeup, self.VolLabel, self.VolTaken, self.tab1, self.tab4],
                        [self.label32, self.WeightLine, self.GetCo, self.Addglac, self.Loadflask, self.label7, self.tab2,self.tab3, self.label71]):
            i.setFont(QFont('Times'))
            j.setFont(QFont('Times'))
               
        self.Title = ImageLabel("DETERMINING THE STRENGTH OF UNKNOWN SOLUTION OF CuSO4")

        self.movie = VolSlider()

        self.burretteMap = ImageLabel("burr_emp", "media/burr_emp.jpg")
        
        self.loadKI = PushButton("Add KI")
        self.loadKI.clicked.connect(self.changeFlask)
        self.loadKSCN = PushButton("Load Hypo in burette")
        self.loadKSCNnStarch = PushButton("Add KSCN and Starch")
        self.loadKSCNnStarch.setEnabled(False)
        self.loadKSCNnStarch.clicked.connect(self.KSCNnStarch)
        self.loadKSCN.clicked.connect(self.LoadHypo)
        self.loadStart = PushButton("START")
        self.loadStart.clicked.connect(self.start)
        self.loadStop = PushButton("PAUSE")
        self.loadStop.clicked.connect(self.Pause)
        self.loadRe = PushButton("RESET")
        self.loadRe.clicked.connect(self.Reset)

        self.volumeDisplay = ImageLabel("0.0")
        self.volumeDisplay.setFont(QFont('Times', 35))
        self.volumeDisplay.setStyleSheet("QLabel {border : 4px solid white;}")

        self.volumeSpeed = Dial()
        self.volumeSpeed.valueChanged.connect(self.changedSpeed)

        self.ButtonBox = VoHGroup("V")
        
        self.ButtonBox.addWidgets([self.loadKI, self.loadKSCN, self.loadKSCNnStarch, self.loadStart, self.loadStop, self.loadRe])

        self.SPEEDLAB = ImageLabel("SPEED")

        self.SPEEDBOX = VoHGroup("V")
        self.SPEEDBOX.addWidgets([self.volumeSpeed, self.SPEEDLAB])
            
        self.MISCBOX = VoHGroup("V")
        self.MISCBOX.addWidgets([self.volumeDisplay, self.ButtonBox, self.SPEEDBOX])

        self.MEDIABOXX = VoHWidget("H")
        self.MEDIABOXX.addWidgets([self.movie, self.burretteMap, self.MISCBOX])

        self.group1 = VoHGroup("V")
        self.group1.addWidgets([self.Title, self.MEDIABOXX])
        
        self.pageBox = QHBoxLayout()
        self.pageBox.addWidget(self.group2)
        self.pageBox.addStretch()
        self.pageBox.addWidget(self.group1)
        self.NOTPAUSEFLAG = True
        self.tab2.setLayout(self.pageBox)
        
        self.errorFlag = 0
        self.volumeDown = 0
        self.start = False
        self.timerTrials = QTimer()
        self.timerTrials.timeout.connect(self.hiddenTimer)
        #self.timerTrials.start(100)
        self.marker = 5000
        self.resumeFlag = False
        self.LoadUn = False
        self.LoadedINFLASK = False
        self.loadStop.setEnabled(False)
        self.loadKI.setEnabled(False)
        self.loadKIFLAG = False
        self.setWindowTitle("IODOMETRY")

        self.timerIodine = QTimer()
        self.timerIodine.timeout.connect(self.showTime)
        self.settle = False
        self.time = 60
        self.starch  = False
        self.twoPerMarker = 0

    def RESET2(self):
        for i in [self.GetCo, self.AddNaCO3, self.Addglac, self.Makeup, self.Loadflask]:
            i.setEnabled(False)

        self.label4.setImage("media/hypo_empt.jpg")
        self.errorMessageM(QMessageBox.Information, "Attention", "This Operation does not reset already loaded sample and previously saved data. Generate and load to change.", "Please Note:")
        
    def start(self):
        if(self.start):
            self.errorFlag = 6
            self.errorMessage()
        else:    
            if(self.LoadedINFLASK ):
                if(self.loadKIFLAG):
                    if(self.LoadUn == False):
                        if(self.conCo == 0):
                            self.errorFlag = 1
                            self.errorMessage()
                            return
                        mm = self.conCo * self.VolTaken.value()
                        self.volumeDown = (mm)/self.stThio
                        
                        self.dataGEN[3] = self.VolTaken.value()
                        self.dataGEN[4] = mm*0.001
                        self.dataGEN[5] = self.volumeDown
                        self.dataGEN[6] = self.stThio
                    else :
                        if(self.stUn == 0):
                            self.errorFlag = 9
                            self.errorMessage()
                            return
                        #st = self.stUn+(float(random.randint(-10, 10)/100)*self.stUn)
                        self.volumeDown = (self.stUn * self.VolUn)/self.stThio
                        self.dataGEN[7] = self.VolUn
                        self.dataGEN[8] = self.volumeDown
                        self.dataGEN[9] = self.stUn
                        
                    self.volumeDown = 100*self.volumeDown
                    n = float(random.randint(20, 55)/100)
                    self.twoPerMarker = n*self.volumeDown
                    if(self.movie.value()<= -4990):
                        self.errorFlag = 3
                        self.errorMessage()
                        return
                    
                    else:
                        self.start = True
                        self.timerTrials.start(100-self.volumeSpeed.value())
                        self.loadStop.setEnabled(True)
                else:
                    self.errorFlag = 5
                    self.errorMessage()
            else :
                self.errorFlag = 4
                self.errorMessage()

        
    def hiddenTimer(self):
        if self.start :
            
            if self.volumeDown > 0:
                self.volumeDown -= 1
            if self.volumeDown <= self.twoPerMarker and self.starch != True:
                self.loadKSCNnStarch.setEnabled(True)
                self.burretteMap.setImage("media/paleYellow.png")

            elif self.starch and self.volumeDown <= 0:
                self.burretteMap.setImage("media/burr_cu.jpg")

        if self.start:
            self.marker+=1
            self.movie.setValue(0-self.marker)
            self.volumeDisplay.setText(str(round(self.marker/100, 1)))
            if(self.marker >= 4990):
                self.timerTrials.stop()
                #self.start = False
                self.loadStop.setText("PAUSE")
                self.Pause()
                self.resumeFlag = True
                self.errorFlag = 3
                self.errorMessage()

    def KSCNnStarch(self):
        if(self.volumeDown > 0):
            self.burretteMap.setImage("media/burr_dirtyBlue.jpg")
            self.starch = True
        self.loadKSCNnStarch.setEnabled(False)

    def Pause(self):

        if(self.loadStop.text() == "PAUSE"):
            self.timerTrials.stop()
            self.loadStop.setText("RESUME")
            self.NOTPAUSEFLAG = False

        else :
            if(self.resumeFlag):
                self.errorFlag = 3
                self.errorMessage()
            else:
                self.timerTrials.start(100-self.volumeSpeed.value())
                self.loadStop.setText("PAUSE")
                self.NOTPAUSEFLAG = True

    def Reset(self):
        self.timerTrials.stop()
        self.start = False
        self.volumeDown = 0
        self.twoPerMarker = 0
        self.starch = False
        self.loadKSCNnStarch.setEnabled(False)
        #self.marker = 5000
        self.loadKSCN.setEnabled(True)
        self.burretteMap.setImage("media/burr_emp.jpg")
        self.loadKI.setEnabled(False)
        self.LoadedINFLASK = False
        self.loadKIFLAG = False
        self.loadStart.setEnabled(True)
        self.loadStop.setText("PAUSE")
        self.loadStop.setEnabled(False)
        self.resumeFlag = False
        self.NOTPAUSEFLAG = True
        
    def changedSpeed(self):
        speed = self.volumeSpeed.value()
        if(self.start and self.NOTPAUSEFLAG):
            self.timerTrials.start(100-speed)
        
    def changeFlask(self):
        if(self.start):
            self.errorFlag = 6
            self.errorMessage()
        else:
            if(self.LoadedINFLASK):
                if(self.loadKIFLAG):
                    self.errorFlag = 8
                    self.errorMessage()
                else:
                    self.burretteMap.setImage("media/burr_s.jpg")
                    self.WaitAMinute()
            else:
                self.errorFlag = 4
                self.errorMessage()
        
    def WaitAMinute(self):

        self.Dialog = QDialog()

        self.sideAni = QMovie(self.resource_path("media/watchGlass.gif"))
        
        self.sideAni.frameChanged.connect(self.repaint)
        self.FlaskLab = ImageLabel()
        self.FlaskLab.setMovie(self.sideAni)
        self.sideAni.start()

        self.Infolabel = QLabel("I2 being liberated.\nPlease wait for a minute to let the Cu2I2 settle.\nPlease do not close untill timer stops.")
        self.timeLeft = QLabel("Time Remaining: 60")
        self.Dialog.setWindowTitle("I2 liberation")


        self.timerIodine.start(1000)
        self.LayoutDialog = QVBoxLayout()
        self.LayoutDialog.addWidget(self.FlaskLab)
        self.LayoutDialog.addWidget(self.Infolabel)
        self.LayoutDialog.addWidget(self.timeLeft)

        self.Dialog.setLayout(self.LayoutDialog)

        self.Dialog.exec_()
        self.timerIodine.stop()
        self.time = 60

    def showTime(self):
        if self.time <= 0:
            self.loadKIFLAG = True
            self.timerIodine.stop()
            self.time = 60
            self.Dialog.close()
            return
        if self.time == 20:
            self.FlaskLab.setImage("media/0.jpg")

        self.time -= 1
        self.timeLeft.setText("Time Remaining: "+str(self.time))

    def getValidate(self):
        try:
            flo = float(self.WeightLine.text())
            if(flo == 0):
                self.errorFlag = 2
                self.errorMessage()
            else:
                if (flo > 12 or flo < 0.5 ):
                    self.errorFlag = 1
                    #self.GetCo.setEnabled(False)
                    self.errorMessage()
                
                else :
                    self.GetCo.setEnabled(True)
                    #self.GetCo.setEnabled(False)
            
        except:
            self.GetCo.setEnabled(False)
            self.errorFlag = 2
            self.errorMessage()

    def GetSolution(self):
        self.label4.setImage("media/hypo1.jpg")
        self.AddNaCO3.setEnabled(True)
        self.GetCo.setEnabled(False)
    def GetSolution1(self):
        self.Addglac.setEnabled(True)
        self.label4.setImage("media/hypo12.jpg")
        self.AddNaCO3.setEnabled(False)
    def GetSolution2(self):
        try:
            flo = float(self.VolLine.text())
            if(flo > 0):
                self.Makeup.setEnabled(True)
                self.Addglac.setEnabled(False)
                self.label4.setImage("media/hypo2.jpg")
        except:
            pass
        
        self.VolLine.setReadOnly(True)

    def GetSolution3(self):
        self.label4.setImage("media/hypo.jpg")
        self.Loadflask.setEnabled(True)
        self.Makeup.setEnabled(False)
        
    def GetSolution4(self):
        if self.getTHIOFLAG != True :
            k = float(random.randint(1000, 19000))
            final_bur = k/10000
            self.stThio = final_bur

        self.VolThio = 100
        self.volLabelThio.setText("Volume Generated :\n100ml")
        self.label8.setImage("media/smallflask.jpg")
        self.getTHIOFLAG = True
            
    def GetSolution5(self):
        k = float(random.randint(1000, 12000))
        final_bur = k/10000
        
        self.stUn2 = final_bur
        self.VolUn = float(random.randint(20, 30))
        self.volLabelUn.setText("Volume of Unknown\nsolution:"+str(self.VolUn)+" ml")
        self.label81.setImage("media/smallflask.jpg")
        self.load_FlaskUn.setEnabled(True)


    def LoadHypo(self):
        if(self.getTHIOFLAG):
            self.marker = 0
            self.volumeDisplay.setText("0.0")
            self.movie.setValue(0)
            #self.loadKSCN.setEnabled(False)
            if(self.resumeFlag):
                self.resumeFlag = False
            #self.timerTrials.start(self.volumeSpeed.value())
        else:
            self.errorFlag = 7
            self.errorMessage()
        
    def loadInFlask(self):
        if(self.LoadedINFLASK):
            self.errorFlag = 6
            self.errorMessage()
        else:
            if(self.VolTaken.value() == 0):
                self.errorFlag = -1
                self.errorMessage()
                return
            else:
                self.LoadUn = False
                self.LoadedINFLASK = True
                self.burretteMap.setImage("media/burr_cu.jpg")
                self.loadKI.setEnabled(True)
                VolL = float(self.VolLine.text())*0.001
                moles = (float(self.WeightLine.text()) / 249.69 )
                moles = moles +(float((random.randint(-10, 10)))/100)* moles

                self.conCo = moles /VolL
                self.conCo = round(self.conCo, 2)

                self.dataGEN[0] = float(self.WeightLine.text())
                self.dataGEN[1] = moles
                self.dataGEN[2] = self.conCo
            
    def loadInFlaskUn(self):
        if(self.LoadedINFLASK):
            self.errorFlag = 6
            self.errorMessage()
        else:
            self.LoadUn = True
            self.LoadedINFLASK = True
            self.stUn = self.stUn2
            self.burretteMap.setImage("media/burr_cu.jpg")
            self.loadKI.setEnabled(True)
        
    def getValidate2(self):
        try:
            flo = float(self.VolLine.text())
            if(flo > 0):
                self.Makeup.setEnabled(True)
            else:
                    self.errorMessage()
        except:
            self.errorFlag = 0
            self.errorMessage()

    def errorMessage(self):
        
        title = "Unknown Error"
        text = "Instrument Error! Report a bug?"
        textM = "UNKNOWN ERROR"
        if(self.errorFlag == 1):
            text = "Warning! Out of range concentration.Too high or too low value."
            title = "RANGE ERROR"
            textM = "OUT OF RANGE"
        elif(self.errorFlag == -1):
            text = "Warning! Invalid Volume. Specify the volume to be taken in flask"
            title = "Zero Volume"
            textM = "ZERO VOLUME"
        elif(self.errorFlag == 2):
            title  = "INVALID ENTRY"
            text = "Provide a non-zero valid entry"
            textM = "ERROR !"
        elif(self.errorFlag == 3):
            title = "HYPO"
            text = "Warning! Load Hypo in Burrete to Resume. Load and then Resume"
            textM = "LOAD HYPO"
        elif(self.errorFlag == 4):
            title = "EMPTY FLASK"
            text = "Warning! Sample Not Loaded in flask. Load the sample first."
            textM = "FLASK IS EMPTY"
        elif(self.errorFlag == 5):
            text = "Attention! ADD KI as an indicator."
            title = "ADD KI"
            textM = "NO INDICATOR"
        elif(self.errorFlag == 6):
            text = "Attention! Previous sample is still Loaded. Please Reset First"
            title = "Loaded"
            textM = "RESET REQUIRED"
        elif(self.errorFlag == 7):
            text = "Attention! Hypo not created. Please Generate First"
            title = "No Hypo"
            textM = "HYPO GENERATION REQUIRED"

        elif(self.errorFlag == 8):
            text = "KI already added. Do a reset to perform this operation."
            title = "KI Already Loaded"
            textM = "RESET REQUIRED"
        elif(self.errorFlag == 9):
            text = "Attention! Unknown Cu sample not loaded. Please Generate and load in flask First"
            title = "No Sample"
            textM = "Unknown Cu GENERATION REQUIRED"


        self.errorFlag = 0
        self.w = QMessageBox()
        self.w.resize(150, 150)
        if(self.errorFlag >= 5):
            self.w.setIcon(QMessageBox.Information)
        else :
            self.w.setIcon(QMessageBox.Critical)
        self.w.setText(textM)
        self.w.setInformativeText(text)
        self.w.setWindowTitle(title)
        self.w.exec()