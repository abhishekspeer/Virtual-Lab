from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

ace = 0
hcl =0
iod = 0

class MimeData(QMimeData):
    data1 = 0
    data2 = "name"
    data3 = 0
    def __init__(self):
        super().__init__()
        
class DragLabel(QLabel):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.flask_ = 0
        self.name_ = label
        self.value_ = 0.01

    def setValue(self, data):
        self.value_ = data
    def setName(self, name):
        self.name_ = name
    def setFlask(self, flask):
        self.flask_ = flask

    def name(self):
        return self.name_
    def flask(self):
        return self.flask_
    def value(self):
        return self.value_
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
 
    def mouseMoveEvent(self, event):
        if not(event.buttons() & Qt.LeftButton):
            return
        else:
            drag = QDrag(self)
            mimedata = MimeData()
            mimedata.data1 = self.value()
            mimedata.data2 = self.name()
            mimedata.data3 = self.flask()
            drag.setMimeData(mimedata)
            pixmap = QPixmap(self.size()) #
            
 
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
 
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)
 
class DropLabel(QLineEdit):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.setAcceptDrops(True)
        self.value_ = 0
        self.name_ = "name"
        self.loaded_ = False
        self.flask_ = 0

    def setValue(self, value):
        self.value_ = value

    def setName(self, name):
        self.name_ = name

    def setFlask(self, flask):
        self.flask_ = flask

    def setLoaded(self, Bool):
        self.loaded_ = Bool
        
    def value(self):
        return self.value_

    def name(self):
        return self.name_

    def flask(self):
        return self.flask_

    def loaded(self):
        return self.loaded_
        
    def dragEnterEvent(self, event):
        event.acceptProposedAction()
 
    def dropEvent(self, event):
        if(self.loaded() == False):
            pos = event.pos()
            self.setValue(event.mimeData().data1)
            self.setName(event.mimeData().data2)
            self.setFlask(event.mimeData().data3)
            self.setText(str(self.name()))
            
        else:
            self.setText("error")
        event.acceptProposedAction()
        
class Exp2_class(QTabWidget):
    
    def __init__(self):
        super().__init__()
        #self.Tabs4 = QTabWidget()
        self.tab14 = QWidget()
        self.tab24 = QWidget()
        self.tab34 = QWidget()
        self.tab44 = QWidget()
        self.addTab(self.tab14," Theory ")
        self.addTab(self.tab24," Perform ")
        self.addTab(self.tab34, " Video ")
        self.addTab(self.tab44, " Question Bank ")
        self.setFont(QFont('Times', 12))
        
        #self.Label1 = QLabel("STOCK")

        self.stockSol_val = QTableWidget(1, 6)
        ver = self.stockSol_val.horizontalHeader()
        ver.setVisible(False)
        ver = self.stockSol_val.verticalHeader()
        ver.setVisible(False)
        for i, j in zip([0, 1, 2], [" Acetone : ", "HCl :", " Iodine : "]):
            self.stockSol_val.setCellWidget(0, i*2, QLabel(j))
            self.stockSol_val.cellWidget(0, i*2).setAlignment(Qt.AlignCenter)
            self.stockSol_val.setCellWidget(0, (i*2)+1, QLineEdit())
            self.stockSol_val.cellWidget(0, (i*2)+1).setText("0.00")
            self.stockSol_val.cellWidget(0, (i*2)+1).setMaximumWidth(50)
            self.stockSol_val.cellWidget(0, (i*2)+1).editingFinished.connect(self.validateStock)
            
        self.stockSol_val.setMaximumWidth(310)
        self.stockSol_val.setMinimumWidth(310)
        self.stockSol_val.setMaximumHeight(50)
        self.stockSol_val.setMinimumHeight(50)
        
        header = self.stockSol_val.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.stockSol_val.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        self.Label2 = QLabel("A) IODINE FLASKS(10ml)")
        
        self.IodineTable = QTableWidget(3, 4)
        ver = self.IodineTable.horizontalHeader()
        ver.setVisible(False)
        ver2 = self.IodineTable.verticalHeader()
        ver2.setVisible(False)
        

        for i in [0, 1, 2, 3]:

            self.IodineTable.setCellWidget(0, i, DragLabel("Iodine-"+str(i+1), self))
            self.IodineTable.cellWidget(0, i).setAlignment(Qt.AlignCenter)
            self.IodineTable.cellWidget(0, i).setPixmap(QPixmap("media/emptyflask.jpg"))
            self.IodineTable.setCellWidget(1, i, QDoubleSpinBox())
            self.IodineTable.setCellWidget(2, i, QPushButton("Get"))
            self.IodineTable.cellWidget(2,i).clicked.connect(self.cal_Iodine)
            

        self.IodineTable.setMaximumHeight(195)
        self.IodineTable.setMinimumHeight(195)
        self.IodineTable.setMaximumWidth(310)
        self.IodineTable.setMinimumWidth(310)
        
        header = self.IodineTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.IodineTable.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.Label4 = QLabel("B) TRIAL FLASKS(10ml)")
        self.SolsTab = QTableWidget(7, 4)

        for k in [0, 1, 2, 3]:
            
            self.SolsTab.setCellWidget(6, k, QPushButton("GET Trial-"+str(k+1)))
            #self.SolsTab.cellWidget(6, k).setAlignment(Qt.AlignCenter)
            self.SolsTab.setCellWidget(5, k, DragLabel("Trial-"+str(k+1), self))
            self.SolsTab.cellWidget(5, k).setAlignment(Qt.AlignCenter)
            self.SolsTab.cellWidget(5, k).setFlask(k+1)
            self.SolsTab.cellWidget(5, k).setPixmap(QPixmap("media/emptyflask.jpg"))
            
            self.SolsTab.cellWidget(6, k).clicked.connect(self.cal_Trial)

        
        header = self.SolsTab.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.SolsTab.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        self.SolsTab.setMaximumHeight(305)
        self.SolsTab.setMinimumHeight(305)
        self.SolsTab.setMaximumWidth(310)
        self.SolsTab.setMinimumWidth(310)

        ver = self.SolsTab.horizontalHeader()
        ver.setVisible(False)
        ver2 = self.SolsTab.verticalHeader()
        ver2.setVisible(False)
            
        self.SolsTab.setCellWidget(0, 1, QLabel("Acetone"))
        self.SolsTab.setCellWidget(0, 2, QLabel("HCl"))
        self.SolsTab.setCellWidget(0, 3, QLabel("Iodine"))

        for i in [1, 2, 3]:
            self.SolsTab.cellWidget(0, i).setAlignment(Qt.AlignCenter)
            
        for i in range(1, 5):
            self.SolsTab.setCellWidget(i, 0, QLabel("  Trial-"+str(i)+"  "))
            self.SolsTab.cellWidget(i, 0).setAlignment(Qt.AlignCenter)
            
        for i in [1, 2, 3, 4]:
            for j in [1, 2, 3]:
                self.SolsTab.setCellWidget(i, j, QDoubleSpinBox())

        self.wid_2lay = QVBoxLayout()
        for i in [self.stockSol_val, self.Label2, self.IodineTable, self.Label4,
                  self.SolsTab]:
              self.wid_2lay.addWidget(i)

        self.wid_2 = QWidget()
        self.wid_2.setLayout(self.wid_2lay)

        self.meterLabel = DropLabel("Drop_here", self)
        self.meterLabel.textChanged.connect(self.update)
        self.meterLabel.setReadOnly(True)
        self.meterLabel.setStyleSheet("QLineEdit {color: none; background-image : url(media/photometer_open.jpg); background-repeat: no-repeat;background-position: 0% 0%;}") 
        self.meterLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.absorb = QLineEdit()
        self.absorb.setEnabled(False)
        self.absorb.setFont(QFont('Times', 20))
        self.absorb.setStyleSheet("QLineEdit {color : white; border : 3px solid white;}")
        self.absorb.setMinimumHeight(100)
        self.absorb.setMaximumWidth(150)
        self.absorb.setText("-E-")
        self.absorb.setAlignment(Qt.AlignCenter)

        self.absorbLab = QLabel("-ASORBANCE-\n(in fraction)")
        self.absorbLab.setAlignment(Qt.AlignCenter)
        
        self.loadBut = QPushButton("-LOAD-")
        self.loadBut.setEnabled(False)
        self.loadBut.clicked.connect(self.loading)
        self.resetBut = QPushButton("-RESET-")
        self.resetBut.clicked.connect(self.reset)
        self.startBut = QPushButton("-START-")
        self.startBut.setEnabled(False)
        self.startBut.clicked.connect(self.starting)

        self.otherMisc()

        self.sideBelowLay = QHBoxLayout()
        self.sideLay2 = QVBoxLayout()
        self.sideBelowWid = QWidget()
        
        for i in [self.waveBox, self.miscWid, self.InfoLabelGroup]:
            self.sideBelowLay.addWidget(i)
            
        self.sideBelowWid.setLayout(self.sideBelowLay)
        self.sideBelowWid.setMaximumHeight(250)
        
        for j in [self.meterLabel, self.sideBelowWid]:
            self.sideLay2.addWidget(j)

        self.sideWid2 = QGroupBox()
        self.sideWid2.setLayout(self.sideLay2)
        

        self.Page4lay = QHBoxLayout()
        self.Page4lay.addWidget(self.wid_2)
        self.Page4lay.addWidget(self.sideWid2)

        self.tab24.setLayout(self.Page4lay)
        self.otherPages()
        
        self.errorFlag = 0
        self.count = 0
        self.timerIodine = QTimer()
        self.timerIodine.timeout.connect(self.showTime)
        self.start = False
        self.timerIodine.start(100)
        self.valueToDisplay = 0

        self.loadedFlag = False
        
        self.loaded = False

        self.flasks_count = [0, 0, 0, 0]
        self.flasks_count_red = [0, 0, 0, 0]
        self.timerTrials = QTimer()
        self.timerTrials.timeout.connect(self.hiddenTimer)
        self.timerTrials.start(50)
        #print("Tab created")
        #return self.Tabs4

    def update(self):
        if(self.meterLabel.text() == ""):
            return
        
        if(self.meterLabel.text() == "-1"):
            self.reset()
            return
        
        if(self.meterLabel.loaded() == True  or self.meterLabel.text() == "error"):
            self.errorFlag = 4
            self.errorMessage()
            self.meterLabel.setText("")
            return
        
        try :
            val = float(self.meterLabel.value())
        except:
            return
        
        self.displayLoad.setText(str(self.meterLabel.name()))
        self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-\nPress LOAD")
        self.loadBut.setEnabled(True)
        self.loadedFlag = True

    def loading(self):
        if(self.loadedFlag):
            if(self.meterLabel.loaded() == False):
                self.meterLabel.setStyleSheet("QLineEdit {color: white; background-image : url(media/photometer.jpg); background-repeat: no-repeat;background-position: 0% 0%;}")
                self.InfoLabel.setText("//LOADED//\n\n-LID CLOSE-\nPress START")
                self.loadBut.setText("-UNLOAD-")
                self.startBut.setEnabled(True)
                self.meterLabel.setLoaded(True)
                #if(self.meterLabel.flask() == 0):
                #self.timerIodine.start(100)
                return

            elif(self.meterLabel.loaded() == True):
                self.loadBut.setText("-LOAD-")
                self.meterLabel.setStyleSheet("QLineEdit {color: white; background-image : url(media/photometer_open.jpg); background-repeat: no-repeat;background-position: 0% 0%;}")
                self.absorb.setText("-E-")
                self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-\n(Drag and Drop)")
                self.displayLoad.setText("-NONE-")
                self.loadBut.setEnabled(False)
                self.valueToDisplay = 0
                self.meterLabel.setText("")
                self.meterLabel.setName("name")
                #if(self.meterLabel.flask() == 0):
                #self.timerIodine.stop()
                self.meterLabel.setValue(0.0)
                self.meterLabel.setLoaded(False)
                self.loadedFlag = False
                return
        else:
            self.errorFlag = 7
            self.errorMessage()
            
    def starting(self):
        try:
            if(self.startBut.text() == "-STOP-"):
                self.start = False
                self.InfoLabel.setText("Stopped!\nYou can unload\nPress UNLOAD")
                self.loadBut.setEnabled(True)
                self.count = 0
                self.startBut.setText("-START-")
                
                return
                
            elif(self.startBut.text() == "-START-"):
                if(self.meterLabel.loaded() == True):
                    if(self.wave.value() != 565):
                        self.errorFlag = 3
                        self.errorMessage()
                        return
                    
                    self.count = 6
                    self.start =  True
                    self.loadBut.setEnabled(False)
                    self.startBut.setText("-STOP-")
            else:
                self.errorFlag = 2
                self.errorMessage()
                return
        except:
            self.errorFlag = 2
            self.errorMessage()
            return
        
    def showTime(self):
        if(self.start):
            self.count -= 1
            if self.count <= 0:
                self.start = False
                
                self.InfoLabel.setText("WARMING UP\nCOMPLETE !\n_")
                if(self.meterLabel.flask() == 0):
                    self.absorb.setText(str(self.meterLabel.value()))
                else:
                    self.absorb.setText(str(self.valueToDisplay))
                
        if(self.start):
            if(self.count == 5):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n.   ")
                
            if(self.count %16 == 4):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n..  ")
                
            if(self.count %16 == 3):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n... ")
                
            if(self.count %16 == 2):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n....")
                
            if(self.count %16 == 1):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n.....")

        elif(self.meterLabel.flask() != 0 and self.meterLabel.loaded() == True and self.startBut.text() == "-STOP-"):
            self.absorb.setText(str(self.valueToDisplay))
        else:
            self.startBut.setText("-START-")
            self.loadBut.setEnabled(True)

    def cal_Iodine(self):
        column = self.IodineTable.currentColumn()
        try:
            val_wid = self.stockSol_val.cellWidget(0,5)
            st = float(val_wid.text())
        except:
            self.errorFlag = 1
            self.errorMessage()
            return
        row = 1
        val_wid = self.IodineTable.cellWidget(row,column)
        val = val_wid.value()
        if(val == 0 or val >= 10):
            self.errorFlag = -1
            self.errorMessage()
            return
        elif(st == 0):
            self.errorFlag = 1
            self.errorMessage()
            return
        else:
            absorbance = round(val/10 + (((float(random.randint(-500, 500)))/10000)*val), 3)
            if(absorbance > 1):
                absorbance = 1
            elif(absorbance< 0):
                absorbance = 0  
            flask = self.IodineTable.cellWidget(row-1,column)
            flask.setPixmap(QPixmap("media/iodine.jpg"))
            flask.setValue(absorbance)

    def cal_Trial(self):
        K = 3.756
        row = self.SolsTab.currentColumn()+1
        self.mode = True
        if(self.validateStock()):
            
            ace_wid = self.SolsTab.cellWidget(row,1)
            ace = (float(self.stockSol_val.cellWidget(0,1).text())*(ace_wid.value()))/10
            if(ace == 0 or ace > 10):
                self.errorFlag = -2
                self.errorMessage()
                return
                
            hcl_wid = self.SolsTab.cellWidget(row,2)
            hcl = (float(self.stockSol_val.cellWidget(0,3).text())*(hcl_wid.value()))/10
            if(hcl == 0 or hcl > 10):
                self.errorFlag = -3
                self.errorMessage()
                return
            
            iod_wid = self.SolsTab.cellWidget(row,3)
            iod = (float(self.stockSol_val.cellWidget(0,5).text())*(iod_wid.value()))/10
            if(iod == 0 or iod > 10):
                self.errorFlag = -4
                self.errorMessage()
                return
            if(iod + ace + hcl > 10):
                self.errorFlag = 5
                self.errorMessage()
                return

            
            rate = K*ace*hcl
            time = (iod*100000)/rate
            flask = self.SolsTab.cellWidget(5,row-1)
            flask.setPixmap(QPixmap("media/iodine.jpg"))
            self.flasks_count[row-1] = int(time)
            self.flasks_count_red[row-1] = int(time)
            self.startTrials = True
            self.errorFlag = 6
            self.errorMessage()
            
    def hiddenTimer(self):
        try:
            setted = 0
            if(self.startTrials):
                for i in [1, 2, 3, 4] :
                    #print(self.flasks_count_red)
                    if(self.flasks_count[i-1] > 0):
                        if(self.flasks_count_red[i-1]>0):
                            self.flasks_count_red[i-1] = self.flasks_count_red[i-1]-1
                            if(i == self.meterLabel.flask()):
                                setted = 1
                                value = self.flasks_count_red[i-1]/self.flasks_count[i-1]
                                value = value
                                self.valueToDisplay = round(value, 3)     
                            
            if(setted == 0):
                self.valueToDisplay = 0.01
                
        except:
            pass

    #def hiddenTimer1(self):
        
    def validateStock(self):

        try:
            if(self.mode == True):
                self.mode = False
                ace_wid = float(self.stockSol_val.cellWidget(0,1).text())
                hcl_wid = float(self.stockSol_val.cellWidget(0,3).text())
                iod_wid = float(self.stockSol_val.cellWidget(0,5).text())

                if(ace_wid == 0 or hcl_wid == 0 or iod_wid == 0):
                    self.errorFlag = 1
                    self.errorMessage()
                    return False
                else:
                    global ace
                    ace = ace_wid
                    global hcl
                    hcl = hcl_wid
                    global iod
                    iod = iod_wid
                    return True
            else:
                col = self.stockSol_val.currentColumn()
                val_wid = self.stockSol_val.cellWidget(0,col)
                try:
                    val = float(val_wid.text())
                    if(val <= 0):
                        self.errorFlag = 1
                        self.errorMessage()
                        return False
                    else:
                        return True
                except:
                    self.errorFlag = 1
                    self.errorMessage()
                    return False
            
        except:
            self.errorFlag = 1
            self.errorMessage()
            return False
        
    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        title = "UNKNOWN ERROR"
        text = "Unidentified error. Report a Bug?"
        textMain ="UNKNOWN ERROR !"
        if(self.errorFlag == 1):
            text = "Stock Solution entered is Invalid!"
            textMain ="Calibration Error!"
        elif(self.errorFlag == 2):
            title  = "Configuration error"
            text = "Error in configuration of instrument. Try reset or relaunching."
            textMain ="Instrument Error!"
        elif(self.errorFlag == -1):
            title  = "Volume Error"
            text = "Zero/out of bound Volume entered. Please Specify the correct volume taken."
            textMain ="ZERO/MAX VOLUME !"
            
        elif(self.errorFlag < -1):
            title  = "Volume Error"
            text = "Out of Bound volume entered (0ml or >= 10 ml).Please Specify the volume taken."
            textMain ="VOLUME ERROR!"
            
        elif(self.errorFlag == 3):
            title = "Wavelength error"
            text = "Reset Wavelenght Appropriate for Iodine Calibration."
            textMain ="Wrong Wavelength"
        elif(self.errorFlag == 4):
            text = "Sample Already Loaded. Unload the sample first."
            textMain = "Error !"
        elif(self.errorFlag == 5):
            text = "Exceeding Flask volume (10 ml is limit). Fill volume appropriately"
            textMain = "Overflow !"
        elif(self.errorFlag == 6):
            text = "ATTENTION !! Reaction in Flask will now start. Please keep your Timer handy."
            title = "ATTENTION !"
            textMain = "REACTION START"
        elif(self.errorFlag == 7):
            text = "ATTENTION !! Nothing is Loaded. Drag and drop a Flask."
            title = "ATTENTION !"
            textMain = "EMPTY PHOTOMETER"

        if(self.errorFlag > 5):
            self.w.setIcon(QMessageBox.Information)
        else:
            self.w.setIcon(QMessageBox.Critical)
        self.w.setText(textMain)
        self.w.setInformativeText(text)
        self.w.setWindowTitle(title)
        self.w.exec()
        self.errorFlag = 0
        
    def reset(self):
        self.meterLabel.setValue(0)
        self.meterLabel.setFlask(0)
        self.meterLabel.setName("name")
        self.meterLabel.setLoaded(False)
        self.startBut.setEnabled(False)
        self.loadedFlag = False
        self.startTrials = False
        self.loaded = False
        self.start = False
        self.flasks_count = [0, 0, 0, 0]
        self.flasks_count_red = [0, 0, 0, 0]

        self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-\n(Drag and Drop)")
        self.displayLoad.setText("-NONE-")
        self.loadBut.setEnabled(False)
        self.loadBut.setText("-LOAD-")
        self.valueToDisplay = 0
        self.absorb.setText("-E-")
        self.meterLabel.setText("")
        self.meterLabel.setName("name")
                #if(self.meterLabel.flask() == 0):
        #self.timerIodine.stop()
        #self.meterLabel.setValue(0.0)
        #self.meterLabel.setLoaded(False)
                #self.loadedFlag = False
        for i in [0, 1, 2, 3]:
            flask = self.SolsTab.cellWidget(5,i)
            flask.setValue(0)
            flask.setPixmap(QPixmap("media/emptyflask.jpg"))
            self.IodineTable.cellWidget(0, i).setPixmap(QPixmap("media/emptyflask.jpg"))
            self.IodineTable.cellWidget(0, i).setValue(0)

    def play4(self):
        
        fileName = "media/exp2.mp4"
        if self.loaded4 == 0:
            self.mediaPlayer4.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton4.setEnabled(True)
            self.playButton4.setText("Pause")
            self.loaded4 = 1
            
        if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer4.pause()
            self.playButton4.setText("Play")
        else:
            self.mediaPlayer4.play()
            self.playButton4.setText("Pause")
 
    def mediaStateChanged4(self, state):
        if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
            self.playButton4.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton4.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged4(self, position):
        self.positionSlider4.setValue(position)
 
    def durationChanged4(self, duration):
        self.positionSlider4.setRange(0, duration)
 
    def setPosition4(self, position):
        self.mediaPlayer4.setPosition(position)
 
    def handleError4(self):
        self.playButton4.setEnabled(False)
        self.errorLabel4.setText("Error: " + self.mediaPlayer4.errorString())

    def changedWave(self):
        self.waveLCD.display(self.wave.value())

    def changedTemp(self):
        self.tempLcd.display(self.temp.value())

    def otherMisc(self):
        self.loLay = QVBoxLayout()
        self.loLay.addWidget(self.startBut)
        self.loLay.addWidget(self.loadBut)
        self.loLay.addWidget(self.resetBut)

        self.loWid = QWidget()
        self.loWid.setLayout(self.loLay)
        self.loWid.setMaximumWidth(100)

        self.HbTemp = QHBoxLayout()
        self.HbTemp.addWidget(self.absorb)
        self.HbTemp.addWidget(self.loWid)

        self.HbWid = QWidget()
        self.HbWid.setLayout(self.HbTemp)

        for i in [self.absorbLab, self.loadBut, self.resetBut, self.startBut]:
            i.setFont(QFont('Times', 12))
        
        self.waveLay = QVBoxLayout()
        self.waveLay.addWidget(self.absorbLab)
        self.waveLay.addWidget(self.HbWid)
        self.waveBox = QGroupBox()
        self.waveBox.setLayout(self.waveLay)

        self.wave = QDial()
        self.wave.setRange(200, 700)
        self.wave.setValue(250)
        self.wave.setNotchesVisible(False)
        self.wave.valueChanged.connect(self.changedWave)

        self.waveLab = QLabel("-WAVELENGTH-\n(in nm)")
        self.waveLab.setAlignment(Qt.AlignCenter)
        
        self.waveLCD = QLCDNumber()
        self.waveLCD.display(250)

        self.tempBox1Lay = QVBoxLayout()
        self.tempBox1Lay.addWidget(self.waveLab)
        self.tempBox1Lay.addWidget(self.waveLCD)
        self.tempBox1 = QWidget()
        self.tempBox1.setLayout(self.tempBox1Lay)

        self.tempBox2Lay = QHBoxLayout()
        self.tempBox2Lay.addWidget(self.wave)
        self.tempBox2Lay.addWidget(self.tempBox1)
        self.tempBox2 = QWidget()
        self.tempBox2.setLayout(self.tempBox2Lay)

        self.tempLcd = QLCDNumber()
        self.tempLcd.setMaximumWidth(70)
        self.tempLab = QLabel("-TEMPERATURE-\n(in Degree C)")
        self.tempLab.setAlignment(Qt.AlignCenter)
        self.tempLcd.display(25)

        self.temp = QDial()
        self.temp.setRange(10, 100)
        self.temp.setValue(25)
        self.temp.setNotchesVisible(True)
        self.temp.valueChanged.connect(self.changedTemp)

        self.tempBox3Lay = QVBoxLayout()
        self.tempBox3Lay.addWidget(self.tempLab)
        self.tempBox3Lay.addWidget(self.tempLcd)
        self.tempBox3 = QWidget()
        self.tempBox3.setLayout(self.tempBox3Lay)

        self.tempBox4Lay=QHBoxLayout()
        self.tempBox4Lay.addWidget(self.temp)
        self.tempBox4Lay.addWidget(self.tempBox3)
        self.tempBox4 = QWidget()
        self.tempBox4.setLayout(self.tempBox4Lay)

        self.miscLay = QFormLayout()
        self.miscLay.addRow(self.tempBox2)
        self.miscLay.addRow(self.tempBox4)
        
        self.miscWid = QGroupBox()
        self.miscWid.setLayout(self.miscLay)

        self.displayLoad = QLineEdit()
        self.displayLoad.setText("--NONE--")
        self.displayLoad.setReadOnly(True)

        self.label456 = QLabel("COM_DASH:")
        self.label456.setAlignment(Qt.AlignCenter)
        self.InfoLabel = QLabel("//UNLOADED//\n\n-LID OPEN-")
        self.InfoLabel.setMinimumWidth(200)
        self.InfoLabel.setMaximumWidth(200)
        self.InfoLabel.setMinimumHeight(150)
        self.InfoLabel.setAlignment(Qt.AlignCenter)
        self.InfoLabel.setFont(QFont('Times', 12)) 
        self.InfoLabel.setStyleSheet("QLabel {border : 3px solid black;}")

        self.InfoLay = QVBoxLayout()
        self.InfoLay.addWidget(self.label456)
        self.InfoLay.addWidget(self.displayLoad)
        self.InfoLay.addWidget(self.InfoLabel)
        self.InfoLabelGroup = QGroupBox()
        self.InfoLabelGroup.setLayout(self.InfoLay)
        
        
    def otherPages(self):
        self.mediaPlayer4 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton4 = QPushButton("Play")
        self.playButton4.setEnabled(True)
        #default is on False, will not play video
        #How the button looks
        self.playButton4.clicked.connect(self.play4)  #when clicked, should play
        self.positionSlider4 = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider4.setRange(0, 0) #setting the range of the slider
        self.positionSlider4.sliderMoved.connect(self.setPosition4)
        
        self.errorLabel4 = QLabel()
        self.errorLabel4.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        
        # Create a widget for window contents
        # Create layouts to place inside widget

        self.videoWidget4 = QVideoWidget()
        self.controlLayout4 = QHBoxLayout()
        self.controlLayout4.setContentsMargins(0, 0, 0, 0)
        self.controlLayout4.addWidget(self.playButton4)
        self.controlLayout4.addWidget(self.positionSlider4)
 
        self.layout4 = QVBoxLayout()
        self.layout4.addWidget(self.videoWidget4)
        self.layout4.addLayout(self.controlLayout4)
        self.layout4.addWidget(self.errorLabel4)
        # Set widget to contain window contents
        self.Video_widget4 = QWidget()
        self.Video_widget4.setLayout(self.layout4)
 
        self.mediaPlayer4.setVideoOutput(self.videoWidget4)
        self.mediaPlayer4.stateChanged.connect(self.mediaStateChanged4)
        self.mediaPlayer4.positionChanged.connect(self.positionChanged4)
        self.mediaPlayer4.durationChanged.connect(self.durationChanged4)
        self.mediaPlayer4.error.connect(self.handleError4)
        self.loaded4 = 0

        self.l14 = QLabel()
        self.l24 = QLabel()
        self.l34 = QLabel()
        self.l44 = QLabel()
        self.tab1Lay4 = QVBoxLayout()
        
        for i, j in zip([1, 2, 3, 4], [self.l14, self.l24, self.l34, self.l44]):
            j.setPixmap(QPixmap("media/Iodination-"+str(i)+".jpg"))
            j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            j.setAlignment(Qt.AlignCenter)
            self.tab1Lay4.addWidget(j)

        self.scrollWidget4 = QWidget()
        self.scrollWidget4.setLayout(self.tab1Lay4)
        
        self.scrollAr4 = QScrollArea()
        self.scrollAr4.setWidget(self.scrollWidget4)
        
        self.tab1Lay24 = QVBoxLayout()
        self.tab1Lay24.addWidget(self.scrollAr4)
        
        self.tab14.setLayout(self.tab1Lay24)
        self.mode = False
        
        self.tab3Lay4 = QVBoxLayout()
        self.tab3Lay4.addWidget(self.Video_widget4)
        self.tab34.setLayout(self.tab3Lay4)
        '''
        self.HomePage_lay4 = QHBoxLayout()
        self.HomePage_lay4.addWidget(self.tabs4)       
        self.Exp4_widget = QWidget()
        self.setLayout(self.HomePage_lay4)
        self.setWindowTitle("PHOTOMETERY")
        '''
        #print("ALL pages created")
        
def main_exp2():
    #print("Function called")
    obj = Exp2_class()
    #print("Object Created")
    return obj
def getUnknowns():
    return[ace, hcl, iod]
