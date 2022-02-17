from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TwoButton(QWidget):
    button1= None
    button2 = None
    def __init__(self, *args, **kwargs):
        
        super(TwoButton, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        self.button2=QPushButton()
        self.button2.setText("/\\")
        self.button1=QPushButton()
        self.button1.setText("\\/")
        lay.addWidget(self.button2)
        lay.addWidget(self.button1)
    
  