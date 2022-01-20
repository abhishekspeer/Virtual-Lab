from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QLabel, QStyle, QMessageBox, QTabWidget, QSlider,QPushButton, QHBoxLayout,QWidget, QVBoxLayout, QScrollArea, QSizePolicy, QPlainTextEdit
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from ModWidgets import VoHGroup, VoHWidget
import os
import sys

from PyQt5.QtGui import QFont, QPixmap

class ImageLabel(QLabel):
    def __init__(self, label, imagePath="", parent=None):
        super().__init__(label, parent)
        self.setImage(imagePath)
        self.setFont(QFont('Times'))

    def setImage(self, imagePath):
        if(imagePath != ""):
            Temp = EXP_PAGE.resource_path(self, imagePath)
            self.setPixmap(QPixmap(Temp))
        self.setAlignment(Qt.AlignCenter)

class EXP_BUTTON(QPushButton):
    def __init__(self, label, stack, title, expClassWid, parent):
        super().__init__(label, parent)
        self.stack = stack
        self.exp1Inst = 0
        self.title = title
        self.expWid = expClassWid
        self.clicked.connect(self.LaunchExp)
        self.parentEx = parent

    def LaunchExp(self):
        if(self.exp1Inst == 0):
            self.exp1Inst = 1
            self.stack.addWidget(self.expWid)
        self.stack.setCurrentWidget(self.expWid)
        self.parentEx.setWindowTitle(self.title)
            
class EXP_PAGE(QTabWidget):
    def __init__(self, imageList, VideoPath, stack):
        super().__init__()
        self.tab1 = VoHWidget("V")
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = VoHGroup("V")
        #self.tabs.resize(300,200)
        # Add tabs
       # stack = QStackedLayout
        backbutton = QPushButton(" BACK ")
        self.setCornerWidget(backbutton, Qt.TopLeftCorner)
        def goBackToDef():
            stack.setCurrentIndex(0)

        backbutton.clicked.connect(goBackToDef)

        self.addTab(self.tab1," Theory ")
        self.addTab(self.tab2," Perform ")
        
        #self.addTab(self.tab3, " Video ")
        #self.addTab(self.tab4," Question Bank ")
        self.otherPages(imageList, VideoPath)
        self.dataGEN = []
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    def otherPages(self, imageList=[], VideoPath = " "):
        self.tab1Lay = VoHWidget("V")
        self.vPATH = VideoPath
        self.widgetList = []
        for i in imageList :
            temp = ImageLabel("the", i)
            temp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.tab1Lay.addWidgets([temp])
        
        self.scrollAr = QScrollArea()
        self.scrollAr.setWidget(self.tab1Lay)
        
        self.tab1.addWidgets([self.scrollAr])

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

        # Create layouts to place inside widget
        self.videoWidget = QVideoWidget()
        self.controlLayout = QHBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.addWidget(self.playButton)
        self.controlLayout.addWidget(self.positionSlider)
 
        # Set widget to contain window contents
        self.Video_widget = VoHWidget("V")
        
        self.Video_widget.addWidgets([self.videoWidget])
        self.Video_widget.VBOX.addLayout(self.controlLayout)
        self.Video_widget.addWidgets([self.errorLabel])
 
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.loaded1 = 0

        self.tab3Lay = QVBoxLayout()
        self.tab3Lay.addWidget(self.Video_widget)

        self.tab3.setLayout(self.tab3Lay)
        self.tab4text = QPlainTextEdit()
        self.tab4.addWidgets([self.tab4text])

    def play(self):
        
        fileName = self.resource_path(self, self.vPATH)
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


    def errorMessageM(self, type = QMessageBox.Critical, title = "Unknown Error", text = "Application Error! Report a bug?", textM = "UNKNOWN ERROR"):

        w = QMessageBox()
        w.setIcon(type)
        w.setText(textM)
        w.setInformativeText(text)
        w.setWindowTitle(title)
        w.exec()

    def getUnknowns(self):
        return self.dataGEN