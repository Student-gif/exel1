from ctypes import alignment
from email.headerregistry import Group
from operator import gt
from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QFrame,QScrollArea
from PyQt5.QtCore import Qt
from TestPdfMaker import PDF
import filedio





class WorkWithData():
    timeDict = {1:"8:00-9:30",
                2:"9:40-11:10",
                3:"11:20-12:50",
                4:"13:30-15:00",
                5:"15:10-16:40",
                6:"16:50-18:20",
                7:"18:30-20:00",
                8:"20:00",
                9:"21:00"}
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
    
    def __init__(self,Time= None,Lesson=None,Audit=None, teacher=None, group= None, ViewMod = False, parent = None, ):
        super(CustomLine, self,).__init__(parent)
        lay = QHBoxLayout(self)
        self.setLayout(lay)
        i = -1
        def dry_func (MaximumWidth,MinimumWidth, Text, Alignment = Qt.Alignment):
            GoodLabel = QLabel(self,margin=10,)
            GoodLabel.setStyleSheet("border: 1px solid black;")
            GoodLabel.setMinimumWidth(MinimumWidth)
            if MinimumWidth != 160:
                GoodLabel.setMaximumWidth(MaximumWidth)
            if Alignment != None:
                    GoodLabel.setAlignment(Alignment)
            GoodLabel.setText(Text)
            lay.addWidget(GoodLabel)
            GoodLabel.setMaximumHeight(60)
        while i !=4:
            i+=1
            if i == 0:
                dry_func (84,85, str(Time), Alignment = Qt.AlignLeft)
            if ViewMod == False:
                if i == 1:
                    dry_func(1,160,str(Lesson),Alignment = Qt.AlignLeft)
                elif i == 2:
                    dry_func(85,80, teacher,None)
                elif i == 3:
                    dry_func(60,65, Audit,None)
            else:
                if i == 1:
                    dry_func(61,60, group,None)
                elif i == 2:
                    dry_func(1,160,Lesson,None)
                elif i == 3:
                    dry_func(80,85, Audit,None)
class CustomWindowLine(QWidget):
     def __init__(self,Time= None,Lesson=None,parent = None, ):
        super(CustomWindowLine, self,).__init__(parent)
        lay = QHBoxLayout(self)
        self.setLayout(lay)
        def dry_func (MinimumWidth, Text,MaximumWidth,):
            GoodLabel = QLabel(self,margin=10,)
            GoodLabel.setStyleSheet("border: 1px solid black;")
            GoodLabel.setMinimumWidth(MinimumWidth)
            if MinimumWidth != 160:
                GoodLabel.setMaximumWidth(MaximumWidth)
            else:
                GoodLabel.setStyleSheet("""
                  background-color: red;
        """)
            GoodLabel.setText(Text)
            lay.addWidget(GoodLabel)
            GoodLabel.setMaximumHeight(60)
        dry_func(83,Time,84)
        dry_func(160,Lesson,1)

            
class mainData(QWidget):
    PrintData = []
    SortedData = []
    def pdfmake(self):
        file = filedio.SaveFileManager.init(filedio.SaveFileManager,format=".pdf")
        PdfMaker = PDF()
        #TODO make better
        scan = self.PrintData
        PdfMaker.print_chapter(scan)
        PdfMaker.output(f"{file}")
        

    def __init__(self, parent = None,SortedData = [],SearchQuestion = None,viewmod = False):
        super(mainData, self,).__init__(parent)
        head = QLabel(self,text=str(SearchQuestion))
        lay = QVBoxLayout(self)
        self.setLayout(lay)
        lay.addWidget(head)

        
        self.PrintData.clear()
        
        for i in range(len(SortedData)):            
            DictData = WorkWithData().sorterS(data=SortedData,i=i)
            if i == 0:
                weekday = QLabel(self,text=DictData[4])
                weekday.setAlignment(Qt.AlignCenter)
                lay.addWidget(weekday)
                self.PrintData.append([DictData[4]])
            if SortedData[i].staticData.weekday > SortedData[i-1].staticData.weekday :     
                    weekday = QLabel(self,text=DictData[4])  
                    weekday.setAlignment(Qt.AlignCenter)         
                    lay.addWidget(weekday)
                    self.PrintData.append([DictData[4]])     

            WindowCount = SortedData[i].staticData.lessonPlace - SortedData[i-1].staticData.lessonPlace
            if WindowCount >=1:
                timeKey = SortedData[i-1].staticData.lessonPlace
                
                for i in range(WindowCount-1):
                    WindowWidget = CustomWindowLine(Time =WorkWithData().timeDict[timeKey+(i+1)],Lesson="ОКНО",)
                    lay.addWidget(WindowWidget)
            lay.addWidget(CustomLine(Time = DictData[0],Lesson=DictData[1],Audit=DictData[2],group=DictData[3],teacher=DictData[5],ViewMod=viewmod))
                

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
        if len(QuestionData) <=11:
            self.scrollArea.setWidget(mainData(SortedData=data,SearchQuestion= QuestionData,viewmod=False))
        else:
            self.scrollArea.setWidget(mainData(SortedData=data,SearchQuestion= QuestionData,viewmod=True))
        lay.addWidget(self.scrollArea)
        # lay.addWidget(mainData(SortedData=data,SearchQuestion= QuestionData))
        

