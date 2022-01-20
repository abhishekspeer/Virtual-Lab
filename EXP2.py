from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout,QLCDNumber,QMessageBox, QDoubleSpinBox, QWidget, QLabel,QLineEdit, QPushButton, QHBoxLayout
import random
from ModWidgets import Dial, FGroup, TableMod, VoHGroup, VoHWidget, PushButton
from DragNDrop import DragLabel, DropLabel
from common import EXP_PAGE, ImageLabel

class Exp2_class(EXP_PAGE):

    def __init__(self, stack):
        imageList = [0, 0, 0, 0]
        self.mode = False
        for i in [0, 1, 2, 3]:
             imageList[i] = "media/Iodination-"+str(i+1)+".jpg"
        self.dataGEN = [0, 0, 0]
        super().__init__(imageList, "media/exp2.mp4", stack)

        self.stockSol_val = TableMod(1, 6)
        for i, j in zip([0, 1, 2], ["Acetone:", "HCl:", "Iodine:"]):
            self.stockSol_val.setCellWidget(0, i*2, QPushButton(j))
            #self.stockSol_val.cellWidget(0, i*2).setAlignment(Qt.AlignCenter)
            self.stockSol_val.setCellWidget(0, (i*2)+1, QLineEdit())
            self.stockSol_val.cellWidget(0, (i*2)+1).setText("0.00")
            self.stockSol_val.cellWidget(0, (i*2)+1).setMaximumWidth(50)
            #self.stockSol_val.cellWidget(0, (i*2)+1).editingFinished.connect(self.validateStock)
            #self.stockSol_val.cellWidget(0, (i*2)+1).returnPressed.connect(self.validateStock)
            
        #self.stockSol_val.setMaximumWidth(310)
        self.stockSol_val.setMinimumWidth(310)
        self.stockSol_val.setMaximumHeight(50)
        self.stockSol_val.setMinimumHeight(50)
        
        self.Label2 = QLabel("A) IODINE FLASKS(10ml)")
        
        self.IodineTable = TableMod(3, 4)
        
        def whichButt1():
            self.cal_Iodine(0)
        def whichButt2():
            self.cal_Iodine(1)
        def whichButt3():
            self.cal_Iodine(2)
        def whichButt4():
            self.cal_Iodine(3)

        for i, j in zip([0, 1, 2, 3], [whichButt1, whichButt2, whichButt3, whichButt4]):

            self.IodineTable.setCellWidget(0, i, DragLabel("Iodine-"+str(i+1), "media/emptyflask.jpg", self))
            self.IodineTable.setCellWidget(1, i, QDoubleSpinBox())
            self.IodineTable.setCellWidget(2, i, QPushButton("Get", self.IodineTable))
            self.IodineTable.cellWidget(2,i).clicked.connect(j)
            
        self.IodineTable.resizing()
        self.IodineTable.setMaximumHeight(195)
        self.IodineTable.setMinimumHeight(195)
        self.IodineTable.setMaximumWidth(310)
        self.IodineTable.setMinimumWidth(310)

        self.Label4 = QLabel("B) TRIAL FLASKS(10ml)")
        self.SolsTab = TableMod(7, 4)

        for k in [0, 1, 2, 3]:
            self.SolsTab.setCellWidget(6, k, QPushButton("GET Trial-"+str(k+1)))

            self.SolsTab.setCellWidget(5, k, DragLabel("Trial-"+str(k+1), "media/emptyflask.jpg", self))
            #DragLabel.setCol
            self.SolsTab.cellWidget(5, k).setCol(k+1)

        self.SolsTab.cellWidget(6, 0).clicked.connect(self.whichButton1)
        self.SolsTab.cellWidget(6, 1).clicked.connect(self.whichButton2)
        self.SolsTab.cellWidget(6, 2).clicked.connect(self.whichButton3)
        self.SolsTab.cellWidget(6, 3).clicked.connect(self.whichButton4)

        
        self.SolsTab.setMaximumHeight(305)
        self.SolsTab.setMinimumHeight(305)
        #self.SolsTab.setMaximumWidth(310)
        self.SolsTab.setMinimumWidth(310)
            
        self.SolsTab.setCellWidget(0, 1, QLabel("Acetone"))
        self.SolsTab.setCellWidget(0, 2, QLabel("HCl"))
        self.SolsTab.setCellWidget(0, 3, QLabel("Iodine"))

        self.SolsTab.resizing()
            
        for i in range(1, 5):
            self.SolsTab.setCellWidget(i, 0, ImageLabel("  Trial-"+str(i)+"  "))
            
        for i in [1, 2, 3, 4]:
            for j in [1, 2, 3]:
                self.SolsTab.setCellWidget(i, j, QDoubleSpinBox())

    
        self.wid_2 = VoHWidget("V")
        self.wid_2.addWidgets([self.stockSol_val, self.Label2, self.IodineTable, self.Label4,self.SolsTab])

        self.meterLabel = DropLabel("Drop_here", 'media/photometer_open.jpg', self)
        self.meterLabel.textChanged.connect(self.update)

        self.absorb = QLineEdit()
        self.absorb.setEnabled(False)
        self.absorb.setFont(QFont('Times', 25))
        self.absorb.setStyleSheet("QLineEdit {color : white; border : 3px solid white;}")
        self.absorb.setMinimumHeight(100)
        self.absorb.setText("-E-")
        self.absorb.setAlignment(Qt.AlignCenter)

        self.absorbLab = ImageLabel("-ASORBANCE-\n(in fraction)")
        
        self.loadBut = PushButton("-LOAD-", False)
        self.loadBut.clicked.connect(self.loading)

        self.resetBut = QPushButton("-RESET-")
        self.resetBut.clicked.connect(self.reset)

        self.startBut = PushButton("-START-", False)
        self.startBut.clicked.connect(self.starting)

        self.otherMisc()

        self.sideBelowWid = VoHWidget("H")
        self.sideBelowWid.addWidgets([self.miscWid.Box, self.waveBox, self.InfoLabelGroup])
        #self.sideBelowWid.setMaximumHeight(250)

        self.sideWid2 = VoHGroup("V")
        self.sideWid2.VBOX.addStretch()
        self.sideWid2.addWidgets([self.meterLabel.getLabel(), self.sideBelowWid])
        self.sideWid2.VBOX.addStretch()
        

        self.Page4lay = QHBoxLayout()
        self.Page4lay.addWidget(self.wid_2)
        self.Page4lay.addStretch()
        self.Page4lay.addWidget(self.sideWid2)

        self.tab2.setLayout(self.Page4lay)
        
        self.errorFlag = 0
        self.count = 0
        self.timerIodine = QTimer()
        self.timerIodine.timeout.connect(self.showTime)
        self.start = False
        self.timerIodine.start(1000)
        self.valueToDisplay = 0

        self.loadedFlag = False
        
        self.loaded = False

        self.flasks_count = [0, 0, 0, 0]
        self.flasks_count_red = [0, 0, 0, 0]
        self.timerTrials = QTimer()
        self.timerTrials.timeout.connect(self.hiddenTimer)
        self.timerTrials.start(50)

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
            val = float(self.meterLabel.vol())
        except:
            return
        
        self.displayLoad.setText(str(self.meterLabel.name()))
        self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-\nPress LOAD")
        self.loadBut.setEnabled(True)
        self.loadedFlag = True

    def loading(self):
        if(self.loadedFlag):
            if(self.meterLabel.loaded() == False):
                self.meterLabel.setImage('media/photometer.jpg')
                self.InfoLabel.setText("//LOADED//\n\n-LID CLOSE-\nPress START")
                self.loadBut.setText("-UNLOAD-")
                self.startBut.setEnabled(True)
                self.meterLabel.setLoaded(True)
                return

            elif(self.meterLabel.loaded() == True):
                self.loadBut.setText("-LOAD-")
                self.meterLabel.setImage('media/photometer_open.jpg')
                self.absorb.setText("-E-")
                self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-\n(Drag and Drop)")
                self.displayLoad.setText("-NONE-")
                self.loadBut.setEnabled(False)
                self.valueToDisplay = 0
                self.meterLabel.setText("")
                self.meterLabel.setName("name")
                self.meterLabel.setVol(0.0)
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
                if(self.meterLabel.col() == 0):
                    self.absorb.setText(str(self.meterLabel.vol()))
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

        elif(self.meterLabel.col() != 0 and self.meterLabel.loaded() == True and self.startBut.text() == "-STOP-"):
            self.absorb.setText(str(self.valueToDisplay))
        else:
            self.startBut.setText("-START-")
            self.loadBut.setEnabled(True)

    def cal_Iodine(self, column):
        #column = self.IodineTable.currentColumn()
        try:
            val_wid = self.stockSol_val.cellWidget(0,5)
            st = float(val_wid.text())
            if st == 0:
                raise Exception
        except:
            self.errorFlag = 1
            self.errorMessage()
            return
        row = 1
        val = self.IodineTable.cellWidget(row,column).value()
        
        if val == 0 or val >= 10 :
            self.errorFlag = -1
            self.errorMessage()
            return

        absorbance = round(val/10 + (((float(random.randint(-500, 500)))/10000)*val), 3)
        if(absorbance > 1):
            absorbance = 1
        elif(absorbance< 0):
            absorbance = 0  
        flask = self.IodineTable.cellWidget(row-1,column)
        flask.setImage("media/iodine.jpg")
        flask.setVol(absorbance)

    def whichButton1(self):
        row = 1
        self.cal_Trial(row)
    def whichButton2(self):
        row = 2
        self.cal_Trial(row)
    def whichButton3(self):
        row = 3
        self.cal_Trial(row)
    def whichButton4(self):
        row = 4
        self.cal_Trial(row)
    
    def cal_Trial(self, row):
        K = 3.756
        self.mode = True
        if(self.validateStock()):
            
            variables = [0, 0, 0]
            tempsSum = 0
            for i, j in zip([1, 2, 3], [1, 3, 5]):
                temp = self.SolsTab.cellWidget(row, i).value()
                tempsSum = tempsSum+temp
                if(temp == 0 or temp >10):
                    self.errorFlag == -1*(i+1)
                    self.errorMessage()
                    return
                variables[i-1] = (float(self.stockSol_val.cellWidget(0,j).text())*(temp))/10
            
            if(tempsSum> 10):
                self.errorFlag = 5
                self.errorMessage()
                return
            rate = K*variables[0]*variables[1]
            time = (variables[2]*100000)/rate

            flask = self.SolsTab.cellWidget(5,row-1)
            flask.setImage("media/iodine.jpg")
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
                            if(i == self.meterLabel.col()):
                                setted = 1
                                value = self.flasks_count_red[i-1]/self.flasks_count[i-1]
                                value = value
                                self.valueToDisplay = round(value, 3)     
                            
            if(setted == 0):
                self.valueToDisplay = 0.01
                
        except:
            pass
        
    def validateStock(self):
        
        ace_wid = 0
        hcl_wid = 0
        iod_wid = 0
        try:
            ace_wid = float(self.stockSol_val.cellWidget(0,1).text())
            hcl_wid = float(self.stockSol_val.cellWidget(0,3).text())
            iod_wid = float(self.stockSol_val.cellWidget(0,5).text())
        except:
            self.errorFlag=8
            self.errorMessage()
            return False
        try:
            if(self.mode == True):
                self.mode = False
                if(ace_wid == 0 or hcl_wid == 0 or iod_wid == 0):
                    self.errorFlag = 1
                    self.errorMessage()
                    return False
                else:
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
                        self.dataGEN[ace_wid, hcl_wid, iod_wid]

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
        elif(self.errorFlag == 8):
            text = "Error! invalid stock solution entered"
            title = "Invalid Entry!"

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

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("RESET PRESSED !!!")
        msg.setInformativeText("Click on Ok if you want to reset all the  Trial solutions generated and instruments")
        msg.setWindowTitle("RESET TRIALS ?")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.resetOKPressed)
        retval = msg.exec_()
        if(retval == QMessageBox.Ok):
    
            self.meterLabel.setVol(0)
            self.meterLabel.setCol(0)
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

            for i in [0, 1, 2, 3]:
                flask = self.SolsTab.cellWidget(5,i)
                flask.setVol(0)
                flask.setImage("media/emptyflask.jpg")
                self.IodineTable.cellWidget(0, i).setImage("media/emptyflask.jpg")
                self.IodineTable.cellWidget(0, i).setVol(0)


    def changedWave(self):
        self.waveLCD.display(self.wave.value())

    def otherMisc(self):

        self.loWid = VoHWidget("V")
        self.loWid.addWidgets([self.startBut, self.loadBut, self.resetBut])

        self.HbTemp = QGridLayout()
        self.HbTemp.addWidget(self.loWid, 0,0, 1, 1)
        self.HbTemp.addWidget(self.absorb, 0, 1, 1, 3)
        

        self.HbWid = QWidget()
        self.HbWid.setLayout(self.HbTemp)

        for i in [self.absorbLab, self.loadBut, self.resetBut, self.startBut]:
            i.setFont(QFont('Times'))
        
        self.waveBox = VoHGroup("V")
        self.waveBox.addWidgets([self.absorbLab, self.HbWid])

        self.wave = Dial(200, 700)
        self.wave.setValue(250)
        self.wave.valueChanged.connect(self.changedWave)

        self.waveLab = ImageLabel("-WAVELENGTH-(in nm)")

        self.waveLCD = QLCDNumber()
        self.waveLCD.display(250)

        self.tempBox1 = VoHWidget("V")
        self.tempBox1.addWidgets([self.waveLab, self.waveLCD])

        self.tempBox2 = VoHWidget("H")
        self.tempBox2.addWidgets([self.wave, self.tempBox1])

        self.tempLcd = QDoubleSpinBox()
        self.tempLab = ImageLabel("-TEMPERATURE-(in C)")
        self.tempLcd.setValue(25)


        self.tempBox3Lay = QGridLayout()
        self.tempBox3Lay.addWidget(self.tempLab, 0,0, 1, 3)
        self.tempBox3Lay.addWidget(self.tempLcd, 0, 3, 1, 1)
        self.tempBox3 = QWidget()
        self.tempBox3.setLayout(self.tempBox3Lay)
        
        self.miscWid = FGroup("G")
        self.miscWid.addWidgets([[self.tempBox2], [self.tempBox3]])

        self.displayLoad = QLineEdit()
        self.displayLoad.setText("--NONE--")
        self.displayLoad.setReadOnly(True)

        self.label456 = ImageLabel("COM_DASH:")
        self.InfoLabel = QLabel("//UNLOADED//\n\n-LID OPEN-")
        self.InfoLabel.setMinimumWidth(200)
        self.InfoLabel.setMaximumWidth(200)
        self.InfoLabel.setMinimumHeight(150)
        self.InfoLabel.setAlignment(Qt.AlignCenter)
        self.InfoLabel.setFont(QFont('Times')) 
        self.InfoLabel.setStyleSheet("QLabel {border : 3px solid black;}")

        self.InfoLabelGroup = VoHGroup("V")
        self.InfoLabelGroup.addWidgets([self.displayLoad, self.InfoLabel])
