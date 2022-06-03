import sys
from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout

class searchWindow(QWidget):
    searchLine = None
    searchButton = None
    colorbutton = None
    clearbutton = None
    def __init__(self, parent = None):
        super(searchWindow, self).__init__(parent)
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        
        
        self.searchLine  = QLineEdit()
        self.searchButton = QPushButton(self,text='search')
        self.clearbutton =  QPushButton(self,text='clear')
        lay.addWidget(self.searchLine)
        lay.addWidget(self.searchButton)
        lay.addWidget(self.clearbutton)
        


