import random
from PyQt5.QtWidgets import QLabel, QMessageBox
from DragNDrop import DropLabel
from EXP3 import Exp3_class
from ModWidgets import PushButton, VoHGroup
from common import ImageLabel

class Exp6_class(Exp3_class):
    def __init__(self, stack):
        super().__init__(stack, imageList=["media/soap-1.jpg", "media/soap-2.jpg", "media/soap-3.jpg"])

        self.SolsTab.cellWidget(0, 3).setText("Oil Sample")
        self.SolsTab.cellWidget(0, 4).setText("Fat Solvent")
        self.SolsTab.cellWidget(0, 6).setText("Ethanolic KOH")

        self.den = float(random.randint(80, 99)/100)
        stren = float(random.randint(400, 500)/100)

        self.SolsTab.cellWidget(3, 3).setName("Oil")
        self.SolsTab.cellWidget(3, 3).setCon(stren)

        self.SolsTab.cellWidget(1, 3).setText(""+str(self.den)+"g/cm3")
        self.SolsTab.cellWidget(2, 3).setValue(5)
        self.SolsTab.cellWidget(3, 3).setCol(0)

        self.SolsTab.cellWidget(3, 4).setName("Fat")
        self.SolsTab.cellWidget(3, 4).setCon(17.1)
        self.SolsTab.cellWidget(3, 4).setCol(0)
        self.SolsTab.cellWidget(1, 4).setText("1:1 v/v")
        self.SolsTab.cellWidget(2, 4).setValue(20)

        strn = float(random.randint(655, 855)/1000)

        self.SolsTab.cellWidget(3, 6).setName("KOH")
        self.SolsTab.cellWidget(3, 6).setCol(1)
        self.SolsTab.cellWidget(3, 6).setCon(strn)
        self.SolsTab.cellWidget(1, 6).setText("-")
        self.SolsTab.cellWidget(2, 6).setValue(40)

        self.retBut.setText("--RESET--")
        self.retBut.setEnabled(True)
        self.min = 45
        self.MINPER = 45
        self.timerDis.setText("45:00")

        self.CURRENT_BUR = "Bur"
        self.CURRENT_CON = "Flask"

        self.SUBFLAG1 = False
        self.SUBFLAG2 = False
        self.extra = True
        self.loadNAOH.setText("Load Bur.")
        self.dataGEN = [0, 0, 0, 0, 0]

    def setUPEqui(self):

        self.SUB1 = PushButton("Load Flask-1\nfor titration")
        self.SUB2 = PushButton("Load Flask-2\nfor titration")

        self.EquiLab = DropLabel("f1", "media/empty2.png", self)
        self.EquiLab.textChanged.connect(self.update)

        self.resetBUT = ImageLabel("FLASK-1(NO OIL)")
        self.resetBUT.setMaximumHeight(20)

        self.RetLab = ImageLabel("FLASK-2(WITH OIL)")
        self.RetLab.setMaximumHeight(20)

        self.RetFlask = DropLabel("f2", "media/empty2.png", parent=self)
        self.RetFlask.textChanged.connect(self.update4)

        self.DropBox = VoHGroup("V")
        self.DropBox.addWidgets([self.resetBUT, self.EquiLab.getLabel() ])
        self.DropBox.setMaximumWidth(170)


        self.retBut.clicked.connect(self.RESET)

        self.RetLAYW = VoHGroup("V")
        self.RetLAYW.addWidgets([self.RetLab, self.RetFlask.getLabel()])
        self.RetLAYW.setMaximumWidth(170) 
        self.RETFLAG = 0
        


    def update(self):

        try:
            if(self.EquiLab.text() == "f1"):
                return

            PASS = False
            if(self.startFlag == False):
                if(self.EquiLab.name()=="Oil"):
                    self.errorMessageM(QMessageBox.Critical, "No Oil Needed", "This Flask is to be prepared without oil.", "No Oil needed")
                    PASS = True
                        
                elif(self.EquiLab.name()=="Fat"):
                    if(self.AceLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.AceLoad = True
                        
                elif(self.EquiLab.name()=="KOH"):
                    if(self.ethLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.ethCon = self.EquiLab.con()
                        self.ethVol = self.EquiLab.vol()
                        self.ethLoad = True
                        
                else:
                    self.errorMessageM(QMessageBox.Information, "Extra Component", "Only Solvent and KOH is needed in this flask.", "Invalid Addition")
                    PASS=True

                if(PASS == False):   
                    self.dropCount += 1
                    if(self.dropCount == 1):
                        self.EquiLab.setImage("media/halffill2.png")
                    elif(self.dropCount == 2):
                        self.EquiLab.setImage("media/fill2.png")
                    else:
                        self.errorFlag = 5
                        self.errorMessage()
            else:
                self.errorFlag = 2
                self.errorMessage()

            self.EquiLab.setText("f1")

        except:
            self.UNKNOWNERROR = "Updating Flask parameters"
            self.errorMessage()  

    def update4(self):

        try:
            if(self.RetFlask.text() == "f2"):
                return
            PASS = False
            if(self.startFlag == False):
                if(self.RetFlask.name()=="Oil"):
                    if(self.HclLoad):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.HclCon = self.RetFlask.con()
                        self.HclVol = self.RetFlask.vol()
                        self.HclLoad = True
                        
                elif(self.RetFlask.name()=="Fat"):
                    if(self.SUBFLAG1):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True

                    else:
                        self.SUBFLAG1 = True
                        
                elif(self.RetFlask.name()=="KOH"):
                    if(self.SUBFLAG2):
                        self.errorFlag = 8
                        self.errorMessage()
                        PASS = True
                    else:
                        self.aceCon = self.RetFlask.con()
                        self.aceVol = self.RetFlask.vol()
                        self.SUBFLAG2 = True
                        
                else:
                    self.errorMessageM(QMessageBox.Information, "Extra Component", "Only OIL, Fat Solvent and KOH is needed in this flask.", "Invalid Addition")
                    PASS=True

                if(PASS == False):   
                    self.RETFLAG += 1
                    if(self.RETFLAG == 1):
                        self.RetFlask.setImage("media/halffill1.png")
                    elif(self.RETFLAG == 2):
                        self.RetFlask.setImage("media/halffill2.png")
                    elif(self.RETFLAG == 3):
                        self.RetFlask.setImage("media/fill2.png")
                    else:
                        self.errorFlag = 5
                        self.errorMessage()
            else:
                self.errorFlag = 2
                self.errorMessage()

            self.RetFlask.setText("f2")
            
        except Exception as e:
            self.UNKNOWNERROR = "Updating Flask parameters and " + str(e)
            self.errorMessage() 

    def START(self):

        if(self.startFlag == False):
            if(self.AceLoad and self.ethLoad and self.HclLoad and  self.SUBFLAG1 and self.SUBFLAG2):
                self.startFlag = True
                self.Finx = self.aceCon*self.aceVol - self.HclCon*self.HclVol
                self.dataGEN[0] = self.den*self.HclVol
                self.dataGEN[1] = self.SolsTab.cellWidget(3, 1).con()
                self.dataGEN[2] = (self.ethCon*self.ethVol)/self.dataGEN[1]
                self.dataGEN[3] = (self.Finx)/self.dataGEN[1]
                self.dataGEN[4] = (56 *(self.dataGEN[2]-self.dataGEN[3])*self.dataGEN[1])/self.dataGEN[0]

                if(self.Finx <= 0):
                    self.Finx = 0
                self.timerTub.start(1000)

            else :
                self.errorFlag = 4
                self.errorMessage()
                return
        else:
            self.errorFlag = 2
            self.errorMessage()
            return

    def CHANGERESET(self):

        self.RESETDROP(self.EquiLab, "f1")
        self.EquiLab.setImage("media/empty2.png")
        self.RESETDROP(self.RetFlask, "f2")
        self.RetFlask.setImage("media/empty2.png")

        self.SUBFLAG1 = False
        self.SUBFLAG2 = False
        self.RETFLAG = 0

    def SUBMIT1(self):
        if(self.startFlag):
            if(self.start == False and self.LoadedINFLASK == False):
                self.FlaDrop.setImage("media/flaskB2.png")
                self.LoadedINFLASK = True
                self.CURRENT_CON = 1
                self.conFlask = self.ethCon*self.ethVol
            else:
                self.errorFlag = 2
                self.errorMessage()
        else:
            self.errorMessageM(QMessageBox.Warning, "No Reaction", "Please Start the reaction in flasks first.", "No reaction in progres")

    def SUBMIT2(self):
        if(self.startFlag):
            if(self.start == False and self.LoadedINFLASK == False):
                self.FlaDrop.setImage("media/flaskB2.png")
                self.LoadedINFLASK = True
                self.CURRENT_CON = 1
                timeSpent = (45-self.min)*60 + (60-self.sec)
                if (timeSpent >= 2700):
                    x = self.FinX
                else:
                    x = (self.FinX*timeSpent)/2700
                    x = round(x, 3)
                self.FlaDrop.setImage("media/flaskB2.png")
                self.LoadedINFLASK = True
                self.CURRENT_CON = 1
                self.conFlask = x
            else:
                self.errorFlag = 2
                self.errorMessage()
        else:
            self.errorMessageM(QMessageBox.Warning, "No Reaction", "Please Start the reaction in flasks first.", "No reaction in progres")

    def update3(self):	
        try:
            if(self.TitDrop.text() == "Bur"):
                return
            if(self.resumeFlag):
                if(self.TitDrop.name() == self.CURRENT_BUR):
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
                   self.errorMessageM(QMessageBox.Warning, "Different Solution", "You are loading a different solution in burette", "Different Solution")
                   self.TitDrop.setText("Bur") 
                   return         

            if(self.start):
                self.errorFlag = 2
                self.errorMessage()
            else:
                self.burCon = self.TitDrop.con()
                self.burVol = self.TitDrop.vol()
                self.movie.setValue(int((self.burVol*100)-5000))
                self.LOADMARK = (self.burVol*100)-5000
                self.burFlag = True
                self.CURRENT_BUR = self.TitDrop.name()

            self.TitDrop.setText("Bur")
        except Exception as e:
            self.UNKNOWNERROR = "Updating Burette parameters and "+str(e)
            self.errorMessage()
            self.TitDrop.setText("Bur")

    def update2(self):
        try:

            if(self.FlaDrop.text() == "Flask"):
                return
            if(self.start):
                self.errorFlag = 2
                self.errorMessage()

            else:
                
                if(self.FlaDrop.name() == " Phenolphthalein "):
                    
                    if(self.LoadedINFLASK == True):
                        if(self.CURRENT_CON == 1):
                            self.FlaDrop.setImage("media/flaskC2.png")
                        self.loadKIFLAG = True
                    else:
                        self.errorMessageM(QMessageBox.Warning, "No Solution", "No Sample is loaded. Drag and drop a flask to titrate first", "No Sample")

                elif(self.LoadedINFLASK == False):
                    self.FlaDrop.setImage("media/flaskB2.png")
                    self.LoadedINFLASK = True
                    self.CURRENT_CON = self.FlaDrop.col()
                    self.conFlask = self.FlaDrop.vol()*self.FlaDrop.con()

                else:
                    self.errorMessageM(QMessageBox.Critical, "Reset", "Sample Already loaded, reset Required", "Please Reset First")   
            self.FlaDrop.setText("Flask")
            
        except:
            self.UNKNOWNERROR = "Updating Flask parameters"
            self.errorMessage()
            self.FlaDrop.setText("Flask")

    def hiddenTimer(self):
        try:
            if self.start and self.resumeFlag == False:
                self.volumeDown -= 1
                self.marker += 1
                if(self.extra):
                    if (self.volumeDown <= 20 and self.volumeDown >= -20):
                        self.FlaDrop.setImage("media/flaskE2.png")
                    elif(self.volumeDown <= -20 and self.volumeDown >= -25):
                        self.FlaDrop.setImage("media/flaskC2.png")
                else:
                    if (self.volumeDown <= 5 and self.volumeDown >= 0):
                        self.FlaDrop.setImage("media/flaskE2.png")
                    elif(self.volumeDown <= 0 and self.volumeDown >= -10):
                        self.FlaDrop.setImage("media/flaskB2.png")

            if self.start:
                self.movie.setValue(int(self.LOADMARK-self.marker))
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

    def START2(self):
        try:
            if(self.LoadedINFLASK and  self.burFlag):
                if(self.loadKIFLAG):
                    if(self.CURRENT_CON == 1 and self.TitDrop.col() == 2):
                        self.extra = False
                    elif(self.CURRENT_CON == 2 and self.TitDrop.col() == 1):
                        self.extra = True
                    else:
                        self.errorFlag = 11
                        self.errorMessage()
                        return
                    
                    self.volumeDown = (100*self.conFlask)/self.burCon
                    self.marker = 0
                    self.volumeDown = int(self.volumeDown)
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