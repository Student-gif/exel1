
from calendar import weekday
from cgi import test
from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QFrame
from numpy import less

class WorkWithData():
    timeDict = {1:"8:00",
                2:"9:40",
                3:"11:10",
                4:"13:30",
                5:"15:10",
                6:"16:40"}
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
        while count !=6:
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


class PrintWindow(QWidget):
    
    def __init__(self, parent = None,Data = [],QuestionData = None):
        data = WorkWithData().structureBuilder(dataWeekList=Data)
        super(PrintWindow, self,).__init__(parent)
        head = QLabel(self,text=str(QuestionData))
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        lay.addWidget(head)
        for i in range(len(data)):
                       
            DictData = WorkWithData().sorterS(data=data,i=i)
            if data[i].staticData.weekday > data[i-1].staticData.weekday:
                lay.addWidget(QLabel(self,text=DictData[4]))
            
            lay.addWidget(CustomLine(Time = DictData[0],Lesson=DictData[1],Audit=DictData[2]))

    


class CustomLine(QWidget):
    def __init__(self,Time= None,Lesson=None,Audit=None,parent = None):
        super(CustomLine, self,).__init__(parent)
        lay = QHBoxLayout(self)
        self.setLayout(lay)
        
               
        for i in range(3):
            FuckUp = QLabel(self,margin=10,)
            FuckUp.setStyleSheet("border: 1px solid black;")
            if i == 0 or i ==2:
                FuckUp.setMaximumWidth(100)
            else:
                FuckUp.setMaximumWidth(240)
            FuckUp.setMaximumHeight(60)
            data = [Time,Lesson,Audit]
            FuckUp.setText(str(data[i])) 
            lay.addWidget(FuckUp)

