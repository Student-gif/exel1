from tkinter import Button
import win32clipboard
from OutputLogick import saveTocsv
from QListenW import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from OutputLogick import saveTocsv
import Logick
lister =[]
layout = QHBoxLayout()
columns =len(Logick.Auditories)
  
 
class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
      
    def initUI(self):
                 # Установить заголовок и начальный размер
        self.setWindowTitle('Ядро Расписание')
        
       
        self.tableWidget = QTableWidget(43,columns)
        #ширина ячеек
        for i in range(43):
            self.tableWidget.setRowHeight(i,80)

        # Установить горизонтальный заголовок таблицы
        for i in range(2,columns):
            self.tableWidget.setColumnWidth(i,80)
        # отрисовка окна индикации
        self.tableWidget.setColumnWidth(1,60)
        self.tableWidget.setColumnWidth(0,40)
        self.tableWidget.setSpan(0,0,1,2)
        #кнопка
        
        
        btn = QPushButton("Some button")
        self.tableWidget.setCellWidget(0, 0, btn)
        btn.clicked.connect(self.giveData)
        
        
        thing1 = 1  
        # конфигурация колон таблицы
        weekdays = ['п\nо\nн\nе\nд\nе\nл\nь\nн\nи\nк','в\nт\nо\nр\nн\nи\nк','с\nр\nе\nд\nа','ч\nе\nт\nв\nе\nр\nг','п\nя\nт\nн\nи\nц\nа','С\nу\nб\nб\nо\nт\nа']        
        for i in range(6):
            self.tableWidget.setSpan(thing1,0,7,1)
            self.tableWidget.setItem(thing1, 0, QTableWidgetItem())
            self.tableWidget.item(thing1,0).setText(weekdays[i])
            self.tableWidget.item(thing1,0).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
            self.tableWidget.item(thing1,0).setFont(QFont("Arial", 16))
            self.tableWidget.item(thing1, 0).setBackground(QColor(0,160,0))      
            thing1 += 7
        #присвоение табличного виджета
        Logick.groupList
        lessonsPlace =0
        weekDay= 1
        #TODO счётчик дней недели и номера пары
        for i in range(2,columns):
            for g in range(1,43):
                if lessonsPlace>6:
                    lessonsPlace=0
                lessonsPlace+=1
                self.tableWidget.setCellWidget(g,i,QListensW(lessonData()))
                self.tableWidget.cellWidget(g,i).updateLess(lessonsPlace,weekDay, Logick.groupList[i-2] )
                if g%7==0:
                    weekDay+=1
                    if weekDay>6:
                        weekDay = 1

           
            
        #Конфигурации столбца с занятиями 
        for i in range(2,43,7):
            for j in range(0,7):              
                self.tableWidget.setItem(i+j-1, 1, QTableWidgetItem())
                self.tableWidget.item(i+j-1,1).setText(str(j+1))
                self.tableWidget.item(i+j-1,1).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
            
        #распаковка данных Аудитории с бд  
        h=[x[0] for x in Logick.Auditories]
        #конфигурация виджетов аудиторий
        for i in range(2,columns):
            self.tableWidget.setItem(0, i, QTableWidgetItem())
            self.tableWidget.item(0, i).setBackground(QColor(220,0,0)) 
            self.tableWidget.item(0, i).setText(h[i-2])
                 # Разрешить щелчок правой кнопкой мыши для создания меню
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                 # Привязать контекстное меню к функции слота generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        #инициализация таблицы
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        
        
                
        
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
            print(data)
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(data)
            win32clipboard.CloseClipboard()


        if action == item2:
            print ('Вы выбрали второй вариант, текущее содержание текста строки:',)
            #self.v = self.tableWidget.setCellWidget(index[0].row(),index[0].column(),QListensW(self.index2.staticData))
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            print(data)
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()
            
            w=self.tableWidget.cellWidget(index[0].row(),index[0].column())
            w.update(data)
                     
        if action == item3:
            print ('Вы выбрали третий вариант, текущее содержание текста строки:', )
            w=self.tableWidget.cellWidget(index[0].row(),index[0].column())
            w.uploadUi()
    
    
    def giveData(self):
        self.checker()
        for i in range(2,columns):
            for g in range(1,43):
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
        msg.setDetailedText("miror eror stroka: {faustrow},\n столбцы{faustcolumn},".format(faustrow=[x[0] for x in faust],faustcolumn= [(x[1],x[2]) for x in faust]))
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
  
        pname = 'QMessageBox'
        cname = 'QTextEdit'
        msg.setStyleSheet(
            """{} {} {{ background-color: white; color: black; font-family: Courier; }}""".format(pname, cname))
        msg.exec_()
        if msg.clickedButton()==QMessageBox.Ignore:
            pass 
    
    def checker(self,):
            faust = []
            button = QPushButton()
            button.setText("A Button")
            button.clicked.connect(self.logs_show) 
            itWas = False
            start= 2
            first= self.tableWidget
            second = self.tableWidget
            for y in range(1,43):
                first.item(y, 1).setBackground(QColor(255,255,255))
                for g in range(start,columns):
                    for h in range(start+g-1,columns): 
                        if itWas==False:
                            second.cellWidget(y,h).setBackgroundRole(9)
                            first.cellWidget(y,g).setBackgroundRole(9)
                            first.cellWidget(y,g).setAutoFillBackground(False)
                        
                        
                        if first.cellWidget(y,g).staticData.teacher==second.cellWidget(y,h).staticData.teacher and first.cellWidget(y,g).staticData.teacher !=''and g!=h:
                                itWas= True
                                print(y,g+1,h+1)
                                print(first.cellWidget(y,g).backgroundRole())
                               
                                faust.append((y,g+1,h+1))
                                first.cellWidget(y,g).setAutoFillBackground(True)
                                first.cellWidget(y,g).setBackgroundRole(111)
                                second.cellWidget(y,h).setAutoFillBackground(True)
                                second.cellWidget(y,h).setBackgroundRole(111)
                                first.item(y, 1).setBackground(QColor(220,0,0)) 
                               
                        
                               
                        if first.cellWidget(y,g).staticData.group==second.cellWidget(y,h).staticData.group and first.cellWidget(y,g).staticData.group !=''and g!=h:
                                first.cellWidget(y,g).setAutoFillBackground(True)
                                first.cellWidget(y,g).setBackgroundRole(QPalette.Dark)
                                second.cellWidget(y,h).setAutoFillBackground(True)
                                second.cellWidget(y,h).setBackgroundRole(QPalette.Dark)
                                first.item(y, 1).setBackground(QColor(220,0,0))
                                print(y,g+1,h+1,'group')
                                itWas= True
                    
                       
            if itWas==True:
                self.logs_show(y,faust=faust) 
            
                
                
            
                            


                    
    
app = QApplication(sys.argv)
example = Table()
example.show()
sys.exit(app.exec_())