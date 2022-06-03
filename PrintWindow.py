from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QFrame
from PyQt5.QtCore import Qt
from fpdf import FPDF





class WorkWithData():
    timeDict = {1:"8:00",
                2:"9:40",
                3:"11:10",
                4:"13:30",
                5:"15:10",
                6:"16:40",
                7:"18:20",
                8:"19:50"}
    WeekDayDict = {1:"пн",
                    2:"вт",
                    3:"ср",
                    4:"чт",
                    5:"пт",
                    6:"сб"}

    def structureBuilder(self,dataWeekList):
        structuredata =[]
        count = 1
        day = 0
        while count !=7:
            day += 1
            for i in range(len(dataWeekList)):
                if dataWeekList[i].staticData.weekday == day:
                    structuredata.append(dataWeekList[i])
            count+=1
        return structuredata


    
    def sorterS(self,data, i ):

        weekdayData = self.WeekDayDict[data[i].staticData.weekday]
        lesson = data[i].staticData.lesson
        lessonPlace = data[i].staticData.auditory
        groupName = data[i].staticData.group
        lessonTime = self.timeDict[data[i].staticData.lessonPlace]
        
        return [lessonTime,lesson,lessonPlace,groupName,weekdayData]
class CustomLine(QWidget):
    def __init__(self,Time= None,Lesson=None,Audit=None,parent = None):
        super(CustomLine, self,).__init__(parent)
        lay = QHBoxLayout(self)
        self.setLayout(lay)               
        for i in range(3):
            GoodLabel = QLabel(self,margin=10,)
            GoodLabel.setStyleSheet("border: 1px solid black;")
            if i == 0:
                GoodLabel.setMaximumWidth(49)
            else:
                GoodLabel.setMaximumWidth(240)
            if i == 2:
                GoodLabel.setMaximumWidth(60)
            GoodLabel.setMaximumHeight(60)
            data = [Time,Lesson,Audit]
            GoodLabel.setText(str(data[i])) 
            lay.addWidget(GoodLabel)
class mainData(QWidget):
    def __init__(self, parent = None,SortedData = [],SearchQuestion = None):
        super(mainData, self,).__init__(parent)
        head = QLabel(self,text=str(SearchQuestion))
        monday = QLabel(text="пн",)
        monday.setAlignment(Qt.AlignCenter)
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        lay.addWidget(head)
        lay.addWidget(monday)
        

        for i in range(len(SortedData)):         
            DictData = WorkWithData().sorterS(data=SortedData,i=i)
            if SortedData[i].staticData.weekday > SortedData[i-1].staticData.weekday or SortedData[i].staticData.weekday == 6:
                weekday = QLabel(self,text=DictData[4])  
                weekday.setAlignment(Qt.AlignCenter)         
                lay.addWidget(weekday)     
            lay.addWidget(CustomLine(Time = DictData[0],Lesson=DictData[1],Audit=DictData[2]))
        GiveDataButton = QPushButton(text="проверить")

        #GiveDataButton.clicked.connect( )
        lay.addWidget(GiveDataButton)
            

            
class PrintWindow(QWidget):
    def __init__(self, parent = None,Data = [],QuestionData = None):
        data = WorkWithData().structureBuilder(dataWeekList=Data)
        super(PrintWindow, self,).__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(mainData(SortedData=data,SearchQuestion= QuestionData))
        

