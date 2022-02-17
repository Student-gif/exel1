from tkinter.messagebox import NO
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class FileDiolog(QWidget):
        filedioObj = None
        filename =None
        def __init__(self, *args, **kwargs):
            self.filedio=QFileDialog()
            super(FileDiolog, self).__init__(*args, **kwargs)
            self.filedioObj = self.filedio
            
class filemanger():
    fild = None
    def init(self):  
        self.fild = FileDiolog()
        return self.fild.filedioObj.getOpenFileName(filter='exel files (*.csv)')[0]

