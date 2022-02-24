from calendar import weekday
from datetime import date, datetime, timedelta
from Logick import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datemodul import weeknum
    
class lessonData():
    teacher: str = ""
    group:str = ""
    lesson:str = ""
    week: int = 0
    weekday: int = -1
    teacherId:int = 0
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
        self.group =ar[2]
        self.lesson=ar[1]
        print(ar)
        return True
    def updateWeekDate(self,dateweekday, newweek):
        self.week = newweek
        self.weekdate=dateweekday
    def updateImportData(self,teacher,group,lesson):
        self.teacher=teacher
        self.group =group
        self.lesson=lesson
        
    def __str__(self) -> str:
        return f'{self.teacher.__str__()};{self.group.__str__()};{self.lesson.__str__()};{self.week.__str__()};{self.weekday.__str__()};{self.teacherId.__str__()};{self.lessonPlace.__str__()};{self.lessonPlace.__str__()};{self.auditory.__str__()};{self.weekdate.__str__}'

        


class QListensW(QWidget):
    
    staticData = lessonData
   
    
    def __init__(self,staticData, *args, **kwargs):
        self.staticData=staticData
        super(QListensW, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)

        linestyle = "QLineEdit{border-radius: 10px;border-color: black;border-width:1px;border-style: outset;background:  #F2F2F2;}"
        self.setLayout(lay)
        self.lineEditTeacher = QLineEdit()
        fixheigt = 25
        self.lineEditGroups = QLineEdit()
        self.lineEditLesson = QLineEdit()
        self.lineEditGroups.setFixedHeight(fixheigt)
        self.lineEditLesson.setFixedHeight(fixheigt)
        self.lineEditTeacher.setFixedHeight(fixheigt)
        self.lineEditGroups.setStyleSheet(linestyle)
        self.lineEditLesson.setStyleSheet(linestyle)
        self.lineEditTeacher.setStyleSheet(linestyle)
        
                  
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
        self.staticData.updateImportData(teacher,group,lesson)

        try:
            self.staticData.updateTeacherId(IdTeachAddic[self.staticData.teacher])
        except:
            pass
    def CustomEventEnter(self):
        stackdata=[self.staticData.auditory,self.staticData.lessonPlace,self.staticData.weekday,self.staticData.teacher,self.staticData.group,self.staticData.lesson]
        self.staticData.group = self.lineEditGroups.text()
        self.staticData.teacher = self.lineEditTeacher.text()
        self.staticData.lesson = self.lineEditLesson.text()
        try:
            self.staticData.updateTeacherId(IdTeachAddic[self.staticData.teacher])
        except:
            self.staticData.group = self.lineEditGroups.text()
            self.staticData.lesson = self.lineEditLesson.text()
            self.staticData.teacher = self.lineEditTeacher.text()
        return stackdata
    def setdateweekday(self):
        
        startday = date.weekday(date.today())
        
        controlday =  self.staticData.weekday
        
        startweek = date.today()-timedelta(days=startday)
        if controlday >= startday:
            dateweekday=startweek + timedelta(controlday-1)
            dateweekday.strftime("%m.%d.%Y")
            self.staticData.updateWeekDate(dateweekday, weeknum)
        elif controlday <= startday:
            dateweekday=startweek + timedelta(controlday-1)
            dateweekday.strftime("%m.%d.%Y")
            self.staticData.updateWeekDate(dateweekday, weeknum)
            
        
        else:
            
            pass
      #TODO поправить даты  ??
    def updateDateWeekdate(self):
        nowdate=self.staticData.weekdate
        nowweek = self.staticData.week
        newweek = nowweek + 1
        if newweek <48:
            nextdate=nowdate+timedelta(7)
        
        if newweek>= 48:
            newweek=48
        self.staticData.updateWeekDate(nextdate, newweek)
     #TODO вернуть как было   
    def degadeweekDate(self):
        nowdate=self.staticData.weekdate
        nowweek = self.staticData.week
        newweek = nowweek -1
        #if newweek >0:
        nextdate=nowdate-timedelta(7)
        #else:
        #   pass
       #if newweek<= 0:
           # newweek=0

        self.staticData.updateWeekDate(nextdate, newweek)
       

    def updateLess(self,lessonplace,weekDay,audit):
        self.staticData.notCopyData(lessonplace,weekDay,audit)
    def changeTextGroup(self,color):
        #self.lineEditGroups.setStyleSheet(f"background: {color};")
        
        self.lineEditGroups.setStyleSheet(f"background: {color};border-radius: 10px;border-color: black;border-width:1px;border-style: outset;")
    def changeTextTeacher(self,color):
        self.lineEditTeacher.setStyleSheet(f"background: {color};border-radius: 10px;border-color: black;border-width:1px;border-style: outset;")
    