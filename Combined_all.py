# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import PyQt5
import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.QtGui
from PyQt5.QtGui import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import random
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
import smtplib
import os
x = 0
user_dets = []
remark = []

import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint 
  
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', 
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"] 
  
  
  
# Assign credentials ann path of style sheet 
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) 
client = gspread.authorize(creds) 
sheet = client.open("LOP Database").sheet1 
 
  
def loginverify(username,password):
	try:
 	 
# Sisplay data 
		data = sheet.get_all_records() 
		userid=[]
		usernameslist = sheet.col_values(2)
	
		k=0;
		#cell = sheet.cell(4, 1).value 
		for i in usernameslist	:
			k=k+1
			if username in i: 
				userid=(sheet.row_values(k))
				
		if userid[1]!=username :
			return 0
			
			
		if userid[2]==password:
			return userid
		else :
			return 0
	except:
		return 0


def getDetails(username):
	try:
		data = sheet.get_all_records() 
		userid=[]
		usernameslist = sheet.col_values(2)
		
		k=0;
		#cell = sheet.cell(4, 1).value 
		for i in usernameslist	:
			k=k+1
			if username in i: 
				userid=(sheet.row_values(k))
				return userid
	except:
		return ['0','invalid','invalid','invalid','invalid','invalid','invalid','invalid']				


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(821, 555)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/login-form-design-02.jpg);\n"
"color:white;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(270, 120, 310, 41))
        MainWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(270, 150, 251, 41))
        font = QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(331, 366, 191, 28))
        font = QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(" border-radius: 10px;\n"
"color:white;\n"
"text-align: center;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QRect(330, 400, 191, 27))
        
        font = QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(" border-radius: 10px;\n"
"color:white;\n"
"\n"
"")
        self.textEdit_2.setFrameShape(QFrame.StyledPanel)
        self.textEdit_2.setFrameShadow(QFrame.Raised)
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(278, 279, 59, 17))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(295, 462, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(403, 461, 169, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.check_password)
        self.pushButton_2.clicked.connect(self.ForgotpasswordForm)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 821, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Online Chemistry"))
        self.label.setText(_translate("MainWindow", "Welcome to Online Chemistry"))
        self.label_2.setText(_translate("MainWindow", "An online platform to perform all chemistry experiments"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">><br /></p></body></html>"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Forgot password..?"))
       

    def check_password(self):
        msg = QMessageBox()
        login_status=loginverify(self.textEdit.toPlainText().strip(),self.textEdit_2.toPlainText().strip())
        
        
        if login_status:	
            msg.setText('Success')
            user_details_list=getDetails(self.textEdit.toPlainText().strip())
            print(user_details_list)
            msg.exec_()
            global x
            x = 1
            global user_dets
            user_dets = user_details_list
            #app.quit()
            #os.system('python3 welcome.py')
            app.closeAllWindows()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()


    def ForgotpasswordForm(self):                                             
        self.w = ForgotpasswordForm()
        self.w.show()        

class ForgotpasswordForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Forgot password form')
        self.resize(500, 120)
    
        layout = QGridLayout()
        widget = QLabel('<font color=blue><h1>Online chemistry</h1></font>')
        label_name = QLabel('<font size="4"> Name </font>')
        label_email = QLabel('<font size="4"> Email Id </font>')

        layout.addWidget(widget, 0, 0)
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(label_email, 2, 0)

        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Please enter your name')
        label_email = QLabel('<font size="4"> EmailId </font>')
        layout.addWidget(self.lineEdit_name, 1, 1)
        
        self.lineEdit_email=QLineEdit()
        self.lineEdit_email.setPlaceholderText('Please enter your emailid')
        layout.addWidget(self.lineEdit_email, 2, 1)
        
        forgot_login = QPushButton('Send password')
        forgot_login.clicked.connect(self.forget_password)
        layout.addWidget(forgot_login, 3, 0)
        self.setLayout(layout)


    def forget_password(self):
    	
        sender='prakharpandey321@gmail.com'
        receiver=self.lineEdit_email.text()
        user_details=getDetails(receiver)
        password='pandey123'
        smtpserver=smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(sender,password)
        msg='Subject:Password of Online chemistry\n'+'Hi '+self.lineEdit_name.text()+'\n Username: '+user_details[1]+'\nPassword: '+user_details[2]+'\n\n regards\nDepartment of chemistry'
        smtpserver.sendmail(sender,receiver,msg)
        msg=QMessageBox()
        smtpserver.close()
        msg.setText('Mail Sent')
        msg.exec_()
        self.hide()

def main_runner(app, user_dets):
    Vlab = app
    #print(user_dets)
    global remark
    remark = user_dets
    #print(remark)
    VlabWind = VlabWindow(Vlab)
    VlabWind.show()
    VlabWind.raise_()
    Vlab.exec_()

class VlabWindow(QMainWindow):
    def __init__(self, Vlab):
        super().__init__()
        self.opp = Vlab
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("Virtual Chem-labs")
        self.DefPage()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.DefPage_widget)
        self.stacked_layout.setCurrentIndex(0)
        self.Central_widget = QWidget()
        self.Central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.Central_widget)
        self.setGeometry(100,50,1100,600)


    def DefPage(self):
        self.head = QLabel("VIRTUAL LABORATORY-1.0.0")
        self.head.setAlignment(Qt.AlignCenter)
        
        self.but1 = QPushButton("Experiment 1")
        self.but1.clicked.connect(self.exp1)
        
        self.but2 = QPushButton("Experiment 2")
        self.but2.clicked.connect(self.exp2)
        
        self.but3 = QPushButton("Experiment 3")
        self.but3.clicked.connect(self.exp3)
        
        self.but4 = QPushButton("Experiment 4")
        self.but4.clicked.connect(self.exp4)
        self.defLab = QLabel("Calculation of strength of ")
        self.defLab2 = QLabel("Idonation using photometry")
        self.defLab3 = QLabel("Equilibrium Constant calculation")
        self.defLab4 = QLabel("Dissociation Constant") 

        self.defLay = QFormLayout()

        for i, j in zip([self.but1, self.but2, self.but3, self.but4],
                        [self.defLab, self.defLab2, self.defLab3, self.defLab4]):
            self.defLay.addRow(i, j)

        
        self.defGr1 = QGroupBox()
        self.defGr1.setLayout(self.defLay)
        self.defLab5 = QLabel("Last performed remarks :")
        self.defLab5.setAlignment(Qt.AlignLeft)
        self.TEXT_BOX_H = QPlainTextEdit()
        #self.TEXT_BOX_H.setMaximumWidth(135)
        self.TEXT_BOX_H.setReadOnly(True)
        self.TEXT_BOX_H.setPlainText("hello")
        flag = 0
        self.TEXT_BOX_H.appendPlainText("USER_ID :" + remark[1])
        try:
            self.TEXT_BOX_H.appendPlainText("Experiment 1 :" + remark[3])
        except :
            self.TEXT_BOX_H.appendPlainText("Experiment 1 : NA")
        try:
            self.TEXT_BOX_H.appendPlainText("Experiment 2 :" + remark[4])
        except :
            self.TEXT_BOX_H.appendPlainText("Experiment 2 : NA")
        try:
            self.TEXT_BOX_H.appendPlainText("Experiment 3 :" + remark[5])
        except :
            self.TEXT_BOX_H.appendPlainText("Experiment 3 : NA")
        
        self.defPageLay = QVBoxLayout()
        self.defPageLay.addWidget(self.head)
        self.defPageLay.addWidget(self.defGr1)
        self.defPageLay.addWidget(self.defLab5)
        self.defPageLay.addWidget(self.TEXT_BOX_H)

        self.sideAni = QMovie("ani1.gif")
        self.sideAni.frameChanged.connect(self.repaint)
        self.sideAniLab = QLabel()
        self.sideAniLab.setMovie(self.sideAni)
        self.sideAni.start()

        self.defGr2 = QGroupBox()
        self.defGr2.setLayout(self.defPageLay)

        self.DefBox = QHBoxLayout()
        self.DefBox.addWidget(self.defGr2)
        self.DefBox.addWidget(self.sideAniLab)

        self.DefPage_widget = QWidget()
        self.DefPage_widget.setLayout(self.DefBox)
        #self.HomePage_widget.setGeometry(100,100,200,200)
        self.DefPage_widget.setWindowTitle("Chem OnLine")
        
    
    def exp1(self):
        
        try:

            self.stacked_layout.setCurrentWidget(self.Exp1_widget)
        except:
            self.EXP_page1()
            self.stacked_layout.addWidget(self.Exp1_widget)
            self.stacked_layout.setCurrentWidget(self.Exp1_widget)
        
    def exp2(self):
        
        try:

            self.stacked_layout.setCurrentWidget(self.Exp2_widget)
        except:
            self.EXP_2page()
            self.stacked_layout.addWidget(self.Exp2_widget)
            self.stacked_layout.setCurrentWidget(self.Exp2_widget)
        
    def exp3(self):
        
        
        try:
            #print("Ok2 3rd")
            self.stacked_layout.setCurrentWidget(self.Exp3_widget)
        except:
            self.Exp3Page()
            self.stacked_layout.addWidget(self.Exp3_widget)
            self.stacked_layout.setCurrentWidget(self.Exp3_widget)
        
    def exp4(self):
        try:
            #print("Ok2 3rd")
            self.stacked_layout.setCurrentWidget(self.Exp4_widget)
        except:
            self.Exp4_page()
            self.stacked_layout.addWidget(self.Exp4_widget)
            self.stacked_layout.setCurrentWidget(self.Exp4_widget)
            
    def dash(self):
        self.stacked_layout.setCurrentWidget(self.DefPage_widget)
    
    def EXP_page1(self):
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        #self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Theory")
        self.tabs.addTab(self.tab2,"Perform")
        self.tabs.addTab(self.tab3, "Video")
        self.tabs.addTab(self.tab4, "Question Bank")
        
        self.label = QLabel("1.Standarizing Hypo Solution\n with known concentration of CuSO4")
        self.label2 = QLabel("Process to prepare standard CuSO4.5H2O solution :")

        self.weight = QLineEdit()
        
        self.init_bur = 50.00
        self.n2 = QLineEdit()
        self.n2.setReadOnly(True)
        self.ans = QLineEdit()
        self.ans.setReadOnly(True)
        
        
        self.label3 = QLabel("Enter weight(grm) of CuSO4.5H2O salt\n(Taken in 100 ml of H2O)")
        self.WeightLine = QLineEdit()
        self.WeightLine.setFixedWidth(100)
        self.WeightLine.returnPressed.connect(self.getWeight)
        
        
        self.VolLabel = QLabel("Enter Volume(ml) of CuSO4.5H2O salt\n(Taken in conical flask)")
        self.VolLine = QLineEdit()
        self.VolLine.setFixedWidth(100)
        self.VolLine.setReadOnly(True)
        #self.vol = QLineEdit()
        self.VolLine.returnPressed.connect(self.getvol)
        self.tempLine = QLineEdit()
        self.tempLine.setReadOnly(True)
        self.tempLine.textChanged.connect(self.randomVol)
        
        self.label4 = QLabel()
        self.lab45 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()
        
        
        
        self.label7 = QLabel("2. Finding the strength of unknown CuSO4 solution")
        self.label8 = QLabel("Enter the Volume(ml) of unknown\n CuSO4.5H2O salt taken")
        self.Unknown = QLineEdit()
        self.Unknown.setFixedWidth(100)
        self.Unknown.setReadOnly(True)
        self.Unknown.returnPressed.connect(self.calculate)
        self.lab9 = QLabel()
        
        self.label9 = QLabel()
        self.label10 = QLabel()
        
        self.label11 = QLabel("Calculate the strength of unknown solution\n Put your answer below :")
        self.ansLine = QLineEdit()
        self.ansLine.setFixedWidth(100)
        self.ansLine.setReadOnly(True)
        self.ansLine.returnPressed.connect(self.checkAns)
        self.correctLabel = QLabel()

        self.HomeLay = QVBoxLayout()
        
        
        for i in[self.label, self.label2, self.label3, self.WeightLine, self.VolLabel, self.VolLine,
                   self.label4, self.lab45, self.label5, self.label6, self.label7, self.label8,
                   self.Unknown,self.lab9, self.label9, self.label10, self.label11, self.ansLine, self.correctLabel]:
            self.HomeLay.addWidget(i)
            
        
        self.Title = QLabel("DETERMINING THE STRENGTH OF UNKNOWN SOLUTION OF CuSO4")
        self.Title.setAlignment(Qt.AlignCenter)
        self.movie2 = QMovie("an2.gif")
        
        #self.movie2.frameChanged.connect(self.repaint)
        ##print("insideClass1")
        self.movie = QLabel()
        
        self.movie.setMovie(self.movie2)
        self.movie2.start()
        ##print("insideClass2")
        
        ##print("insideClassMid")
        self.movieBox = QVBoxLayout()
        self.movieBox.addWidget(self.Title)
        self.movieBox.addWidget(self.movie)
        self.group1 = QGroupBox()
        self.group1.setLayout(self.movieBox)
        self.group2 = QGroupBox()
        self.group2.setLayout(self.HomeLay)

        self.pageBox = QHBoxLayout()
        self.pageBox.addWidget(self.group2)
        self.pageBox.addWidget(self.group1)
        
        self.tab2.setLayout(self.pageBox)
        
        #self.tab1text = QPlainTextEdit()
        
        self.l1 = QLabel()
        self.l1.setPixmap(QPixmap("Copper-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setStyleSheet("QLabel {background-color: red;}")
        
        self.l2 = QLabel()
        self.l2.setPixmap(QPixmap("Copper-2.jpg"))
        self.l2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l2.setAlignment(Qt.AlignCenter)
        self.l2.setStyleSheet("QLabel {background-color: red;}")
        
        self.tab3text = QPlainTextEdit()
        self.tab4text = QPlainTextEdit()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton = QPushButton()
        self.playButton.setEnabled(True) #default is on False, will not play video
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
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

        self.backHome = QPushButton("Back")
        self.backHome.clicked.connect(self.goBackToDef)
        
        self.HomePage_lay = QFormLayout()
        self.HomePage_lay.addRow(self.tabs, self.backHome)
        
       
        
        self.Exp1_widget = QWidget()
        self.Exp1_widget.setLayout(self.HomePage_lay)
        self.Exp1_widget.setGeometry(100,100,200,200)
        self.Exp1_widget.setWindowTitle("Experiment 1")
        #print("insideClassend")

 
    def play(self):
        
        fileName = "exp1.mp4"
        if self.loaded1 == 0:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.loaded1 = 1
            
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
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
        
    def goBackToDef(self):
        self.stacked_layout.setCurrentWidget(self.DefPage_widget)
        
    def getWeight(self):
        try:
            flo = float(self.WeightLine.text())
            ##print("ok")
            self.label4.setText("Processing.....")
            ##print("ok2")
            self.weight.setText(str(flo))
            ##print("ok3")
            self.VolLine.setReadOnly(False)
        except:
            self.WeightLine.setText("")
            self.errorMessage()
        
    def getvol(self):
        try:
            f = float(self.VolLine.text())
            #self.vol = f
            init_bur = 50.00
            
            self.lab45.setText("Following are the burrette readings")
            #print("ok1")
            self.label5.setText("Initial Reading : "+str(init_bur)+ " ml")
            #print("ok2")
            self.tempLine.setText(str(f))
            #print("ok3")
            self.Unknown.setReadOnly(False)
            
        except:
            self.VolLine.setText("")
            self.errorMessage()
            
    def randomVol(self):
        f = float(self.tempLine.text())
        k = float(random.randint(10000, 40000))
        final_bur = k/1000
        we = float(self.weight.text())
        self.label6.setText("Final Reading : "+str(final_bur)+ " ml")
        n1 = we/249.68
        v2 = 50.00-f
        n2 = (n1*f)/v2
        self.n2.setText(str(n2))
            
    def calculate(self):
        try:
            n2 = float(self.n2.text())
            v3 = float(self.Unknown.text())
            k = float(random.randint(9000, 45000))
            v4 = k/1000
            self.lab9.setText("Following are the burrette readings")
            self.label9.setText("Initial Reading : "+str(self.init_bur)+ " ml")
            self.label10.setText("Final Reading : "+str(v4)+" ml")
            vlo4 = 50.00-v4
            n3 = (n2*vlo4)/v3
            self.ans.setText(str(n3))
            self.ansLine.setReadOnly(False)
        except:
            self.Unknown.setTeext("")
            self.errorMessage()
    def checkAns(self):
        try:
            an = float(self.ans.text())
            an = round(an, 3)
            user = float(self.ansLine.text())
            
            if(user >= an*0.95 and user <= an*1.05):
                self.correctLabel.setText("Correct Answer !")
            else:
                self.correctLabel.setText("Incorrect ! Ans = "+str(an))
        except :
            self.correctLabel.setText("Invalid !")

    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        self.w.setIcon(QMessageBox.Warning)
        self.w.setInformativeText("Invalid entry !")
        self.w.setWindowTitle("Warning")
        self.w.exec()

    def EXP_2page(self):

        #print("hello there")
        self.tabs2 = QTabWidget()
        self.tab12 = QWidget()
        self.tab22 = QWidget()
        self.tab32 = QWidget()
        self.tab42 = QWidget()
        self.tab52 = QPushButton()
        self.tabs2.addTab(self.tab12,"Theory")
        self.tabs2.addTab(self.tab22,"Perform")
        self.tabs2.addTab(self.tab32, "Video")
        self.tabs2.addTab(self.tab42, "Question Bank")
        #self.tabs2.addTab(self.tab52, "Back")
        
        #print("hello there")
        #self.tab2.setLayout(self.tab2Lay)

        self.l12 = QLabel()
        self.l12.setPixmap(QPixmap("Iodination-1.jpg"))
        self.l12.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.l22 = QLabel()
        self.l22.setPixmap(QPixmap("Iodination-2.jpg"))
        self.l22.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.l32 = QLabel()
        self.l32.setPixmap(QPixmap("Iodination-3.jpg"))
        self.l32.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.l42 = QLabel()
        self.l42.setPixmap(QPixmap("Iodination-4.jpg"))
        self.l42.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.tab1Lay2 = QVBoxLayout()
        self.tab1Lay2.addWidget(self.l12)
        self.tab1Lay2.addWidget(self.l22)
        self.tab1Lay2.addWidget(self.l32)
        self.tab1Lay2.addWidget(self.l42)
        
        self.scrollWidget2 = QWidget()
        self.scrollWidget2.setLayout(self.tab1Lay2)

        self.scrollAr2 = QScrollArea()
        self.scrollAr2.setWidget(self.scrollWidget2)
        
        self.tab1Lay22 = QVBoxLayout()
        self.tab1Lay22.addWidget(self.scrollAr2)
        self.tab12.setLayout(self.tab1Lay22)
        #first tab done
        
        
        self.ScrollArea = QScrollArea()
        self.ScrollArea.setObjectName("ScrollArea")
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy.setHeightForWidth(self.ScrollArea.sizePolicy().hasHeightForWidth())
        self.ScrollArea.setSizePolicy(sizePolicy)

        #print("hello there")
        
        self.ScrollArea.setFrameShape(QFrame.WinPanel)
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.ScrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 620, 1124))

        self.formLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget.setGeometry(QRect(27, 61, 498, 92))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBox_17 = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_17)
        self.doubleSpinBox_18 = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_18)
        self.doubleSpinBox_19 = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_19)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QRect(45, 42, 194, 17))
        self.label.setObjectName("label")
        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QRect(3, 180, 630, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QRect(62, 213, 505, 152))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(2, 0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(3, 0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(4, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setGeometry(QRect(163, 242, 100, 32))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_2.setGeometry(QRect(262, 242, 100, 32))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_3.setGeometry(QRect(362, 242, 100, 32))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_4 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_4.setGeometry(QRect(463, 243, 100, 32))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_5 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_5.setGeometry(QRect(163, 273, 100, 32))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_6 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_6.setGeometry(QRect(263, 272, 100, 32))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_7 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_7.setGeometry(QRect(363, 273, 100, 32))
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.doubleSpinBox_8 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_8.setGeometry(QRect(462, 271, 100, 32))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.doubleSpinBox_9 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_9.setGeometry(QRect(163, 301, 100, 32))
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.doubleSpinBox_10 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_10.setGeometry(QRect(263, 302, 100, 32))
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.doubleSpinBox_11 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_11.setGeometry(QRect(362, 302, 100, 32))
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.doubleSpinBox_12 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_12.setGeometry(QRect(462, 301, 100, 32))
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.doubleSpinBox_13 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_13.setGeometry(QRect(162, 332, 100, 32))
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.doubleSpinBox_14 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_14.setGeometry(QRect(262, 332, 100, 32))
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.doubleSpinBox_15 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_15.setGeometry(QRect(363, 331, 100, 32))
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.doubleSpinBox_16 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_16.setGeometry(QRect(463, 331, 100, 32))
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QRect(2, 401, 631, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QRect(106, 377, 434, 25))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QRect(258, 423, 141, 161))
        self.groupBox.setObjectName("groupBox")
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QRect(12, 28, 123, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet("QLCDNumber { background-color: red }")
        self.dial = QDial(self.groupBox)
        self.dial.setGeometry(QRect(49, 55, 50, 64))
        self.dial.setMouseTracking(False)
        self.dial.setMaximum(1000)
        self.dial.setObjectName("dial")
        self.dial.valueChanged.connect(lambda: self.dial_method())
        
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QRect(26, 130, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setGeometry(QRect(91, 51, 44, 17))
        font = QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setGeometry(QRect(0, 605, 631, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self.ScrollArea)
        
        self.sideAni2 = QMovie("graph2.gif")
        self.sideAniLab2 = QLabel()

        self.sideAni22 = QMovie("graph7.gif")
        self.sideAniLab22 = QLabel()

        self.grp1Lay2 = QVBoxLayout()
        self.grp1Lay2.addWidget(self.sideAniLab2)
        self.grp1Lay2.addWidget(self.sideAniLab22)

        self.sideAniLab2.setMovie(self.sideAni2)
        self.sideAni2.start()
        
        self.sideAniLab22.setMovie(self.sideAni22)
        self.sideAni22.start()
        
        self.grpBox2 = QWidget()
        self.grpBox2.setLayout(self.grp1Lay2)
        
        

        self.tab2Lay2 = QHBoxLayout()
        self.tab2Lay2.addWidget(self.ScrollArea)
        self.tab2Lay2.addWidget(self.grpBox2)
        
        self.tab22.setLayout(self.tab2Lay2)
        #second tab done


        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton2 = QPushButton()
        self.playButton2.setEnabled(True) #default is on False, will not play video
        self.playButton2.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
        self.playButton2.clicked.connect(self.play2)  #when clicked, should play
 
        self.positionSlider2 = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider2.setRange(0, 0) #setting the range of the slider
        self.positionSlider2.sliderMoved.connect(self.setPosition2)
 
        self.errorLabel2 = QLabel()
        self.errorLabel2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
        # Create a widget for window contents
 
        # Create layouts to place inside widget
        self.videoWidget2 = QVideoWidget()
        self.controlLayout2 = QHBoxLayout()
        self.controlLayout2.setContentsMargins(0, 0, 0, 0)
        self.controlLayout2.addWidget(self.playButton2)
        self.controlLayout2.addWidget(self.positionSlider2)
 
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.videoWidget2)
        self.layout2.addLayout(self.controlLayout2)
        self.layout2.addWidget(self.errorLabel2)
 
        # Set widget to contain window contents
        self.Video_widget2 = QWidget()
        self.Video_widget2.setLayout(self.layout2)
 
        self.mediaPlayer2.setVideoOutput(self.videoWidget2)
        self.mediaPlayer2.stateChanged.connect(self.mediaStateChanged2)
        self.mediaPlayer2.positionChanged.connect(self.positionChanged2)
        self.mediaPlayer2.durationChanged.connect(self.durationChanged2)
        self.mediaPlayer2.error.connect(self.handleError2)
        self.loaded2 = 0

        self.tab3Lay2 = QVBoxLayout()
        self.tab3Lay2.addWidget(self.Video_widget2)
        self.tab32.setLayout(self.tab3Lay2)
        
        self.backHome2 = QPushButton("Back")
        self.backHome2.clicked.connect(self.goBackToDef)
        
        
        
        self.HExp2_lay = QHBoxLayout()
        self.HExp2_lay.addWidget(self.tabs2)
        self.HExp2_lay.addWidget(self.backHome2)
        
        self.Exp2_widget = QWidget()
        self.Exp2_widget.setGeometry(100,100,200,200)
        self.Exp2_widget.setLayout(self.HExp2_lay)
        #overall done
        
        self.Exp2_widget.setWindowTitle("Experiment 2")

    def retranslateUi(self):
        #print("hello there re")
        _translate = QCoreApplication.translate
        self.ScrollArea.setWindowTitle(_translate("self.ScrollArea", "Experiment 2"))
        self.label_2.setText(_translate("self.ScrollArea", "Enter weight of Acetone(in grams)"))
        self.label_3.setText(_translate("self.ScrollArea", "Enter weight of HCl (in grams)"))
        self.label_4.setText(_translate("self.ScrollArea", "Enter weight of I<sub>2</sub> (in grams)"))
        self.label.setText(_translate("self.ScrollArea", "Stock Solution preparation:"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("self.ScrollArea", "Acetoen(in ml)"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("self.ScrollArea", "HCl(in ml)"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("self.ScrollArea", "H2O(in ml)"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("self.ScrollArea", "Iodine(in ml)"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("self.ScrollArea", "Trial 1"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("self.ScrollArea", "Trial 2"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("self.ScrollArea", "Trial 3"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("self.ScrollArea", "Trial 4"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("self.ScrollArea", "Click to confirm the readings "))
        self.pushButton.clicked.connect(lambda:self.Perdormexp())
        self.groupBox.setTitle(_translate("self.ScrollArea", "spectrophotometer"))
        self.pushButton_2.setText(_translate("self.ScrollArea", "Start"))
        
        self.pushButton_2.clicked.connect(lambda:self.chechValue())

        self.label_7.setText(_translate("ScrollArea", "λ (in nm)"))
        

    def dial_method(self):
        self.lcdNumber.display(self.dial.value())


    def Perdormexp(self):
        #calculate molarity of stock solution
        self.m1_acetone=(self.doubleSpinBox_17.value()/58.08)/0.1
        self.m1_hcl=(self.doubleSpinBox_18.value()/36.46)/0.1
        self.m1_iodine=(self.doubleSpinBox_19.value()/253.8089)/0.1

        #Calculate molarity for volumes used in trial 1
        self.total_volume_trial_1=self.doubleSpinBox.value()+self.doubleSpinBox_2.value()+self.doubleSpinBox_3.value()+self.doubleSpinBox_4.value()
        self.m1_acetone_trial1=(self.m1_acetone*self.doubleSpinBox.value())/self.total_volume_trial_1
        self.m1_hcl_trial1=(self.m1_hcl*self.doubleSpinBox_2.value())/self.total_volume_trial_1
        self.m1_iodine_trial1=(self.m1_iodine*self.doubleSpinBox_4.value())/self.total_volume_trial_1

        #Calculate molarity for volumes used in trial 2
        self.total_volume_trial_2=self.doubleSpinBox_5.value()+self.doubleSpinBox_6.value()+self.doubleSpinBox_7.value()+self.doubleSpinBox_8.value()
        self.m1_acetone_trial2=(self.m1_acetone*self.doubleSpinBox_5.value())/self.total_volume_trial_2
        self.m1_hcl_trial2=(self.m1_hcl*self.doubleSpinBox_6.value())/self.total_volume_trial_2
        self.m1_iodine_trial2=(self.m1_iodine*self.doubleSpinBox_8.value())/self.total_volume_trial_2

        #Calculate molarity for volumes used in trial 3
        self.total_volume_trial_3=self.doubleSpinBox_9.value()+self.doubleSpinBox_10.value()+self.doubleSpinBox_11.value()+self.doubleSpinBox_12.value()
        self.m1_acetone_trial3=(self.m1_acetone*self.doubleSpinBox_9.value())/self.total_volume_trial_3
        self.m1_hcl_trial3=(self.m1_hcl*self.doubleSpinBox_10.value())/self.total_volume_trial_3
        self.m1_iodine_trial3=(self.m1_iodine*self.doubleSpinBox_12.value())/self.total_volume_trial_3

        #Calculate molarity for volumes used in trial 4
        self.total_volume_trial_4=self.doubleSpinBox_13.value()+self.doubleSpinBox_14.value()+self.doubleSpinBox_15.value()+self.doubleSpinBox_16.value()
        self.m1_acetone_trial4=(self.m1_acetone*self.doubleSpinBox_13.value())/self.total_volume_trial_4
        self.m1_hcl_trial4=(self.m1_hcl*self.doubleSpinBox_14.value())/self.total_volume_trial_4
        self.m1_iodine_trial4=(self.m1_iodine*self.doubleSpinBox_16.value())/self.total_volume_trial_4

    
    def chechValue(self):
        if self.dial.value()==545:
            self.Spectoscopy()
        else:
            msgBox=QMessageBox()
            msgBox.setText("Error No Data available for mentioned Wavelength")
            msgBox.exec()
            
    def Spectoscopy(self):
        _translate = QCoreApplication.translate
        self.k=random.randint(-4,5)
        self.k=28+self.k
        self.k=self.k/1000000
        self.k_dash_trial1=self.k*self.m1_acetone_trial1*self.m1_hcl_trial1
        self.k_dash_trial2=self.k*self.m1_acetone_trial2*self.m1_hcl_trial2
        self.k_dash_trial3=self.k*self.m1_acetone_trial3*self.m1_hcl_trial3
        self.k_dash_trial4=self.k*self.m1_acetone_trial4*self.m1_hcl_trial4
        t=0
        key=int(1)
        sys.stdout = open("lab_record.txt", "w")
        #print("trial 1")
        #print("Time(sec)\tabsorbance")
        while(t<1800):
            a=0.3636*(self.m1_iodine_trial1-self.k_dash_trial1*t)
            #print(t,"\t",a)
            t=t+30
        t=0
        #print("trial 2")
        #print("Time(sec)\tabsorbance")    
        while(t<1800):
            a=0.3636*(self.m1_iodine_trial2-self.k_dash_trial2*t)
            #print(t,"\t",a)
            t=t+30
        t=0
        #print("trial 3")
        #print("Time(sec)\tabsorbance")
        while(t<1800):
            a=0.3636*(self.m1_iodine_trial3-self.k_dash_trial3*t)
            #print(t,"\t",a)
            t=t+30
        t=0
        #print("trial 4")
        #print("Time(sec)\tabsorbance")
        while(t<1800):
            a=0.3636*(self.m1_iodine_trial4-self.k_dash_trial4*t)
            #print(t,"\t",a)
            t=t+30
        msgBox=QMessageBox()
        msgBox.setText("Sucessful, The record has been saved to your pc in the file folder")
        msgBox.exec()

    def play2(self):
        
        fileName = "exp2.mp4"
        if self.loaded2 == 0:
            self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton2.setEnabled(True)
            self.loaded2 = 1
            
        if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer2.pause()
        else:
            self.mediaPlayer2.play()
 
    def mediaStateChanged2(self, state):
        if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
            self.playButton2.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton2.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged2(self, position):
        self.positionSlider2.setValue(position)
 
    def durationChanged2(self, duration):
        self.positionSlider2.setRange(0, duration)
 
    def setPosition2(self, position):
        self.mediaPlayer2.setPosition(position)
 
    def handleError2(self):
        self.playButton2.setEnabled(False)
        self.errorLabel2.setText("Error: " + self.mediaPlayer2.errorString())
        

    def Exp3Page(self):
        ##print("insideClass")
        self.tabs3 = QTabWidget()
        self.tab13 = QWidget()
        self.tab23 = QWidget()
        self.tab33 = QWidget()
        self.tab43 = QWidget()

        self.tabs3.addTab(self.tab13,"Theory")
        self.tabs3.addTab(self.tab23,"Perform")
        self.tabs3.addTab(self.tab33, "Video")
        self.tabs3.addTab(self.tab43, "Question Bank")

        #print("tabs added")
        # Create first tab
        self.templab3 = QLabel("Room Temp :")
        self.tempLine3 = QLineEdit()
        self.next3 = QPushButton("Next")
        self.next3.clicked.connect(self.getVolumeNaOH3)
        
        self.tempBox3 = QGroupBox()
        self.tempLay3 = QFormLayout()
        self.tempLay3.addRow(self.templab3, self.tempLine3)
        self.tempLay3.addRow(self.next3)
        
        self.tempBox3.setLayout(self.tempLay3)
        
        #print("temp box done")

        self.botlab3 = QLabel("")
        self.label3 = QLabel("")
        self.VolLab3 = QLabel("")
        self.vol1Naoh3 = QLineEdit()
        self.vol1Naoh3.setReadOnly(True)
        self.N1Naoh3 = QLineEdit()
        
        self.next13 = QPushButton("Next")
        self.next13.clicked.connect(self.getVolHCl3)

        self.tempBox23 = QGroupBox()
        self.tempLay23 = QFormLayout()
        
        self.tempLay23.addRow(self.botlab3)
        self.tempLay23.addRow(self.label3)
        self.tempLay23.addRow(self.VolLab3)
        self.tempLay23.addRow(self.VolLab3, self.vol1Naoh3)
        self.tempLay23.addRow(self.next13)
        self.tempBox23.setLayout(self.tempLay23)

        #print("NaOh done")
        
        self.labe23 = QLabel("")
        self.VolLab23 = QLabel("")
        self.volLabHcl3 = QLineEdit()
        self.volLabHcl3.setReadOnly(True)
        self.N3NHcl3 = QLineEdit()
        self.next23 = QPushButton("Next")
        self.next23.clicked.connect(self.lastStep3)

        self.tempBox33 = QGroupBox()
        self.tempLay33 = QFormLayout()
        
        self.tempLay33.addRow(self.labe23)
        self.tempLay33.addRow(self.VolLab23, self.volLabHcl3)
        self.tempLay33.addRow(self.next23)
        
        self.tempBox33.setLayout(self.tempLay33)
        #print("HCl done")
        
        self.labe33 = QLabel("")
        self.labe43= QLabel("")
        self.VolLast3 = QLabel("")
        self.VolLine3 = QLineEdit()
        self.VolLine3.setReadOnly(True)
        self.NLast3 = QLineEdit()
        #self.next2 = QPushButton("Next")

        self.tempBox43 = QGroupBox()
        self.tempLay43 = QFormLayout()
        
        self.tempLay43.addRow(self.labe33)
        self.tempLay43.addRow(self.labe43)
        self.tempLay43.addRow(self.VolLast3, self.VolLine3)
              
        self.tempBox43.setLayout(self.tempLay43)
        #print("Last done")
        

        self.HomeLay3 = QVBoxLayout()
        
        
        for i in[self.tempBox3, self.tempBox23, self.tempBox33, self.tempBox43]:
            self.HomeLay3.addWidget(i)
            
        #print("widgets added")
        
        self.Title3 = QLabel("DETERMINING THE EQUILIBRIUM CONSTANT")
        self.Title3.setAlignment(Qt.AlignCenter)
        self.movie23 = QMovie("test_tube.gif")
        
        self.movie3 = QLabel()
        
        self.movie3.setMovie(self.movie23)
        self.movie23.start()
        ##print("insideClass2")
        
        ##print("insideClassMid")
        self.movieBox3 = QVBoxLayout()
        self.movieBox3.addWidget(self.Title3)
        self.movieBox3.addWidget(self.movie3)
        self.group13 = QGroupBox()
        self.group13.setLayout(self.movieBox3)
        self.group23 = QGroupBox()
        self.group23.setLayout(self.HomeLay3)

        self.pageBox3 = QHBoxLayout()
        self.pageBox3.addWidget(self.group23)
        self.pageBox3.addWidget(self.group13)
        
        self.tab23.setLayout(self.pageBox3)

        #print("tab2 done")
        #self.tab1text = QPlainTextEdit()
        
        self.l13 = QLabel()
        self.l13.setPixmap(QPixmap("equi-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l13.setAlignment(Qt.AlignCenter)
        
        self.l23 = QLabel()
        self.l23.setPixmap(QPixmap("equi-2.jpg"))
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
        self.playButton3.setEnabled(True) #default is on False, will not play video
        self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
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

        self.backHome3 = QPushButton("Back")
        self.backHome3.clicked.connect(self.goBackToDef)
        self.HomePage_lay3 = QHBoxLayout()
        self.HomePage_lay3.addWidget(self.tabs3)
        self.HomePage_lay3.addWidget(self.backHome3)
        #print("back button added")
       
        self.Exp3_widget = QWidget()
        self.Exp3_widget.setLayout(self.HomePage_lay3)
        self.Exp3_widget.setGeometry(100,100,200,200)
        self.Exp3_widget.setWindowTitle("Experiment 3")

        ##print("insideClassend")

    def play3(self):
        
        fileName = "exp3.mp4"
        if self.loaded3 == 0:
            self.mediaPlayer3.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton3.setEnabled(True)
            self.loaded3 = 1
            
        if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer3.pause()
        else:
            self.mediaPlayer3.play()
 
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
        
    def lastStep3(self):
        try:
            self.labe33.setText("now we have following liquids\n5 mL  ~3N HCl Soluti, 4 mL pure ethanol\n1 mL glacial acetic acid, 5 mL pure ethyl acetate")
            self.labe43.setText("Titrate the whole contents of the bottles\nafter reaching equilibrium,\nwith standard NaOH solution using\n phenolphthalein indicator")
            self.VolLast3.setText("Vol of NaOH:")
            #print("funct-1.....")
            n2 = float(self.N3NHcl3.text())
            n1 = float(self.N1Naoh3.text())
            v2 = 5.00
            v1 = n2*v2/n1
            #print("funct-2......")
            self.VolLine3.setText(str(v1))
            
        except:
            #self.volLabHcl.setText("")
            self.errorMessage()
            
        
    def getVolumeNaOH3(self):
        #try:
        self.botlab3.setText("Solutions given :\n5ml ~3N HCl + 4ml C2H5OH+ 1 ml Acetic Acid")
        self.label3.setText("1.Standarizing ~1N NaOH\n with 0.3 Oxalic Acid")
        self.VolLab3.setText("Vol of NaOH :")
        #print("funct-1")
        self.tempLine3.setReadOnly(True)
        n2 = 0.30
        #print("funct-2")
        x = float(random.randint(-900, 900))
        n1 = 1.00 + float(x/float(1000))
        v2 = 25.00
        #print("funct-3")
        if(n1 == 0):
            n1 = 0.00001
        v1 = n2*v2/n1
        #print("funct-4")
        self.vol1Naoh3.setText(str(v1))
        self.N1Naoh3.setText(str(n1))
        #print("funct-5")            
        #except:
        #self.vol1Naoh.setText("")
        #self.N1Naoh.setText("")
        #self.errorMessage()
        
    def getVolHCl3(self):
        try:
            self.labe23.setText("2. Standardize ~3N HCl:")
            self.VolLab23.setText("Vol of HCl used :")
            n2 = float(self.N1Naoh3.text())
            v2 = float(self.vol1Naoh3.text())
            
            n1 = 3.00 + float(random.randint(-999, 999))/1000.00
            v1 = n2*v2/n1
            self.volLabHcl3.setText(str(v1))
            self.N3NHcl3.setText(str(n1))
            
        except:
            self.volLabHcl3.setText("")
            self.errorMessage()

    def Exp4_page(self):
        #print("Initiated")
        
        self.tabs4 = QTabWidget()
        self.tab14 = QWidget()
        self.tab24 = QWidget()
        self.tab34 = QWidget()
        self.tab44 = QWidget()

        self.tabs4.addTab(self.tab14,"Theory")
        self.tabs4.addTab(self.tab24,"Perform")
        self.tabs4.addTab(self.tab34, "Video")
        self.tabs4.addTab(self.tab44, "Question Bank")

        self.GiveLab = QLabel("Given Kcl Solution")
        self.spin_b = QDoubleSpinBox()
        self.spin_b.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        #self.spin_b.setValue("0.00")
        self.spin_b.valueChanged.connect(self.NoteValue)
        #print("initailized")
        self.AdjustLabel = QLabel("Adjust the Conductance")
        self.LineforDisplay = QLineEdit()
        self.LineforDisplay.setReadOnly(True)
        self.LineforDisplay.setText("0.00e-3ohm^-1cm^2")
        self.DialCond = QDial()
        self.DialCond.setRange(0, 10000)
        self.DialCond.setNotchesVisible(False)
        self.DialCond.valueChanged.connect(self.changedValue)
        self.labTemp = QLabel("")
        
        self.formLay1 = QFormLayout()
        self.formLay1.addRow(self.GiveLab, self.spin_b)
        self.formLay1.addRow(self.AdjustLabel, self.labTemp)
        self.formLay1.addRow(self.LineforDisplay, self.DialCond)
        #print("okasofar")
        self.widgetCond = QWidget()
        self.widgetCond.setLayout(self.formLay1)
        
        self.nextBut4 = QPushButton("Next")
        self.nextBut4.clicked.connect(self.setNext4)
        self.grpbox14 = QGroupBox()
        self.grpbox1lay4 = QVBoxLayout()
        self.grpbox1lay4.addWidget(self.widgetCond)
        self.grpbox1lay4.addWidget(self.nextBut4)
        self.grpbox14.setLayout(self.grpbox1lay4)
        #print("okasofar")
        #self.throwLab = QLabel("Throw out the KCL Soln")
        #self.WashLab = QLabel("Wash the Beaker and Electrode")
        self.PipLabel = QLabel("")
        self.makLab = QLabel("")
        self.UseLab = QLabel("")
        self.TheCon = QLabel("Concentration of stock:")
        self.ConLine = QLineEdit()
        self.nextBut24 = QPushButton("Next")
        self.nextBut24.setEnabled(False)
        self.nextBut24.clicked.connect(self.validate)
        
        self.grpbo2lay4 = QFormLayout()
        #self.grpbo2lay4.addWidget(self.throwLab)
        #self.grpbo2lay4.addWidget(self.WashLab)
        self.grpbo2lay4.addRow(self.PipLabel)
        self.grpbo2lay4.addRow(self.makLab)
        #self.grpbo2lay4.addRow(self.UseLab)
        self.grpbo2lay4.addRow(self.TheCon, self.ConLine)
        self.grpbo2lay4.addRow(self.UseLab)
        #self.grpbo2lay4.addWt(self.ConLine)
        self.grpbo2lay4.addRow(self.nextBut24)

        self.grpbo24 = QGroupBox()
        self.grpbo24.setLayout(self.grpbo2lay4)
        #print("okasofar")
        self.maklab = QLabel("Make up the Volm to 100ml using Stock:")
        self.rowTit_1 = QLabel("Conc")
        self.rowTit_2 = QLabel("H2O")
        self.rowTit_3 = QLabel("Stock")

        self.n4 = QLabel("N/4")
        self.n8 = QLabel("N/8")
        self.n16 = QLabel("N/16")
        self.n32 = QLabel("N/32")
        self.n64 = QLabel("N/64")
        #print("okasofar...")
        self.spin_n4h = QDoubleSpinBox()
        self.spin_n4n = QDoubleSpinBox()
        self.spin_n8h = QDoubleSpinBox()
        self.spin_n8n = QDoubleSpinBox()
        self.spin_n16h = QDoubleSpinBox()
        self.spin_n16n = QDoubleSpinBox()
        self.spin_n32h = QDoubleSpinBox()
        self.spin_n32n = QDoubleSpinBox()
        self.spin_n64n = QDoubleSpinBox()
        self.spin_n64h = QDoubleSpinBox()
        #print("okasofar.....")
        self.validateBut = QPushButton("Validate")
        self.validateBut.clicked.connect(self.validate2)
        
        self.grpbo3lay4 = QGridLayout()
        self.grpbo3lay4.addWidget(self.rowTit_1, 1, 0)
        self.grpbo3lay4.addWidget(self.rowTit_2, 1, 1)
        self.grpbo3lay4.addWidget(self.rowTit_3, 1, 2)
        
        #self.grpbo3lay4.addWidget(self.n4, self.spin_n4h, self.spin_n4n)
        self.grpbo3lay4.addWidget(self.n4, 2, 0)
        self.grpbo3lay4.addWidget(self.spin_n4h, 2, 1)
        self.grpbo3lay4.addWidget(self.spin_n4n, 2, 2)

        self.grpbo3lay4.addWidget(self.n8, 3, 0)
        self.grpbo3lay4.addWidget(self.spin_n8h, 3, 1)
        self.grpbo3lay4.addWidget(self.spin_n8n, 3, 2)

        self.grpbo3lay4.addWidget(self.n16, 4, 0)
        self.grpbo3lay4.addWidget(self.spin_n16h, 4, 1)
        self.grpbo3lay4.addWidget(self.spin_n16n, 4, 2)

        self.grpbo3lay4.addWidget(self.n32, 5, 0)
        self.grpbo3lay4.addWidget(self.spin_n32h, 5, 1)
        self.grpbo3lay4.addWidget(self.spin_n32n, 5, 2)

        self.grpbo3lay4.addWidget(self.n64, 6, 0)
        self.grpbo3lay4.addWidget(self.spin_n64h, 6, 1)
        self.grpbo3lay4.addWidget(self.spin_n64n, 6, 2)
        

        #self.grpbo3lay4.addRow(self.n8, self.spin_n8h, self.spin_n8n)
        #self.grpbo3lay4.addRow(self.n16, self.spin_n16h, self.spin_n16n)
        #self.grpbo3lay4.addRow(self.n32, self.spin_n32h, self.spin_n32n)

        self.grpbo34 = QGroupBox()
        self.temp1 = QGroupBox()
        self.temp1.setLayout(self.grpbo3lay4)
        
        self.grms34 = QVBoxLayout()
        self.grms34.addWidget(self.maklab)
        self.grms34.addWidget(self.temp1)
        self.grms34.addWidget(self.validateBut)
        
        self.grpbo34.setLayout(self.grms34)
        #print("okasofar4")
        self.marklab = QLabel("Note Conductance (in ohm^-1 cm^2):")

        self.markn4 = QLabel("N/4")
        self.markn8 = QLabel("N/8")
        self.markn16 = QLabel("N/16")
        self.markn32 = QLabel("N/32")
        self.markn64 = QLabel("N/64")

        self.note_n4n = QLineEdit()
        self.note_n4n.setReadOnly(True)
        self.note_n8n = QLineEdit()
        self.note_n8n.setReadOnly(True)
        self.note_n16n = QLineEdit()
        self.note_n16n.setReadOnly(True)
        self.note_n32n = QLineEdit()
        self.note_n32n.setReadOnly(True)
        self.note_n64n = QLineEdit()
        self.note_n64n.setReadOnly(True)
        
        self.grpbo4lay = QFormLayout()

        self.grpbo4lay.addRow(self.marklab)

        self.grpbo4grid = QGridLayout()
        self.grpbo4grid.addWidget(self.markn4, 0, 0)
        self.grpbo4grid.addWidget(self.note_n4n, 0, 1)
        self.grpbo4grid.addWidget(self.markn8, 0, 2)
        self.grpbo4grid.addWidget(self.note_n8n, 0, 3)
        self.grpbo4grid.addWidget(self.markn16, 1, 0)
        self.grpbo4grid.addWidget(self.note_n16n, 1, 1)
        self.grpbo4grid.addWidget(self.markn32, 1, 2)
        self.grpbo4grid.addWidget(self.note_n32n, 1, 3)
        self.grpbo4grid.addWidget(self.markn64, 2, 0)
        self.grpbo4grid.addWidget(self.note_n64n, 2, 1)

        self.grpbo4gridBox = QWidget()
        self.grpbo4gridBox.setLayout(self.grpbo4grid)

        self.grpbo4lay.addRow(self.grpbo4gridBox)

        self.grpbo44 = QGroupBox()
        self.grpbo44.setLayout(self.grpbo4lay)
        ########
        #print("okasofar5")

        self.side1box4 = QGroupBox()
        self.side1lay4 = QVBoxLayout()

        self.side1lay4.addWidget(self.grpbox14)
        self.side1lay4.addWidget(self.grpbo24)
        self.side1lay4.addWidget(self.grpbo34)
        self.side1lay4.addWidget(self.grpbo44)
        
        self.side1box4.setLayout(self.side1lay4)
        #print("OnesideDone")

        self.Titlelab4 = QLabel("DISSOCIATION CONSTANT")
        self.Titlelab4.setAlignment(Qt.AlignCenter)

        self.ani4 = QMovie("discon2.gif")
        self.aniLab4 = QLabel()
        self.aniLab4.setMovie(self.ani4)
        self.ani4.start()

        self.side2lay4 = QVBoxLayout()
        self.side2lay4.addWidget(self.Titlelab4)
        self.side2lay4.addWidget(self.aniLab4)

        self.side2wid4 = QWidget()
        self.side2wid4.setLayout(self.side2lay4)

        self.Page4lay = QHBoxLayout()
        self.Page4lay.addWidget(self.side1box4)
        self.Page4lay.addWidget(self.side2wid4)

        self.tab24.setLayout(self.Page4lay)
        #print("tab2done")
        self.mediaPlayer4 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton4 = QPushButton()
        self.playButton4.setEnabled(True) #default is on False, will not play video
        self.playButton4.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
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
        self.l14.setPixmap(QPixmap("discon-1.jpg"))
        self.l14.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l14.setAlignment(Qt.AlignCenter)
        
        self.l24 = QLabel()
        self.l24.setPixmap(QPixmap("discon-2.jpg"))
        self.l24.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l24.setAlignment(Qt.AlignCenter)
    
        self.l34 = QLabel()
        self.l34.setPixmap(QPixmap("discon-3.jpg"))
        self.l34.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l34.setAlignment(Qt.AlignCenter)
  
        self.l44 = QLabel()
        self.l44.setPixmap(QPixmap("discon-4.jpg"))
        self.l44.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l44.setAlignment(Qt.AlignCenter)

        self.tab1Lay4 = QVBoxLayout()
        self.tab1Lay4.addWidget(self.l14)
        self.tab1Lay4.addWidget(self.l24)
        self.tab1Lay4.addWidget(self.l34)
        self.tab1Lay4.addWidget(self.l44)

        self.scrollWidget4 = QWidget()
        self.scrollWidget4.setLayout(self.tab1Lay4)
        
        self.scrollAr4 = QScrollArea()
        self.scrollAr4.setWidget(self.scrollWidget4)
        
        self.tab1Lay24 = QVBoxLayout()
        self.tab1Lay24.addWidget(self.scrollAr4)
        
        self.tab14.setLayout(self.tab1Lay24)
        
        
        self.tab3Lay4 = QVBoxLayout()
        self.tab3Lay4.addWidget(self.Video_widget4)
        self.tab34.setLayout(self.tab3Lay4)

        self.backHome4 = QPushButton("Back")
        self.backHome4.clicked.connect(self.goBackToDef)
        self.HomePage_lay4 = QHBoxLayout()
        self.HomePage_lay4.addWidget(self.tabs4)
        self.HomePage_lay4.addWidget(self.backHome4)
        #print("back button added")
       
        self.Exp4_widget = QWidget()
        self.Exp4_widget.setLayout(self.HomePage_lay4)
        self.Exp4_widget.setGeometry(100,100,200,200)
        self.Exp4_widget.setWindowTitle("Experiment 4")

        ##print("insideClassend")

    def setNext4(self):
        val = float(self.DialCond.value())/100
        if(val != 12.88):
            self.errorMessage()
            return
        
        self.PipLabel.setText("Pipette out 50 ml 1N Acetic Acid")
        self.makLab.setText("Make up the volm to 100 ml")
        #self.UseLab = QLabel("Use Conductivity Water !!")
        self.TheCon.setText("Concentration of stock:")
        self.nextBut24.setEnabled(True)

    def play4(self):
        
        fileName = "exp4.mp4"
        if self.loaded4 == 0:
            self.mediaPlayer4.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton4.setEnabled(True)
            self.loaded4 = 1
            
        if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer4.pause()
        else:
            self.mediaPlayer4.play()
 
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

    def NoteValue(self):

        condval = self.spin_b.value()

    def changedValue(self):
        val = float(self.DialCond.value())/100
        self.LineforDisplay.setText(str(val)+ "e-3omh^-1cm^2")

    def validate(self):

        try:
            k = float(self.ConLine.text())
            if(k<0.45 or k>0.55):
               self.UseLab.setText("Wrong ! it's 0.5. Anyways continue")
            else :
                self.UseLab.setText("Correct ! it's 0.5.")
        except:
            pass
    def validate2(self):
        
        for i, j in zip([self.spin_n4h , self.spin_n8h,self.spin_n16h, self.spin_n32h, self.spin_n64h],
                     [self.spin_n4n, self.spin_n8n, self.spin_n16n, self.spin_n32n, self.spin_n64n]):
            try:
                temp = float(i.value()) + float(j.value())
                
                if temp != 100 :
                    self.errorMessage()
                    return
            except:
                self.errorMessage()
                return
        self.CalculateConductivity()

    def CalculateConductivity(self):

        import math
        
        Ka = 1.75
        k = float(random.randint(100, 9999))
        error = k/10000
        Ka = Ka + error
        Ka = Ka/100000
        c1 = 0.00
        c2 = 0.00
        c3 = 0.00
        c4 = 0.00
        c5 = 0.00
        for i, j, z in zip([self.spin_n4h , self.spin_n8h,self.spin_n16h, self.spin_n32h, self.spin_n64h],
                     [self.spin_n4n, self.spin_n8n, self.spin_n16n, self.spin_n32n, self.spin_n64n],
                           [c1, c2, c3, c4, c5]):
            try:
                z = (float(self.ConLine.text())*float(j.value()))/(float(i.value()) + float(j.value()))
                
            except:
                self.errorMessage()
                return
                
        
        c1 = c1 + (float(random.randint(10, 200))/1000)
        c2 = c2 + (float(random.randint(10, 200))/1000)
        c3 = c3 + (float(random.randint(10, 200))/1000)
        c4 = c4 + (float(random.randint(10, 200))/1000)
        c5 = c5 + (float(random.randint(10, 200))/1000)
        alpha1 = (math.sqrt((Ka**2) + (4*c1*Ka))-Ka)/(2*c1)
        alpha2 = (math.sqrt((Ka**2) + (4*c2*Ka))-Ka)/(2*c2)
        alpha3 = (math.sqrt((Ka**2) + (4*c3*Ka))-Ka)/(2*c3)
        alpha4 = (math.sqrt((Ka**2) + (4*c4*Ka))-Ka)/(2*c4)
        alpha5 = (math.sqrt((Ka**2) + (4*c5*Ka))-Ka)/(2*c5)

        kappa1 = "%.3f" %(390.8*alpha1*c1)
        kappa2 = "%.3f" %(390.8*alpha2*c2)
        kappa3 = "%.3f" %(390.8*alpha3*c3)
        kappa4 = "%.3f" %(390.8*alpha4*c4)
        kappa5 = "%.3f" %(390.8*alpha5*c5)

        
        
        self.note_n4n.setText(str(kappa1)+"e-3")
        self.note_n8n.setText(str(kappa2)+"e-3")
        self.note_n16n.setText(str(kappa3)+"e-3")
        self.note_n32n.setText(str(kappa4)+"e-3")
        self.note_n64n.setText(str(kappa5)+"e-3")
import test_rc
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    if(x == 1):
        
        main_runner(app, user_dets)
