
from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel

class PrintWindow(QWidget):

    def check(self,Data,i):
        Group = Data[i].staticData.weekday
        auditory = Data[i].staticData.lesson
        lessonPlace = Data[i].staticData.auditory
        return [Group,auditory,lessonPlace]
    def __init__(self, parent = None,Data = [],QuestionData = None):
        super(PrintWindow, self,).__init__(parent)
        Data = Data
        QuestionData = QuestionData
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        lay.addWidget(QLabel(self,text=str(QuestionData)))
        for i in range(len(Data)):
            self.data=self.check(Data,i)
            lay.addWidget(CustomLine(Time = self.data[0],Lesson=self.data[1],Audit=self.data[2]))

    


class CustomLine(QWidget):
        
    def __init__(self,Time= None,Lesson=None,Audit=None,parent = None):
        super(CustomLine, self,).__init__(parent)
        lay = QHBoxLayout(self)
        self.setLayout(lay)
        lay.addWidget(QLabel(self,text=str(Time)))
        lay.addWidget(QLabel(self,text=str(Lesson)))
        lay.addWidget(QLabel(self,text=str(Audit)))
