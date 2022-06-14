from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QFrame,QScrollArea
from PyQt5.QtCore import Qt
from TestPdfMaker import PDF





class WorkWithData():
    timeDict = {1:"8:00-9:30",
                2:"9:40-11:10",
                3:"11:20-12:50",
                4:"13:30-15:00",
                5:"15:10-16:40",
                6:"16:50-18:20",
                7:"18:30-20:00",
                8:"20:00"}
    WeekDayDict = {1:"Понедельник",
                    2:"Вторник",
                    3:"Среда",
                    4:"Четверг",
                    5:"Пятница",
                    6:"Суббота"}
    # TODO make better
    def structureBuilder(self,dataWeekList):
        morestructData = []
        day = 0
        while day !=7:
            day += 1
            structuredata =[]
            for i in range(len(dataWeekList)):              
                if dataWeekList[i].staticData.weekday == day:
                    structuredata.append(dataWeekList[i])
            time = 0
            while time !=9:            
                    time +=1
                    for i in range(len(structuredata)):
                        if  structuredata[i].staticData.lessonPlace == time:
                            morestructData.append(structuredata[i]) 
        return morestructData
    
    def sorterS(self,data, i ):
        weekdayData = self.WeekDayDict[data[i].staticData.weekday]
        lesson = data[i].staticData.lesson
        lessonPlace = data[i].staticData.auditory
        groupName = data[i].staticData.group
        lessonTime = self.timeDict[data[i].staticData.lessonPlace]
        teacheName = data[i].staticData.teacher      
        return [lessonTime,lesson,lessonPlace,groupName,weekdayData,teacheName]
class CustomLine(QWidget):
    def __init__(self,Time= None,Lesson=None,Audit=None,parent = None):
        super(CustomLine, self,).__init__(parent)
        lay = QHBoxLayout(self)
        self.setLayout(lay)               
        for i in range(3):
            GoodLabel = QLabel(self,margin=10,)
            GoodLabel.setStyleSheet("border: 1px solid black;")
            data = [Time,Lesson,Audit]
            if i == 0:
                GoodLabel.setMaximumWidth(84)
                GoodLabel.setAlignment(Qt.AlignLeft)
            else:
                GoodLabel.setMinimumWidth(240)
                GoodLabel.setMaximumWidth(self.size().width()+240)
                GoodLabel.setAlignment(Qt.AlignLeft)
            if i == 2:
                GoodLabel.setMaximumWidth(60)
            GoodLabel.setMaximumHeight(60)
            
            GoodLabel.setText(str(data[i])) 
            lay.addWidget(GoodLabel)
class mainData(QWidget):
    PrintData = [["Понедельник"]]
    SortedData = []
    def pdfmake(self):
        PdfMaker = PDF()
        #TODO make better
        scan = self.PrintData
        PdfMaker.print_chapter(scan)
        PdfMaker.output("test.pdf")
        

    def __init__(self, parent = None,SortedData = [],SearchQuestion = None):
        super(mainData, self,).__init__(parent)
        head = QLabel(self,text=str(SearchQuestion))
        monday = QLabel(text="Понедельник",)
        monday.setAlignment(Qt.AlignCenter)
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        lay.addWidget(head)
        lay.addWidget(monday)
        
        self.PrintData.clear()
        
        for i in range(len(SortedData)):            
            DictData = WorkWithData().sorterS(data=SortedData,i=i)

            if SortedData[i].staticData.weekday > SortedData[i-1].staticData.weekday or SortedData[i].staticData.weekday == 6:
                
                weekday = QLabel(self,text=DictData[4])  
                weekday.setAlignment(Qt.AlignCenter)         
                lay.addWidget(weekday)
                self.PrintData.append([DictData[4]])     

            WindowCount = SortedData[i].staticData.lessonPlace - SortedData[i-1].staticData.lessonPlace
            if WindowCount >=1:
                timeKey = SortedData[i-1].staticData.lessonPlace
                for i in range(WindowCount-1):
                    lay.addWidget(CustomLine(Time =WorkWithData().timeDict[timeKey+(i+1)],Lesson="ОКНО",Audit=""),)
            lay.addWidget(CustomLine(Time = DictData[0],Lesson=DictData[1],Audit=DictData[2]))
                

            self.PrintData.append([DictData[0],DictData[1],DictData[2],DictData[5]])

        GiveDataButton = QPushButton(text="проверить")

        GiveDataButton.clicked.connect(self.pdfmake)

        lay.addWidget(GiveDataButton)
        
            

            
class PrintWindow(QWidget):
    def __init__(self, parent = None,Data = [],QuestionData = None):
        data = WorkWithData().structureBuilder(dataWeekList=Data)
        super(PrintWindow, self,).__init__(parent)
        lay = QVBoxLayout(self)
        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidget(mainData(SortedData=data,SearchQuestion= QuestionData))
        lay.addWidget(self.scrollArea)
        # lay.addWidget(mainData(SortedData=data,SearchQuestion= QuestionData))
        

