
#import PyQt5
#import PyQt5.QtCore
from PyQt5.QtCore import *
#import PyQt5.QtGui
from PyQt5.QtGui import *
#import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import random
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
#import sheets
import cmath
global userID

import os
FOLDER = str(os.getcwd())

naoh = 0
hcl = 0
data1 = [0, 0, 0, 0, 0, 0]
data2 = [0, 0, 0, 0, 0, 0]

class MimeData(QMimeData):
    vol = 0
    con = 0
    name = "name"
    col = 0
    def __init__(self):
        super().__init__()
        
class DragLabel(QLabel):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.con_ = 0
        self.name_ = label
        self.vol_ = 0
        self.col_ = 0

    def setCon(self, data):
        self.con_ = data
    def setCol(self, data):
        self.col_ = data
    def setName(self, name):
        self.name_ = name
    def setVol(self, vol):
        self.vol_ = vol

    def name(self):
        return self.name_
    def con(self):
        return self.con_
    def vol(self):
        return self.vol_
    def col(self):
        return self.col_
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
 
    def mouseMoveEvent(self, event):
        if not(event.buttons() & Qt.LeftButton):
            return
        else:
            if(self.vol() == 0):
                #print("here")
                self.errorMessage()
                return
        
            drag = QDrag(self)
            #print("Here")
            mimedata = MimeData()
            #print("Con")
            mimedata.con = self.con()
            mimedata.col = self.col()
            mimedata.vol = self.vol()
            mimedata.name = self.name()
            #print("MIMING DONE")
            drag.setMimeData(mimedata)
            pixmap = QPixmap(self.size()) #
            
 
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
 
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)
            
    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        self.w.setIcon(QMessageBox.Warning)
        self.w.setText("Zero Volume Taken")
        self.w.setInformativeText("No Volume of solution taken!")
        self.w.setWindowTitle("Warning")
        self.w.exec()

        
class DropLabel(QLineEdit):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.setAcceptDrops(True)
        self.con_ = 0
        self.name_ = "name"
        self.loaded_ = False
        self.vol_ = 0
        self.col_ = 0

    def setCon(self, value):
        self.con_ = value

    def setCol(self, value):
        self.col_ = value

    def setName(self, name):
        self.name_ = name

    def setVol(self, flask):
        self.vol_ = flask

    def setLoaded(self, Bool):
        self.loaded_ = Bool
        
    def vol(self):
        return self.vol_
    def name(self):
        return self.name_
    def con(self):
        return self.con_
    def loaded(self):
        return self.loaded_
    def col(self):
        return self.col_
        
    def dragEnterEvent(self, event):
        #print("Enter")
        event.acceptProposedAction()
 
    def dropEvent(self, event):
        #print("Droper")

        pos = event.pos()
        #print("Okay1")
        self.setVol(event.mimeData().vol)
        #print("Okay")
        self.setName(event.mimeData().name)
        #print("Okay2")
        self.setCon(event.mimeData().con)
        #print("Okay3")
        self.setCol(event.mimeData().col)
            
        self.setText(str(self.name()))
            
        
        event.acceptProposedAction()


class Exp3_class(QTabWidget):
    def __init__(self):
        super().__init__()
        #self.tabs3 = QTabWidget()
        self.tab13 = QWidget()
        self.tab23 = QWidget()
        self.tab33 = QWidget()
        self.tab43 = QWidget()
        
        self.addTab(self.tab13," Theory ")
        self.addTab(self.tab23," Perform ")
        self.addTab(self.tab33, " Video ")
        self.addTab(self.tab43, " Question Bank ")
        
        self.setFont(QFont('Times', 12))

        self.SolsLab = QLabel("SOLUTION RACK")
        self.SolsTab = QTableWidget(5, 8)
        
        self.setUPtable()
        self.SolsTab.setMinimumHeight(280)

        self.EquiLab = DropLabel("EquiLab", self)
        self.EquiLab.textChanged.connect(self.update)
        self.EquiLab.setReadOnly(True)
        self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/emptytest.png); background-repeat: no-repeat;background-position: 0% 0%;}")
        self.EquiLab.setMinimumHeight(301)

        self.DisplayDrop = QLineEdit()
        self.DisplayDrop.setReadOnly(True)
        self.resetBUT = QPushButton("Reset")
        self.resetBUT.clicked.connect(self.RESET)
        self.dropCount = 0

        self.HclLoad = False
        self.ethLoad = False
        self.AceLoad = False
        self.eacLoad = False
        self.extra = False

        self.timerDis = QLabel("60:00")
        self.timerDis.setAlignment(Qt.AlignCenter)
        self.timerDis.setFont(QFont('Times', 15)) 
        self.timerDis.setStyleSheet("QLabel {border : 3px solid white;}")

        self.min = 60
        self.sec = 0
        self.startFlag = False
        self.startBut = QPushButton("-START-")
        self.startBut.clicked.connect(self.START)

        self.retBut = QPushButton("-RETRIEVE-")
        self.retBut.setEnabled(False)
        self.retBut.clicked.connect(self.RETRIEVE)
        self.timerTub = QTimer()
        self.timerTub.timeout.connect(self.showTime)

        self.TestMisc = QVBoxLayout()
        self.TestMisc.addWidget(self.timerDis)
        self.TestMisc.addWidget(self.startBut)
        self.TestMisc.addWidget(self.retBut)
        self.TestMiscW = QGroupBox()
        self.TestMiscW.setLayout(self.TestMisc)
        self.TestMiscW.setMaximumWidth(142)

        self.DropLay = QVBoxLayout()
        #self.DropLay.addWidget(self.DisplayDrop)
        self.DropLay.addWidget(self.EquiLab)
        self.DropLay.addWidget(self.resetBUT)
        self.DropBox = QGroupBox()
        self.DropBox.setLayout(self.DropLay)
        self.DropBox.setMaximumWidth(142)

        self.RetLab = QLabel("RETRIEVE FLASK:")
        self.RetLab.setFont(QFont('Times'))
        self.RetLab.setMaximumHeight(20)
        self.RetFlask = DragLabel(" HCl ", self)
        self.RetFlask.setPixmap(QPixmap("media/empty2.png"))

        self.RETFLAG = False

        self.RetLAY = QVBoxLayout()
        self.RetLAY.addWidget(self.RetLab)
        self.RetLAY.addWidget(self.RetFlask)
        self.RetLAYW = QGroupBox()
        self.RetLAYW.setLayout(self.RetLAY)
        self.RetLAYW.setMaximumWidth(170)

        self.SUB1 = QPushButton("Feed On-going\n reaction as\nTrial 1")
        self.SUB1.clicked.connect(self.SUBMIT1)
        self.SUB2 = QPushButton("Feed On-going\n reaction as\nTrial 2")
        self.SUB2.clicked.connect(self.SUBMIT2)
        
        self.retReset = QLabel("Please Do not reset\nbefore Feeding.\n\nUpload allowed \nonce per session")
        self.SUBFLAG1 = False
        self.SUBFLAG1 = False
        self.SUB1.setFont(QFont('Times', 10))
        self.SUB2.setFont(QFont('Times', 10))
        #self.SUB3.setFont(QFont('Times', 10))
        self.retReset.setFont(QFont('Times', 10))

        self.SUBLay = QVBoxLayout()
        self.SUBLay.addWidget(self.SUB1)
        self.SUBLay.addWidget(self.SUB2)
        #self.SUBLay.addWidget(self.SUB3)
        self.SUBLay.addWidget(self.retReset)

        self.SUBGro = QGroupBox()
        self.SUBGro.setLayout(self.SUBLay)
        self.SUBGro.setMaximumWidth(142)
        
        self.InstructLAB1 = QLabel("1.LEFT UPPER HALF\nIS SOLUTION RACK\n\n2.LEFT LOWER HALF\nIS FOR EQUM.\n\n3.RIGTH SECTION\nIS FOR TITRATION")
        #self.InstructLAB1.setAlignment(Qt.AlignCenter)
        
        self.Instruct = QGroupBox()
        self.InstructLay = QVBoxLayout()
        self.InstructLay.addWidget(self.InstructLAB1) 
        #self.InstructLay.addWidget()
        self.Instruct.setLayout(self.InstructLay)
        self.Instruct.setMaximumWidth(171)
        
        self.EquiLAY = QHBoxLayout()
        self.EquiLAY.addWidget(self.DropBox)
        self.EquiLAY.addWidget(self.TestMiscW)
        self.EquiLAY.addWidget(self.RetLAYW)
        self.EquiLAY.addWidget(self.SUBGro)
        self.EquiLAY.addWidget(self.Instruct)
        
        self.EquiLAYW = QWidget()
        self.EquiLAYW.setLayout(self.EquiLAY)
        
        self.TitDrop = DropLabel("Bur", self)
        self.TitDrop.textChanged.connect(self.update3)
        self.TitDrop.setMinimumHeight(320)
        self.TitDrop.setMaximumHeight(320)
        self.TitDrop.setReadOnly(True)
        self.TitDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/bur-min.png); background-repeat: no-repeat;background-position: 0% 0%;}")

        self.FlaDrop = DropLabel("Flask", self)
        self.FlaDrop.textChanged.connect(self.update2)
        self.FlaDrop.setMinimumHeight(250)
        self.FlaDrop.setMaximumHeight(250)
        self.FlaDrop.setReadOnly(True)
        self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskEm2.png); background-repeat: no-repeat;background-position: 0% 0%;}")

        self.movie = QSlider(Qt.Vertical)
        self.movie.setRange(-5000, 0)
        self.movie.setAutoFillBackground(True)
        self.movie.setValue(-5000)
        self.movie.setFocusPolicy(Qt.NoFocus)
        self.movie.setTickPosition(QSlider.TicksBothSides)
        self.movie.setTickInterval(1)
        self.movie.setEnabled(False)

        self.reset2 = QPushButton("Reset")
        self.reset2.clicked.connect(self.RESET2)
        
        self.DROP2 = QGridLayout()
        self.DROP2.addWidget(self.movie, 0, 0, 3, 1)
        self.DROP2.addWidget(self.TitDrop, 0, 1, 1, 1)
        self.DROP2.addWidget(self.FlaDrop, 1, 1, 1, 1)
        self.DROP2.addWidget(self.reset2, 2, 1, 1, 1)
        self.DROP2W = QGroupBox()
        self.DROP2W.setLayout(self.DROP2)

        self.DROP2W.setMaximumWidth(270)

        self.loadKI = QPushButton("Add Indicator")
        #self.loadKI.clicked.connect(self.changeFlask)
        self.loadNAOH = QPushButton("Load NaOH")
        self.loadNAOH.clicked.connect(self.LoadHypo)
        
        self.loadStart = QPushButton("START")
        self.loadStart.clicked.connect(self.START2)
        self.loadStop = QPushButton("PAUSE")
        self.loadStop.clicked.connect(self.Pause)
        self.loadRe = QPushButton("RESET")
        self.loadRe.clicked.connect(self.RESET2)

        self.volumeDisplay = QLabel("0.00")
        self.volumeDisplay.setFont(QFont('Times', 30))
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
        ############################################
        ############################################

        self.Side1 = QVBoxLayout()
        self.Side1.addWidget(self.SolsTab)
        self.Side1.addWidget(self.EquiLAYW)
        self.Side1W = QWidget()
        self.Side1W.setLayout(self.Side1)
        
        self.pageBox3 = QHBoxLayout()
        self.pageBox3.addWidget(self.Side1W)
        self.pageBox3.addWidget(self.MISCBOX)
        self.pageBox3.addWidget(self.DROP2W)
        
        self.tab23.setLayout(self.pageBox3)
        
        self.otherPages()
        self.UNKNOWNERROR = "-Unidentified-"
        
    def SUBMIT1(self):

        if(self.totVol != 0):
            global data1
            data1 = [self.aceCon*self.aceVol/self.totVol, self.ethCon*self.ethVol/self.totVol,
                     self.eacCon*self.eacVol/self.totVol, (self.aceCon*self.aceVol-self.FinX)/self.totVol,
                     (self.ethCon*self.ethVol-self.FinX)/self.totVol, (self.eacCon*self.eacVol+self.FinX)/self.totVol]

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
        
        if(self.totVol != 0):
            
            global data2
            data2 = [self.aceCon*self.aceVol/self.totVol, self.ethCon*self.ethVol/self.totVol,
                     self.eacCon*self.eacVol/self.totVol, (self.aceCon*self.aceVol-self.FinX)/self.totVol,
                     (self.ethCon*self.ethVol-self.FinX)/self.totVol, (self.eacCon*self.eacVol+self.FinX)/self.totVol]

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
            msg.setText("Total Volume zero")
            msg.setWindowTitle("Zero Volume")
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
                    #if(self.LoadedINFLASK == False):
                    self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskB2.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    self.LoadedINFLASK = True
                    self.volFlask = self.FlaDrop.vol()*self.FlaDrop.con()
                    self.conFlask += self.volFlask
                    #print(self.conFlask)
                       
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
                   		self.movie.setValue((self.burVol*100)-5000)
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
                    self.movie.setValue((self.burVol*100)-5000)
                    self.LOADMARK = (self.burVol*100)-5000
                    self.burFlag = True

                else:
                    self.errorFlag = 10
                    self.errorMessage()
            self.TitDrop.setText("Bur")
        except:
            self.UNKNOWNERROR = "Updating Burette parameters"
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
            self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskEm2.png); background-repeat: no-repeat;background-position: 0% 0%;}")

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
            #self.timerTrials.stop()
            speed = self.volumeSpeed.value()
            #self.volumeSpeedDis.setText(str(round((0.1+100-speed)/100, 2)))
            self.timerTrials.start(100-speed)
        except:
            self.UNKNOWNERROR = "Changing Titration Speed"
            self.errorMessage()

    def Pause(self):
        try:
            if(self.loadStop.text() == "PAUSE"):
                self.timerTrials.stop()
                self.loadStop.setText("RESUME")

            else :
                self.timerTrials.start(100-self.volumeSpeed.value())
                self.loadStop.setText("PAUSE")
        except:
            self.UNKNOWNERROR = "Starting/Pausing the titration"
            self.errorMessage()
            
    def LoadHypo(self):
        try:
            self.marker = 0
            self.movie.setValue(self.LOADMARK)
            #self.loadNAOH.setEnabled(False)
            if(self.resumeFlag):
                self.resumeFlag = False
        except:
            self.UNKNOWNERROR = "Refilling Burette"
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
                    self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskE2.png); background-repeat: no-repeat;background-position: 0% 0%;}")

                elif(self.volumeDown <= -20 and self.volumeDown >= -25):
                    self.FlaDrop.setStyleSheet("QLineEdit {color: black; background-image : url(media/flaskC2.png); background-repeat: no-repeat;background-position: 0% 0%;}")

            if self.start:
                #text = (self.volumeDown/100)
                self.movie.setValue(self.LOADMARK-self.marker)
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
            self.UNKNOWNERROR = "Starting/Stoping Timer"
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
                        self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l1test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    elif(self.dropCount == 2):
                        self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l2test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    elif(self.dropCount == 3):
                        self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l3test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
                    elif(self.dropCount == 4):
                        self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/l4test.png); background-repeat: no-repeat;background-position: 0% 0%;}")
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
        
    def RESET(self):
        try:
            self.dropCount = 0
            self.RESETDROP(self.EquiLab, "EquiLab")
            self.EquiLab.setStyleSheet("QLineEdit {color: none; background-image : url(media/emptytest.png); background-repeat: no-repeat;background-position: 0% 0%;}")
            self.HclLoad = False
            self.ethLoad = False
            self.AceLoad = False
            self.eacLoad = False
            self.extra = False
            self.sec = 0
            self.min = 60
            self.startFlag = False
            self.timerTub.stop()
            self.timerDis.setText("60:00")
            self.HclCon = 0
            self.HclVol = 0
            self.ethCon = 0
            self.ethVol = 0
            self.aceCon = 0
            self.aceVol = 0
            self.totVol = 0
            self.eacCon = 0
            self.eacVol = 0
            self.retBut.setEnabled(False)
            self.FinX = 0
            self.RESETDROP(self.RetFlask, "flask")
            self.RetFlask.setPixmap(QPixmap("media/empty2.png"))
            self.time = 3600
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

        self.RetFlask.setPixmap(QPixmap("media/fill2.png"))
    
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
        
    def play3(self):
        
        fileName = FOLDER+"/media/exp3.mp4"
        if self.loaded3 == 0:
            self.mediaPlayer3.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton3.setEnabled(True)
            self.playButton3.setText("Pause")
            self.loaded3 = 1
            
        if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
            self.playButton3.setText("Play")
            self.mediaPlayer3.pause()
        else:
            self.mediaPlayer3.play()
            self.playButton3.setText("Pause")
 
    def mediaStateChanged3(self, state):
        if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
            self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged3(self, position):
        self.positionSlider3.setValue(position)
 
    def durationChanged3(self, duration):
        self.positionSlider3.setRange(0, duration)
 
    def setPosition3(self, position):
        self.mediaPlayer3.setPosition(position)
 
    def handleError3(self):
        self.playButton3.setEnabled(False)
        self.errorLabel3.setText("Error: " + self.mediaPlayer3.errorString())
        
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
            text = "ATTENTION !! Reaction in Flask has reached equilibrium. You May retrieve your solution."
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
            temp = QLabel(names[i])
            temp.setFont(QFont('Times', 12))
            self.SolsTab.setCellWidget(0, i, temp)
            self.SolsTab.cellWidget(0, i).setAlignment(Qt.AlignCenter)
            
            if(i):
                self.SolsTab.setCellWidget(3, i, DragLabel(names[i], self))
                self.SolsTab.cellWidget(3, i).setPixmap(QPixmap("media/light2.png"))
                self.SolsTab.cellWidget(3, i).setAlignment(Qt.AlignCenter)
                self.SolsTab.setCellWidget(4, i, QDoubleSpinBox())
                self.SolsTab.cellWidget(4, i).valueChanged.connect(self.VolEntry)
                temp2 = QLabel()
                temp2.setFont(QFont('Times', 10))
                self.SolsTab.setCellWidget(1, i, temp2)
                self.SolsTab.setCellWidget(2, i, QDoubleSpinBox())
                self.SolsTab.cellWidget(1, i).setAlignment(Qt.AlignCenter)
                self.SolsTab.cellWidget(2, i).setReadOnly(True)
            else:
                self.SolsTab.setCellWidget(1, i, QLabel("Conc->"))
                self.SolsTab.setCellWidget(2, i, QLabel("Vol->"))
                self.SolsTab.setCellWidget(3, i, QLabel("Flask->"))
                self.SolsTab.setCellWidget(4, i, QLabel("Vol Taken->"))
                
        
        self.SolsTab.cellWidget(3, 1).setCon(3+(random.randint(-99, 99)/100))
        global hcl
        hcl = self.SolsTab.cellWidget(3, 1).con()
        self.SolsTab.cellWidget(1, 1).setText("~3N")
        self.SolsTab.cellWidget(3, 1).setCol(1)
        self.SolsTab.cellWidget(2, 1).setValue(15)

        

        self.SolsTab.cellWidget(3, 2).setCon(1+(random.randint(-99, 99)/100))
        global naoh
        naoh = self.SolsTab.cellWidget(3, 2).con()
        self.SolsTab.cellWidget(1, 2).setText("~1N")
        
        self.SolsTab.cellWidget(2, 2).setValue(50)

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
        self.SolsTab.cellWidget(3, 5).setCol(1)

        self.SolsTab.cellWidget(3, 6).setCon(10.2)
        self.SolsTab.cellWidget(1, 6).setText("~10.2M")
        self.SolsTab.cellWidget(2, 6).setValue(10)

        self.SolsTab.cellWidget(3, 7).setCon(4.1)
        self.SolsTab.cellWidget(1, 7).setText("~4.1M")
        self.SolsTab.cellWidget(2, 7).setValue(4)
        
        for i in range(5):
            self.SolsTab.cellWidget(i, 0).setAlignment(Qt.AlignCenter)

        self.SolsTab.cellWidget(3, 7).setPixmap(QPixmap("media/pink2.png"))
        header = self.SolsTab.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.SolsTab.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        #self.SolsTab.setMaximumHeight(280)
        #self.SolsTab.setMinimumHeight(305)
        #self.SolsTab.setMaximumWidth(310)
        #self.SolsTab.setMinimumWidth(310)

        ver = self.SolsTab.horizontalHeader()
        ver.setVisible(False)
        ver2 = self.SolsTab.verticalHeader()
        ver2.setVisible(False)
    def setUPTITBOX(self):
        
        self.ButtonBox = QGroupBox()
        self.ButtonBox.setMaximumWidth(170)
        self.buttonLay = QVBoxLayout()

        
        for i in [self.loadNAOH, self.loadStart, self.loadStop, self.loadRe]:
            self.buttonLay.addWidget(i)

        self.ButtonBox.setLayout(self.buttonLay)

        self.SPEEDLAB = QLabel("-SPEED-")
        self.SPEEDLAB.setMaximumHeight(30)
        self.SPEEDLAB.setAlignment(Qt.AlignCenter)
        self.SPEEDLay = QVBoxLayout()
        self.SPEEDBOX = QGroupBox()
        #self.SPEEDLay.addWidget(self.volumeSpeedDis)
        self.SPEEDLay.addWidget(self.volumeSpeed)
        self.SPEEDLay.addWidget(self.SPEEDLAB)
        self.SPEEDBOX.setLayout(self.SPEEDLay)
            
        for i, j in zip([self.loadNAOH, self.loadStop, self.volumeSpeedDis],
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
        
    def otherPages(self):
        self.l13 = QLabel()
        self.l13.setPixmap(QPixmap("media/equi-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l13.setAlignment(Qt.AlignCenter)
        
        self.l23 = QLabel()
        self.l23.setPixmap(QPixmap("media/equi-2.jpg"))
        self.l23.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l23.setAlignment(Qt.AlignCenter)

        
        self.tab1Lay3 = QVBoxLayout()
        self.tab1Lay3.addWidget(self.l13)
        self.tab1Lay3.addWidget(self.l23)


        self.scrollWidget3 = QWidget()
        self.scrollWidget3.setLayout(self.tab1Lay3)
        
        self.scrollAr3 = QScrollArea()
        self.scrollAr3.setWidget(self.scrollWidget3)
        
        self.tab1Lay23 = QVBoxLayout()
        self.tab1Lay23.addWidget(self.scrollAr3)
        
        self.tab13.setLayout(self.tab1Lay23)
        #print("tab1 done")        

        self.tab3text3 = QPlainTextEdit()
        self.tab4text3 = QPlainTextEdit()

        self.mediaPlayer3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton3 = QPushButton()
        self.playButton3.setText("Play")
        self.playButton3.setEnabled(True) #default is on False, will not play video
        #self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
        self.playButton3.clicked.connect(self.play3)  #when clicked, should play
 
        self.positionSlider3 = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider3.setRange(0, 0) #setting the range of the slider
        self.positionSlider3.sliderMoved.connect(self.setPosition3)
 
        self.errorLabel3 = QLabel()
        self.errorLabel3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
        # Create a widget for window contents
 
        # Create layouts to place inside widget
        self.videoWidget3 = QVideoWidget()
        self.controlLayout3 = QHBoxLayout()
        self.controlLayout3.setContentsMargins(0, 0, 0, 0)
        self.controlLayout3.addWidget(self.playButton3)
        self.controlLayout3.addWidget(self.positionSlider3)
 
        self.layout3 = QVBoxLayout()
        self.layout3.addWidget(self.videoWidget3)
        self.layout3.addLayout(self.controlLayout3)
        self.layout3.addWidget(self.errorLabel3)
 
        # Set widget to contain window contents
        self.Video_widget3 = QWidget()
        self.Video_widget3.setLayout(self.layout3)
 
        self.mediaPlayer3.setVideoOutput(self.videoWidget3)
        self.mediaPlayer3.stateChanged.connect(self.mediaStateChanged3)
        self.mediaPlayer3.positionChanged.connect(self.positionChanged3)
        self.mediaPlayer3.durationChanged.connect(self.durationChanged3)
        self.mediaPlayer3.error.connect(self.handleError3)
        self.loaded3 = 0

        self.tab3Lay3 = QVBoxLayout()
        self.tab3Lay3.addWidget(self.Video_widget3)
        self.tab33.setLayout(self.tab3Lay3)
        
        self.tab4Lay3 = QVBoxLayout()
        self.tab4Lay3.addWidget(self.tab4text3)
        
        self.tab43.setLayout(self.tab4Lay3)
        
def main_exp3(remark, sheet):
    global userID
    userID = remark
    global sheetID
    sheetID = sheet
    #print("here")
    obj = Exp3_class()
    return obj

def getUnknowns():
    data = []
    data.append(hcl)
    data.append(naoh)
    global data1
    for i in data1:
        data.append(round(i, 3))
    #data1 = []
    global data2
    for i in data2:
        data.append(round(i, 3))
    
    return data
