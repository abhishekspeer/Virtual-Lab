
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDial, QFormLayout, QGroupBox,QHeaderView, QSlider,QPushButton, QHBoxLayout, QTableWidget,QWidget, QVBoxLayout

class TableMod(QTableWidget):
    def __init__(self, row, column, parent= None):
        super().__init__(row, column, parent)
        ver = self.horizontalHeader()
        ver.setVisible(False)
        ver = self.verticalHeader()
        ver.setVisible(False)

    def resizing(self):
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def setAlignment(self):
        for i in range(0, self.columnCount):
            for j in range(0, self.rowCount):
                try:
                    self.cellWidget(i, j).setAlignment(Qt.AlignCenter)
                except:
                    pass
class PushButton(QPushButton):
    def __init__(self, label, Enb = True, parent=None):
        super().__init__(label, parent)
        self.setFont(QFont('Times'))
        self.setEnabled(Enb)

class FGroup():
    def __init__(self, GoW, parent=None):
        self.Flay = QFormLayout()
        self.Box = QGroupBox()
        if(GoW == "W"):
            self.Box = QWidget()

        self.Box.setLayout(self.Flay)

    def addWidgets(self, widgetLists):
        for i in widgetLists:
            if len(i) == 2:
                self.Flay.addRow(i[0], i[1])
            else:
                self.Flay.addRow(i[0])
            
class VoHGroup(QGroupBox):
    def __init__(self,VoH, parent=None):
        super().__init__(parent)
        self.VBOX = QVBoxLayout()
        if(VoH == "H"):
            self.VBOX = QHBoxLayout()
        self.setLayout(self.VBOX)

    def addWidgets(self, widgetList = []):
        for i in widgetList:
            self.VBOX.addWidget(i)

class VoHWidget(QWidget):
    def __init__(self,VoH, parent=None):
        super().__init__(parent)
        self.VBOX = QVBoxLayout()
        if(VoH == "H"):
            self.VBOX = QHBoxLayout()
        self.setLayout(self.VBOX)

    def addWidgets(self, widgetList = []):
        for i in widgetList:
            self.VBOX.addWidget(i)
        
class Dial(QDial):
    def __init__(self, lo = -100, hi = 100):
        super().__init__()
        self.setRange(lo, hi)
        self.setValue(0)
        self.setNotchesVisible(True)

class VolSlider(QSlider):
    def __init__(self, lo = -5000, hi = 0):
        super().__init__()
        self.setOrientation(Qt.Vertical)
        self.setMinimumWidth(10)
        self.setStyleSheet("QSlider {color : white;}")
        self.setRange(lo, hi)
        self.setAutoFillBackground(True)
        self.setValue(lo)
        self.setFocusPolicy(Qt.NoFocus)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setTickInterval(1)
        self.setEnabled(False)