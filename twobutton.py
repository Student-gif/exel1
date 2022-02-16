from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TwoButton(QWidget):
    buttom1= None
    buttton2 = None
    def __init__(self, *args, **kwargs):
        
        super(TwoButton, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        self.buttton2=QPushButton()
        self.buttton2.setText("/\\")
        self.buttom1=QPushButton()
        self.buttom1.setText("\\/")
        lay.addWidget(self.buttton2)
        lay.addWidget(self.buttom1)
    

