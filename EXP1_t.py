from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import os
FOLDER = os.getcwd()

dataGEN = [0, 0, 0, 0, 0, 0, 0, 0, 0]

class Exp1_class(QTabWidget):
    def __init__(self):
        super().__init__()
        #self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        #self.tabs.resize(300,200)
        # Add tabs
        self.addTab(self.tab1," Theory ")
        self.addTab(self.tab2," Perform ")
        self.addTab(self.tab3, " Video ")
        self.addTab(self.tab4, " Question Bank ")
        self.setFont(QFont('Times', 12))
        self.label = QLabel("1.STANDARDIZING HYPO SOLUTION\n( with known concentration of CuSO4)")
        #self.label2 = QLabel(" Prepare standard CuSO4.5H2O soln :")        
        self.label3 = QLabel("Enter weight(grm) of CuSO4.5H2O:")
        self.label32 = QLabel("Enter volm (ml) of flask for sol:")
        self.WeightLine = QLineEdit()
        self.WeightLine.setText("0.00")
        self.WeightLine.editingFinished.connect(self.getValidate)
        self.VolLine = QLineEdit()
        self.VolLine.setText("100")
        self.VolLine.editingFinished.connect(self.getValidate2)
        self.VolLine.setReadOnly(True)
        self.GetCo = QPushButton("GET SOLUTION")
        self.GetCo.clicked.connect(self.GetSolution)
        self.AddNaCO3 = QPushButton("ADD NaCO3")
        self.AddNaCO3.clicked.connect(self.GetSolution1)
        self.Addglac = QPushButton("ADD CH3COOH")
        self.Addglac.clicked.connect(self.GetSolution2)
        self.Makeup = QPushButton("MAKE UP VOLM\n(100 ml)")
        self.Makeup.clicked.connect(self.GetSolution3)

        self.Loadflask = QPushButton("Load in Con. Flask")
        self.loadRESET = QPushButton("RESET")
        self.loadRESET.setFont(QFont('Times', 12))
        self.loadRESET.clicked.connect(self.RESET2)
        self.Loadflask.clicked.connect(self.loadInFlask)

        self.conCo = 0.001

        for i in [self.GetCo, self.AddNaCO3, self.Addglac, self.Makeup, self.Loadflask]:
            i.setEnabled(False)

        self.form1Ly = QFormLayout()
        self.form1Ly.addRow(self.label)

        self.label4 = QLabel("Hypo-Standard")
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setPixmap(QPixmap("media/hypo_empt.jpg"))
        
        self.volLay = QHBoxLayout()
        self.VolLabel = QLabel("Enter Vol(ml) of CuSO4 soln\n(Taken in conical flask)")
        self.VolTaken = QDoubleSpinBox()

        self.form2Ly = QFormLayout()
        self.form2Ly.addRow(self.label3, self.WeightLine)
        self.form2Ly.addRow(self.GetCo) 
        self.form2Ly.addRow(self.AddNaCO3, self.Addglac)
        #self.form2Ly.addRow(self.label32, self.VolLine)
        self.form2Ly.addRow(self.Makeup)
        self.form2Ly.addRow(self.VolLabel, self.VolTaken)
        self.form2Ly.addRow(self.Loadflask)
        self.form2Ly.addRow(self.loadRESET)

        self.temp = QGroupBox()
        self.temp.setLayout(self.form2Ly)

        self.form1Ly.addRow(self.temp, self.label4)
    

        self.form1Box = QWidget()
        self.form1Box.setLayout(self.form1Ly)
        
        self.label7 = QLabel("2. STANDARDIZE HYPO SOLUTION :")
        self.label8 = QLabel()

        self.label8.setAlignment(Qt.AlignCenter)
        self.label8.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.gethio = QPushButton("GET Na2S2O2.5H2O")
        self.gethio.setFont(QFont('Times', 12))
        self.gethio.clicked.connect(self.GetSolution4)
        self.getTHIOFLAG = False
        self.stThio = 0.01
        self.VolThio = 100
        self.volLabelThio = QLabel("Volume Generated :\n-NA-")
        self.volLabelThio.setFont(QFont('Times', 10))

        self.hypoLay = QGridLayout()
        self.hypoLay.addWidget(self.label7, 0, 0, 1, 4)
        self.hypoLay.addWidget(self.volLabelThio, 1, 0, 2, 2)
        self.hypoLay.addWidget(self.label8, 1, 2, 2, 2)
        self.hypoLay.addWidget(self.gethio, 3, 0, 1, 4)
        
        self.unLay = QGridLayout()

        self.label71 = QLabel("3. DETERMINE UNKOWN :")
        self.label71.setFont(QFont('Times', 10))
        self.label81 = QLabel()
        self.label81.setAlignment(Qt.AlignCenter)
        self.label81.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.getUn = QPushButton("GET UNKNOWN")
        self.getUn.clicked.connect(self.GetSolution5)
        self.getUn.setFont(QFont('Times', 12))
        self.load_FlaskUn = QPushButton("Load in flask")
        self.volLabelUn = QLabel("Volume of Unknown\nsolution:-NA-")
        self.volLabelUn.setFont(QFont('Times', 10))

        self.unLay.addWidget(self.label71, 0, 0, 1, 4)
        self.unLay.addWidget(self.volLabelUn, 1, 0, 2, 2)
        self.unLay.addWidget(self.label81, 1, 2, 2, 2)
        self.unLay.addWidget(self.getUn, 3, 0, 1, 4)
        self.unLay.addWidget(self.load_FlaskUn, 4, 0, 1, 4)
        
        self.load_FlaskUn.setEnabled(False)
        self.load_FlaskUn.setFont(QFont('Times', 10))
        self.load_FlaskUn.clicked.connect(self.loadInFlaskUn)
        self.stUn = 0.01
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
        
        self.HomeLay = QVBoxLayout()
        
        
        for i in[self.form1Box, self.restBox]:
            self.HomeLay.addWidget(i)

        for i, j in zip([self.label, self.label3,  self.VolLine, self.AddNaCO3, self.Makeup, self.VolLabel, self.VolTaken, self.tab1, self.tab4],
                        [self.label32, self.WeightLine, self.GetCo, self.Addglac, self.Loadflask, self.label7, self.tab2,self.tab3, self.label71]):
            i.setFont(QFont('Times', 10))
            j.setFont(QFont('Times', 10))
            
        self.Loadflask.setFont(QFont('Times', 12))   
        self.Title = QLabel("DETERMINING THE STRENGTH OF UNKNOWN SOLUTION OF CuSO4")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Title.setFont(QFont('Times', 12))
        #self.movie2.frameChanged.connect(self.repaint)
        ##print("insideClass1")
        self.movie = QSlider(Qt.Vertical)
        self.movie.setMinimumWidth(10)
        self.movie.setStyleSheet("QSlider {color : white;}")
        self.movie.setRange(-5000, 0)
        self.movie.setAutoFillBackground(True)
        self.movie.setValue(-5000)
        self.movie.setFocusPolicy(Qt.NoFocus)
        self.movie.setTickPosition(QSlider.TicksBothSides)
        self.movie.setTickInterval(1)
        self.movie.setEnabled(False)

        self.burretteMap = QLabel()
        self.burretteMap.setPixmap(QPixmap("media/burr_emp.jpg"))

        self.MEDIABOX = QHBoxLayout()
        self.MEDIABOX.addWidget(self.movie)
        self.MEDIABOX.addWidget(self.burretteMap)

        self.MEDIABOXX = QWidget()
        self.MEDIABOXX.setLayout(self.MEDIABOX)
        
        self.loadKI = QPushButton("Add KI")
        self.loadKI.clicked.connect(self.changeFlask)
        self.loadKSCN = QPushButton("Load Hypo in burette")
        self.loadKSCN.clicked.connect(self.LoadHypo)
        self.loadStart = QPushButton("START")
        self.loadStart.clicked.connect(self.start)
        self.loadStop = QPushButton("PAUSE")
        self.loadStop.clicked.connect(self.Pause)
        self.loadRe = QPushButton("RESET")
        self.loadRe.clicked.connect(self.Reset)

        self.volumeDisplay = QLabel("0.0")
        self.volumeDisplay.setFont(QFont('Times', 35))
        self.volumeDisplay.setAlignment(Qt.AlignCenter)
        self.volumeDisplay.setStyleSheet("QLabel {border : 4px solid white;}")
        #self.volumeDisplay.setReadOnly(True)

        self.volumeSpeed = QDial()
        self.volumeSpeed.setRange(-100, 100)
        self.volumeSpeedDis = QLabel("0")
        self.volumeSpeedDis.setAlignment(Qt.AlignCenter)
        
        #self.volumeSpeedDis.setFont(QFont('Times', 20))
        self.volumeSpeedDis.setStyleSheet("QLabel {border : 3px}")
        self.volumeSpeed.setValue(0)
        self.volumeSpeed.setNotchesVisible(True)
        self.volumeSpeed.valueChanged.connect(self.changedSpeed)
        #self.volumeSpeed.setEnabled(False)

        self.ButtonBox = QGroupBox()
        self.ButtonBox.setMaximumWidth(200)
        self.buttonLay = QVBoxLayout()

        
        for i in [self.loadKI, self.loadKSCN, self.loadStart, self.loadStop, self.loadRe]:
            self.buttonLay.addWidget(i)

        self.ButtonBox.setLayout(self.buttonLay)

        self.SPEEDLAB = QLabel("SPEED")
        self.SPEEDLAB.setMaximumHeight(30)
        self.SPEEDLAB.setAlignment(Qt.AlignCenter)
        self.SPEEDLay = QVBoxLayout()
        self.SPEEDBOX = QGroupBox()
        #self.SPEEDLay.addWidget(self.volumeSpeedDis)
        self.SPEEDLay.addWidget(self.volumeSpeed)
        self.SPEEDLay.addWidget(self.SPEEDLAB)
        self.SPEEDBOX.setLayout(self.SPEEDLay)
            
        for i, j in zip([self.loadKSCN, self.loadStop, self.volumeSpeedDis],
                     [self.loadKI, self.loadStart, self.loadRe]):
            i.setFont(QFont('Times', 12))
            j.setFont(QFont('Times', 12))
            
        self.MISCBOX = QGroupBox()
        self.MISCLAY = QVBoxLayout()
        self.MISCLAY.addWidget(self.volumeDisplay)
        self.MISCLAY.addWidget(self.ButtonBox)
        self.MISCLAY.addWidget(self.SPEEDBOX)
        self.MISCBOX.setLayout(self.MISCLAY)
        self.MISCBOX.setMaximumWidth(200)

        self.MEDIABOX.addWidget(self.MISCBOX)

        self.movieBox = QVBoxLayout()
        self.movieBox.addWidget(self.Title)
        self.movieBox.addWidget(self.MEDIABOXX)
        self.group1 = QGroupBox()
        self.group1.setLayout(self.movieBox)
        self.group2 = QGroupBox()
        self.group2.setLayout(self.HomeLay)
        self.group2.setMaximumWidth(550)

        self.pageBox = QHBoxLayout()
        self.pageBox.addWidget(self.group2)
        self.pageBox.addWidget(self.group1)
        self.NOTPAUSEFLAG = True
        self.tab2.setLayout(self.pageBox)
        
        self.otherPages()
        
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

    def RESET2(self):

        for i in [self.GetCo, self.AddNaCO3, self.Addglac, self.Makeup, self.Loadflask]:
            i.setEnabled(False)

        self.label4.setPixmap(QPixmap("media/hypo_empt.jpg"))
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText("Please Note:")
        msg.setInformativeText("This Operation does not reset already loaded sample and previously saved data. Generate and load to change.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        
    def start(self):
        if(self.start):
            self.errorFlag = 6
            self.errorMessage()
        else:    
            if(self.LoadedINFLASK ):
                if(self.loadKIFLAG):
                    global dataGEN
                    if(self.LoadUn == False):
                        mm = self.conCo * self.VolTaken.value()
                        self.volumeDown = (mm)/self.stThio
                        
                        dataGEN[0] = 0.24969 * mm
                        dataGEN[1] = mm
                        dataGEN[4] = self.volumeDown
                        dataGEN[2] = self.VolTaken.value()
                        dataGEN[3] = self.conCo
                        dataGEN[5] = self.stThio
                    else :
                        st = self.stUn+(float(random.randint(-10, 10)/100)*self.stUn)
                        self.volumeDown = (self.stUn * self.VolUn)/self.stThio
                        
                        dataGEN[7] = self.volumeDown
                        dataGEN[8] = st
                        dataGEN[6] = self.VolUn
                        
                    self.volumeDown = 100*self.volumeDown
                    
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
            else:
                self.burretteMap.setPixmap(QPixmap("media/burr_cu.jpg"))

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
        #self.movie.setValue(-5000)
        #self.volumeDisplay.setText("0.0")
        self.volumeDown = 0
        #self.marker = 5000
        self.loadKSCN.setEnabled(True)
        self.burretteMap.setPixmap(QPixmap("media/burr_emp.jpg"))
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
                self.burretteMap.setPixmap(QPixmap("media/burr_s.jpg"))
                #self.loadKI.setEnabled(False)
                self.loadKIFLAG = True
            else:
                self.errorFlag = 4
                self.errorMessage()
        
    def getValidate(self):
        try:
            flo = float(self.WeightLine.text())
            if(flo == 0):
                self.errorFlag = 2
                self.errorMessage()
            else:
                if (flo > 10 or flo < 0 ):
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
        self.label4.setPixmap(QPixmap("media/hypo1.jpg"))
        self.AddNaCO3.setEnabled(True)
        self.GetCo.setEnabled(False)
    def GetSolution1(self):
        self.Addglac.setEnabled(True)
        self.label4.setPixmap(QPixmap("media/hypo12.jpg"))
        self.AddNaCO3.setEnabled(False)
    def GetSolution2(self):
        try:
            flo = float(self.VolLine.text())
            if(flo > 0):
                self.Makeup.setEnabled(True)
                self.Addglac.setEnabled(False)
                self.label4.setPixmap(QPixmap("media/hypo2.jpg"))
        except:
            pass
        
        self.VolLine.setReadOnly(True)

    def GetSolution3(self):
        self.label4.setPixmap(QPixmap("media/hypo.jpg"))
        VolL = float(self.VolLine.text())*0.001
        moles = (float(self.WeightLine.text()) / 249.69 )
        moles = moles +(float((random.randint(-10, 10)))/100)* moles

        self.conCo = moles /VolL
        self.conCo = round(self.conCo, 2)
        self.Loadflask.setEnabled(True)
        self.Makeup.setEnabled(False)
        
    def GetSolution4(self):
        k = float(random.randint(1000, 10000))
        final_bur = k/10000
        
        self.stThio = final_bur
        self.VolThio = 100
        self.volLabelThio.setText("Volume Generated :\n100ml")
        self.label8.setPixmap(QPixmap("media/smallflask.jpg"))
        self.getTHIOFLAG = True
        
        
    def GetSolution5(self):
        k = float(random.randint(1000, 12000))
        final_bur = k/10000
        
        self.stUn = final_bur
        self.VolUn = float(random.randint(20, 30))
        self.volLabelUn.setText("Volume of Unknown\nsolution:"+str(self.VolUn)+" ml")
        self.label81.setPixmap(QPixmap("media/smallflask.jpg"))
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
                self.burretteMap.setPixmap(QPixmap("media/burr_cu.jpg"))
                self.loadKI.setEnabled(True)
            
    def loadInFlaskUn(self):
        if(self.LoadedINFLASK):
            self.errorFlag = 6
            self.errorMessage()
        else:
            self.LoadUn = True
            self.LoadedINFLASK = True
            self.burretteMap.setPixmap(QPixmap("media/burr_cu.jpg"))
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

    def play(self):
        
        fileName = FOLDER+"/media/exp1.mp4"
        if self.loaded1 == 0:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.playButton.setText("Pause")
            self.loaded1 = 1
            
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setText("Play")
            self.mediaPlayer.pause()
        else:
            self.playButton.setText("Pause")
            self.mediaPlayer.play()
 
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
 
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
 
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
 
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

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
        
        
    def otherPages(self):
        self.l1 = QLabel()
        self.l1.setPixmap(QPixmap("media/Copper-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l1.setAlignment(Qt.AlignCenter)
        
        self.l2 = QLabel()
        self.l2.setPixmap(QPixmap("media/Copper-2.jpg"))
        self.l2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l2.setAlignment(Qt.AlignCenter)

        self.tab3text = QPlainTextEdit()
        self.tab4text = QPlainTextEdit()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton = QPushButton("Play")
        self.playButton.setEnabled(True) #default is on False, will not play video
        #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
        self.playButton.clicked.connect(self.play)  #when clicked, should play
 
        self.positionSlider = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider.setRange(0, 0) #setting the range of the slider
        self.positionSlider.sliderMoved.connect(self.setPosition)
 
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
        # Create a widget for window contents
 
        # Create layouts to place inside widget
        self.videoWidget = QVideoWidget()
        self.controlLayout = QHBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.addWidget(self.playButton)
        self.controlLayout.addWidget(self.positionSlider)
 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.videoWidget)
        self.layout.addLayout(self.controlLayout)
        self.layout.addWidget(self.errorLabel)
 
        # Set widget to contain window contents
        self.Video_widget = QWidget()
        self.Video_widget.setLayout(self.layout)
 
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.loaded1 = 0
        self.tab1Lay = QVBoxLayout()
        self.tab1Lay.addWidget(self.l1)
        self.tab1Lay.addWidget(self.l2)

        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.tab1Lay)

        self.scrollAr = QScrollArea()
        self.scrollAr.setWidget(self.scrollWidget)
        
        self.tab3Lay = QVBoxLayout()
        self.tab3Lay.addWidget(self.Video_widget)
        
        self.tab4Lay = QVBoxLayout()
        self.tab4Lay.addWidget(self.tab4text)
        
        self.tab1Lay2 = QVBoxLayout()
        self.tab1Lay2.addWidget(self.scrollAr)
        
        self.tab1.setLayout(self.tab1Lay2)
        self.tab3.setLayout(self.tab3Lay)
        self.tab4.setLayout(self.tab4Lay)
def getUnknowns():
    #print("YES BEING CALLED")
    global dataGEN
    return dataGEN


def main_exp1():
    obj = Exp1_class()
    return obj


