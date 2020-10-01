# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import smtplib
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox,QDialog)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 120, 310, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 150, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(331, 366, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(" border-radius: 10px;\n"
"color:white;\n"
"text-align: center;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 400, 191, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(" border-radius: 10px;\n"
"color:white;\n"
"\n"
"")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(278, 279, 59, 17))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(295, 462, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(403, 461, 169, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(238, 238, 236);")
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
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Forgot password..?"))
       

    def check_password(self):
        msg = QMessageBox()
        
        if self.textEdit.toPlainText() == 'Chemdept' and self.textEdit_2.toPlainText() == '1234':
            msg.setText('Success')
            msg.exec_()
            app.quit()
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
        password='pandey123'
        smtpserver=smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(sender,password)
        msg='Subject:Password of Online chemistry\n'+'Hi '+self.lineEdit_name.text()+'\n Username: Chemdept\nPassword: 1234\n\n regards\nDepartment of chemistry'
        smtpserver.sendmail(sender,receiver,msg)
        msg=QMessageBox()
        smtpserver.close()
        msg.setText('Mail Sent')
        msg.exec_()
        self.hide()


import test_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
