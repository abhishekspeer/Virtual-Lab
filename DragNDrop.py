from PyQt5.QtCore import QMimeData, Qt
from common import ImageLabel
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QSizePolicy

class MimeData(QMimeData):
    vol = 0
    con = 0
    name = "name"
    col = 0
    def __init__(self):
        super().__init__()
        
class DragLabel(ImageLabel):
    def __init__(self, label, imagePath, res=False, parent=None):
        super().__init__(label, imagePath, parent)
        self.con_ = 0
        self.name_ = label
        self.vol_ = 0
        self.col_ = 0
        self.res = res

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
            if(self.vol() == 0 and self.res == True):
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

class DropMap(ImageLabel):
    def __init__(self, label, imagePath, parent=None):
        super().__init__(label, imagePath, parent)
        self.setAcceptDrops(True)
        self.superWidget = parent

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        self.superWidget.dropEvent(event)
        event.acceptProposedAction()

class DropLabel(QLineEdit):
    def __init__(self, label, imagePath, parent=None):
        super().__init__(label, parent)
        self.setAcceptDrops(True)
        self.con_ = 0
        self.name_ = "name"
        self.loaded_ = False
        self.vol_ = 0
        self.col_ = 0

        self.setReadOnly(True)
        self.setMaximumHeight(0)
        self.setMaximumWidth(0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.LabelMap = DropMap("hello", imagePath, self)

    def getLabel(self):
        return self.LabelMap
    
    def setImage(self, imagePath):
        self.LabelMap.setImage(imagePath)

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
        pos = event.pos()
        self.setVol(event.mimeData().vol)
        self.setName(event.mimeData().name)
        self.setCon(event.mimeData().con)
        self.setCol(event.mimeData().col)
        self.setText(str(self.name()))
        event.acceptProposedAction()