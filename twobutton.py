from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TwoButton(QWidget):
    def __init__(self, *args, **kwargs):
        
        super(TwoButton, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)
        self.setLayout(lay)
      
        self.buttonmn = self.minusbtnF()
        self.buttonpl = self.plusbtnF()
        lay.addWidget(self.buttonpl)
        lay.addWidget(self.buttonmn)
    def plusbtnF(self):
        self.plusbtn=QPushButton()
        self.plusbtn.setText("/\\")
        return self.plusbtn
    def minusbtnF(self):
        self.minusbtn=QPushButton()
        self.minusbtn.setText("\\/")
        return self.minusbtn
        
