from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox,QDialog)
import os
import qdarkstyle
import sheets
import smtplib
#Old
x = 0
user_dets = []
k = 0
print("ALL MODULES IMPORTED")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        exe = sheets.Initialize()
        if(exe == 0):
            self.w = QMessageBox()
            self.w.setText("Failed to Login")
            self.w.setInformativeText("Unable to obtain token")
            self.w.setWindowTitle("Error")
            self.w.exec()
            exit(1)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(821, 555)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/login-form-design-02.jpg);\n"
"color:white;\n"
"background-repeat: no-repeat;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 120, 310, 41))
        #MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        #self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 150, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(331, 366, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("text-align: center;\n")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 400, 191, 27))
        self.textEdit_2.setEchoMode(QLineEdit.Password)
        #self.successLab = QtWidgets.QLabel(self.centralwidget)
        #self.successLab.setGeometry(QtCore.QRect(329, 434, 191, 26))
        font = QtGui.QFont('Times', 12)
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        #self.textEdit_2.setStyleSheet(" border-radius: 10px;\n"
#"color:white;\n"
#"\n"
#"")
        #self.textEdit_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_2.setFrame(True)
        self.textEdit_2.setFrame(True)
        self.textEdit_2.setObjectName("textEdit_2")
        #self.textEdit_2.editingFinished.connect(self.check_password)
        self.textEdit_2.returnPressed.connect(self.check_password)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(278, 279, 59, 17))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(295, 462, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(403, 461, 169, 25))
        #self.pushButton_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.check_password)
        self.pushButton_2.clicked.connect(self.ForgotpasswordForm)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to VLAB"))
        self.label.setText(_translate("MainWindow", "VIRTUAL LABORATORY"))
        self.label_2.setText(_translate("MainWindow", "Virtual Chemistry Lab."))
        MainWindow.setWindowIcon(QtGui.QIcon('media/icon.ico'))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Forgot password..?"))
       

    def check_password(self):
        msg = QMessageBox()
        log_name = self.textEdit.text().strip()
        log_pass = self.textEdit_2.text().strip()
        if(log_name == '' or log_pass == ''):
            msg = QMessageBox()
            msg.setWindowTitle("No details")
            msg.setText("Missing password/userid\nEnter correct details")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        global k
        global user_dets
        login_status, user_dets, k = sheets.loginverify(log_name, log_pass)

        if login_status:
            if(user_dets == None):
                msg = QMessageBox()
                msg.setWindowTitle("ERROR")
                msg.setText("Invalid User")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
            else:
                global x
                x = 1
                app.closeAllWindows()

        else:
            msg.setText('Incorrect Password/UserID')
            msg.setWindowTitle("Invaild !")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


    def ForgotpasswordForm(self):                                             
        self.w = ForgotpasswordForm()
        self.w.show()        

class ForgotpasswordForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Forgot password?')
        self.resize(400, 100)
    
        layout = QGridLayout()
        widget = QLabel("VLAB-Forget Password")
        #widget.setAlignment(Qt.AlignCe)
        #widget.setFont(QtGui.QFont('Times', 15))
        widget2 = QLabel("Forget Password")
        #widget2.setAlignment(Qt.AlignCenter)
        label_name = QLabel('<font size="5"> Name </font>')
        label_email = QLabel('<font size="5">User Id*</font>')
        #label_user = QLabel('<font size="4">Username*</font>')

        layout.addWidget(widget, 0, 0, 1, 3)
        #layout.addWidget(widget2, 1, 1)
        layout.addWidget(label_name, 2, 0, 1, 1)
        layout.addWidget(label_email, 3, 0, 1, 1)
        #layout.addWidget(label_user, 4, 0, 1, 1)

        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setFont(QtGui.QFont('Times', 12))
        self.lineEdit_name.setPlaceholderText('Please enter your name')

        layout.addWidget(self.lineEdit_name, 2, 1, 1, 3)
        
        self.lineEdit_email=QLineEdit()
        self.lineEdit_email.setFont(QtGui.QFont('Times', 12))
        self.lineEdit_email.setPlaceholderText('Please enter your userid')
        self.lineEdit_email.returnPressed.connect(self.forget_password)
        layout.addWidget(self.lineEdit_email, 3, 1, 1, 3)

        self.lineEdit_user=QLineEdit()
        self.lineEdit_user.setPlaceholderText('Please enter your username')
        
        #layout.addWidget(self.lineEdit_user, 4, 1, 1, 3)
        
        forgot_login = QPushButton('Send password')
        forgot_login.setFont(QtGui.QFont('Times', 12))
        forgot_login.clicked.connect(self.forget_password)
        layout.addWidget(forgot_login, 4, 1, 1, 2)
        self.setLayout(layout)


    def forget_password(self):
        
        if(self.lineEdit_email.text() == ''):
            msg = QMessageBox()
            msg.setWindowTitle("Missing details")
            msg.setText("Fields marked with * are required")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        else:
            user_details = sheets.fetchDetails(self.lineEdit_email.text())
            if(user_details == None):
                #print("No details")
                msg = QMessageBox()
                msg.setWindowTitle("Invalid")
                msg.setText("User Not Found")
                msg.setInformativeText("Provide valid UserID.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return

            else:
                sender='vlab.noreply@gmail.com'
                password='pssword'
                smtpserver=smtplib.SMTP("smtp.gmail.com",587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo
                smtpserver.login(sender,password)
                msg='Subject:Password for VLab\n'+'Hi '+self.lineEdit_name.text()+'\n\nCredentials for Vlab:\nUsername: '+user_details[0]+'\nPassword: '+user_details[1]+'\n\n Regards\nDepartment of chemistry'
                sent = smtpserver.sendmail(sender,user_details[2],msg)
                if(sent == {}):
                    msg=QMessageBox()
                    msg.setWindowTitle("Success")
                    msg.setText('Mail Sent')
                    msg.setInformativeText('Please check your inbox. Also check your spam folder')
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                    self.hide()
                else:
                    msg=QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText('Unable to send message')
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    #self.hide()
                smtpserver.close()
                return

import srcMain
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    if(x == 1):
        import DashBoard
        DashBoard.main(1, user_dets, k, sheets)
        print("returned to main script. Report a Bug")
        sys.exit(1)
