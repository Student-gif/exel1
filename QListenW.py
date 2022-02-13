from calendar import weekday
from datetime import date, datetime, timedelta
from Logick import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

    
class lessonData():
    teacher: str = ""
    group:str = ""
    lesson:str = ""
    week: int = -1
    weekday: int = -1
    teacherId:int = -1
    lessonPlace:int = 0
    auditory:int = 0
    weekdate:date= date.today()
    
    def notCopyData(self,lessonPlace,WeekDay,auditory,):
        self.auditory = auditory
        self.lessonPlace = lessonPlace
        self.weekday = WeekDay
        return True
    def updateTeacherId(self,teacherId):
        self.teacherId = teacherId
        return True
    def updatecopydata(self,data):

        ar=data.split(';')
        self.teacher=ar[0]
        self.group =ar[1]
        self.lesson=ar[1]
        return True
    def updateWeekDate(self,dateweekday):
        self.weekdate=dateweekday
    def __str__(self) -> str:
        return f'{self.teacher.__str__()};{self.group.__str__()};{self.lesson.__str__()};{self.week.__str__()};{self.weekday.__str__()};{self.teacherId.__str__()};{self.lessonPlace.__str__()};{self.lessonPlace.__str__()};{self.auditory.__str__()};{self.weekdate.__str__}'

        


class QListensW(QWidget):
    
    staticData = lessonData

    def __init__(self,staticData, *args, **kwargs):
        self.staticData=staticData
        super(QListensW, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)



        self.setLayout(lay)
        self.lineEditTeacher = QLineEdit()
      
        self.lineEditGroups = QLineEdit()
        self.lineEditLesson = QLineEdit()
                  
        completerTeacher = QCompleter([s[0].__str__() for s in Prepods], self.lineEditTeacher)
        completerGroup = QCompleter([s[0].__str__() for s in Groups], self.lineEditGroups)
        completerLesson = QCompleter([s[0].__str__() for s in Lessons], self.lineEditLesson)

    

        self.lineEditTeacher.setCompleter(completerTeacher)
        self.lineEditGroups.setCompleter(completerGroup)
        self.lineEditLesson.setCompleter(completerLesson)     
        
        lay.addWidget(self.lineEditTeacher)
        lay.addWidget(self.lineEditLesson)
        lay.addWidget(self.lineEditGroups)

        self.lineEditLesson.editingFinished.connect(self.CustomEventEnter)
        self.lineEditTeacher.editingFinished.connect(self.CustomEventEnter)
        self.lineEditGroups.editingFinished.connect(self.CustomEventEnter)

        self.uploadUi()
    #забирает данные
    def real(self):
        return self.staticData
    def update(self,data):
        self.staticData.updatecopydata(data)
        self.uploadUi()

    def uploadUi(self):
        self.lineEditTeacher.setText(self.staticData.teacher)
        self.lineEditGroups.setText(self.staticData.group)
        self.lineEditLesson.setText(self.staticData.lesson)
    def helptoimport(self,teacher,group,lesson):
        self.lineEditTeacher.setText(teacher)
        self.lineEditGroups.setText(group)
        self.lineEditLesson.setText(lesson)
    
    def CustomEventEnter(self):
        self.staticData.group = self.lineEditGroups.text()
        self.staticData.teacher = self.lineEditTeacher.text()
        self.staticData.lesson = self.lineEditLesson.text()
        try:
            self.staticData.updateWeekDate(self.setdateweekday())
            self.staticData.updateTeacherId(IdTeachAddic[self.staticData.teacher])
        except:
            self.staticData.group = self.lineEditGroups.text()
            self.staticData.lesson = self.lineEditLesson.text()
            self.staticData.teacher = self.lineEditTeacher.text()
    def setdateweekday(self):
        startday = date.weekday(date.today())
        controlday =  self.staticData.weekday
        startweek = date.today()-timedelta(days=startday)
        if controlday >= startday:
            dateweekday=startweek + timedelta(controlday-1)
        elif controlday <= startday:
            dateweekday=startweek + timedelta(controlday-1)
            
        else:
            pass
       
        

        
        dateweekday=dateweekday.strftime("%m.%d.%Y")
        return dateweekday



    def updateLess(self,lessonplace,weekDay,audit):
       
        self.staticData.notCopyData(lessonplace,weekDay,audit)

  