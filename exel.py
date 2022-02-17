import Converter
from tkinter import Button
import win32clipboard
from OutputLogick import saveTocsv
from QListenW import *
from twobutton import TwoButton
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import Logick
lister =[]
layout = QHBoxLayout()
columns =len(Logick.Auditories)
import filedio


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
    
    def initUI(self):
                 # Установить заголовок и начальный размер
        self.setWindowTitle('Ядро Расписание')
       
               
        self.tableWidget = QTableWidget(49,columns)
    
        #ширина ячеек
        for i in range(49):
            self.tableWidget.setRowHeight(i,80)
        # Установить горизонтальный заголовок таблицы
        for i in range(2,columns):
            self.tableWidget.setColumnWidth(i,120)
        # отрисовка окна индикации
        self.tableWidget.setColumnWidth(1,20)
        self.tableWidget.setColumnWidth(0,40)
           
        thing1 = 1  
        # конфигурация колон таблицы
        weekdays = ['п\nо\nн\nе\nд\nе\nл\nь\nн\nи\nк','в\nт\nо\nр\nн\nи\nк','с\nр\nе\nд\nа','ч\nе\nт\nв\nе\nр\nг','п\nя\nт\nн\nи\nц\nа','С\nу\nб\nб\nо\nт\nа']        
        for i in range(6):
            self.tableWidget.setSpan(thing1,0,8,1)
            self.tableWidget.setItem(thing1, 0, QTableWidgetItem())
            self.tableWidget.item(thing1,0).setText(weekdays[i])
            self.tableWidget.item(thing1,0).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
            self.tableWidget.item(thing1,0).setFont(QFont("Arial", 16))
            self.tableWidget.item(thing1, 0).setBackground(QColor(0,160,0))      
            self.tableWidget.item(thing1, 0).setFlags(Qt.NoItemFlags|Qt.ItemIsEnabled)
            thing1 += 8
        #присвоение табличного виджета
        Logick.groupList
        lessonsPlace =0
        weekDay= 1
      
        for i in range(2,columns):
            for g in range(1,49):
                if lessonsPlace>7:
                    lessonsPlace=0
                lessonsPlace+=1
                self.tableWidget.setCellWidget(g,i,QListensW(lessonData()))
                self.tableWidget.cellWidget(g,i).updateLess(lessonsPlace,weekDay, Logick.groupList[i-2] )
                if g%8==0:
                    weekDay+=1
                    if weekDay>6:
                        weekDay = 1
                self.tableWidget.cellWidget(g,i).setdateweekday()
      
        #Конфигурации столбца с занятиями 
        for i in range(2,49,8):
            for j in range(0,8):              
                self.tableWidget.setItem(i+j-1, 1, QTableWidgetItem())
                self.tableWidget.item(i+j-1,1).setText(str(j+1))
                self.tableWidget.item(i+j-1,1).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
                self.tableWidget.item(i+j-1,1).setFlags(Qt.NoItemFlags|Qt.ItemIsEnabled)
                #конфигурация вертикального хедера
                header_item = QTableWidgetItem(str(j+1))
                self.tableWidget.setVerticalHeaderItem(i+j-1,header_item)
        #распаковка данных Аудитории с бд  
        h=[x[0] for x in Logick.Auditories]
        #конфигурация виджетов аудиторий
        for i in range(2,columns):
            self.tableWidget.setItem(0, i, QTableWidgetItem())
            self.tableWidget.item(0, i).setBackground(QColor(220,0,0)) 
            self.tableWidget.item(0, i).setText(h[i-2])
            self.tableWidget.item(0, i).setFlags(Qt.NoItemFlags|Qt.ItemIsEnabled)
              #конфигурация горизонтального хедера таблицы
            header_item = QTableWidgetItem(h[i-2])
            self.tableWidget.setHorizontalHeaderItem(i,header_item)
      
       
        
           
            
        
                 # Разрешить щелчок правой кнопкой мыши для создания меню
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                 # Привязать контекстное меню к функции слота generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        #инициализация таблицы
        layout.addWidget(self.tableWidget)
        ##
        ## меню бар для импорта
        menu_bar = QMenuBar()
        menu_file = menu_bar.addMenu('menu')
        action_exit = menu_file.addAction('взять csv')
        action_save = menu_file.addAction('Сохранить')
        action_change = menu_file.addAction('неделю назад')
        action_changeNext = menu_file.addAction('неделю вперед')

        action_exit.triggered.connect(self.importxl)
        action_save.triggered.connect(self.giveData)
        action_changeNext.triggered.connect(self.nextweek)
        action_change.triggered.connect(self.previusweek)
        

        layout.setMenuBar(menu_bar)
        ##/////////////
        ##
    
        self.setLayout(layout)
        self.weeknumCheck()
        #кнопки
        btn = TwoButton()
        self.tableWidget.setCellWidget(0,1,btn)
        butup=btn.button1
        butdow=btn.button2 
        butup.clicked.connect(self.previusweek)
        butdow.clicked.connect(self.nextweek)
        #диалог файловый
      
        
    def generateMenu(self, pos):
    
        menu = QMenu()
        item1 = menu.addAction (u'копировать')
        item2 = menu.addAction (u'вставить')
        item3 = menu.addAction (u'закрыть')
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
                         # Показать текст данных выбранной строки
        # копипаста 
        index = self.tableWidget.selectedIndexes()
        if action == item1:
            
            #self.indexData = self.tableWidget.cellWidget(index[0].row(),index[0].column())
            addToClipBoard = self.tableWidget.cellWidget(index[0].row(),index[0].column()).staticData
            data = addToClipBoard.teacher+';'+addToClipBoard.lesson+';'+addToClipBoard.group
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(data)
            win32clipboard.CloseClipboard()


        if action == item2:
            #self.v = self.tableWidget.setCellWidget(index[0].row(),index[0].column(),QListensW(self.index2.staticData))
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()
            
            w=self.tableWidget.cellWidget(index[0].row(),index[0].column())
            
            if data != None:
                w.update(data)
            else:
                data = ""
                pass
            
                     
        if action == item3:
            w=self.tableWidget.cellWidget(index[0].row(),index[0].column())
            w.uploadUi()
    
    
    def giveData(self):
        lister.clear()
        self.checker()
        for i in range(2,columns):
            for g in range(1,49):
                cel =self.tableWidget.cellWidget(g,i).real()
                if cel.lesson!='':
                    lister.append(cel)
      

        saveTocsv(lister)
#Анализ на совпадения   
   
   
    def logs_show(self,y,faust):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(' "Ошибка "')
        msg.setInformativeText('Совпали ячейки',)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Ignore,)
        msg.setDetailedText("miror eror строка: {faustrow},\n столбцы{faustcolumn},".format(faustrow=[x[0] for x in faust],faustcolumn= [(x[1],x[2]) for x in faust]))
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
  
        pname = 'QMessageBox'
        cname = 'QTextEdit'
        msg.setStyleSheet(
            """{} {} {{ background-color: white; color: black; font-family: Courier; }}""".format(pname, cname))
        
        if msg.exec_()==QMessageBox.Ignore:
                faustrow=[x[0] for x in faust]
                faustcolumn= [x[1]for x in faust]
                faustcolumn2= [x[2] for x in faust]
                for i in faustrow:
                    self.tableWidget.item(i,1).setBackground(QColor(255,255,255))
                    for g in faustcolumn:
                        self.tableWidget.cellWidget(i,g-1).setBackgroundRole(9)
                        self.tableWidget.cellWidget(i,g-1).setAutoFillBackground(False)
                        for h in faustcolumn2:
                           
                            
                            self.tableWidget.cellWidget(i,h-1).setBackgroundRole(9)
                            self.tableWidget.cellWidget(i,h-1).setAutoFillBackground(False)
                            

      
    def checker(self,):
            faust = []
            
            itWas = False
            start= 2
            first= self.tableWidget
            second = self.tableWidget
            for y in range(1,49):
                first.item(y, 1).setBackground(QColor(255,255,255))
                for g in range(start,columns):
                    for h in range(start+g-1,columns): 
                        if itWas==False:
                            second.cellWidget(y,h).setBackgroundRole(9)
                            first.cellWidget(y,g).setBackgroundRole(9)
                            first.cellWidget(y,g).setAutoFillBackground(False)
                        
                        
                        if first.cellWidget(y,g).staticData.teacher==second.cellWidget(y,h).staticData.teacher and first.cellWidget(y,g).staticData.teacher !=''and g!=h:
                                itWas= True
                               
                                faust.append((y,g+1,h+1))
                                first.cellWidget(y,g).setAutoFillBackground(True)
                                first.cellWidget(y,g).setBackgroundRole(14)
                                second.cellWidget(y,h).setAutoFillBackground(True)
                                second.cellWidget(y,h).setBackgroundRole(14)
                                first.item(y, 1).setBackground(QColor(220,0,0)) 
                               
                        
                               
                        if first.cellWidget(y,g).staticData.group==second.cellWidget(y,h).staticData.group and first.cellWidget(y,g).staticData.group !=''and g!=h:
                                itWas= True
                                faust.append((y,g+1,h+1))
                                first.cellWidget(y,g).setAutoFillBackground(True)
                                first.cellWidget(y,g).setBackgroundRole(15)
                                second.cellWidget(y,h).setAutoFillBackground(True)
                                second.cellWidget(y,h).setBackgroundRole(15)
                                first.item(y, 1).setBackground(QColor(220,0,0))
                              
                    
                       
            if itWas==True:
                self.logs_show(y,faust=faust) 
    #импорт exl 
    def importxl(self):
        widget= self.tableWidget
        self.file = filedio.filemanger.init(filedio.filemanger)
        self.lessons =  Converter.openFFFF( self.file)
        print (self.file)
        for l in self.lessons:
            for i in range(2,columns):
                for g in range(1,49):
                    if widget.cellWidget(g,i).staticData.auditory == l.audit.replace('- ', '-') and widget.cellWidget(g,i).staticData.lessonPlace == l.num and  widget.cellWidget(g,i).staticData.weekday ==  l.weak_day:
                        widget.cellWidget(g,i).helptoimport(teacher=l.teather,group=l.group,lesson=l.dis)
        
                    #print(widget.cellWidget(g,i).staticData.auditory,l.audit.replace('- ', '-'))
#    def takesafe(self):




    def weeknumCheck(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem())

        self.tableWidget.item(0, 0).setText("номер недели "+self.tableWidget.cellWidget(6,6).staticData.week.__str__())      
      
        self.tableWidget.item(0, 0).setFlags(Qt.NoItemFlags|Qt.ItemIsEnabled)
   # def initFileDialog(self):
   #    filedia=QFileDialog
   #    filename= filedia.getOpenFileName(self,'open',filter='exel files (*.csv)')
   #    inputFilename = filename
    #    return filename[0]   
    #    
#
#

    def nextweek(self):
          for i in range(2,columns):
            for g in range(1,49):
                self.tableWidget.cellWidget(g,i).updateDateWeekdate()
                self.weeknumCheck()
    def previusweek(self):
          for i in range(2,columns):
            for g in range(1,49):
                self.tableWidget.cellWidget(g,i).degadeweekDate()
                self.weeknumCheck()

                    
    
app = QApplication(sys.argv)
example = Table()
example.show()
sys.exit(app.exec_())