#unicode - 8
from fpdf import FPDF
class PDF(FPDF):
    
    def headerSculptor(self,deviation,txt,centr,fontSize):
        self.set_font("Sans", "", fontSize)
        self.set_x((210 - self.get_string_width(txt)+deviation) / centr)
    def HighHeading(self):
        #Оформляет заголовок
        #first Block text
        for i in ["Cочинский институт(филиал)","ФГАОУ ВО«Российский университет дружбы народов»"]:
            self.headerSculptor(6,i,2,12)
            self.cell(w = self.get_string_width(i), h=9, txt = i, align="C",ln=1)
    def SomeLowerHeading(self):
         from datetime import date
         #Second block text
         for i in ["УТВЕРЖДАЮ","Зам. директора по образовательной деятельности","________Т.В Мирошниченко",f"{date.today().day}.0{date.today().month}.{date.today().year}"]:
            self.set_font("Sans", "", 9)
            self.set_x(120)
            self.cell(txt=i,
                   h=5,align="C",
                   w = self.get_string_width(i),ln=1)
         self.ln(10)
    def LowerHeading(self):
        from datetime import date
        t = date.today().isocalendar()
        for i in ["РАСПИСАНИЕ",f"учебных занятий на ВЕСЕННИЙ СЕМЕСТР {date.today().year-1}-{date.today().year} учебного года",f"{date.today()}г. по {date.fromisocalendar(t.year,t.week+1,t.weekday)}.г"]:
            self.headerSculptor(6,i,2,9)
            self.cell(txt=i,
                   h=5,align="C",
                   w = self.get_string_width(i),ln=1)
    def header(self):
        """Оформление верхнего контитула каждого листа"""
        # Делает заголовок
        self.HighHeading()
        #Формат подписи
        self.SomeLowerHeading() 

        self.headerSculptor(6,"Отделение среднего профессианального образования",2,12)
        self.cell(txt="Отделение среднего профессианального образования",h=5,align="C",w = self.get_string_width("Отделение среднего профессианального образования"),)
        self.ln(10)
        self.LowerHeading()
        # Выполнение разрыва строки в 10 мм
        self.ln(8)

    def footer(self):
        """Оформление нижнего контитула каждого листа"""
        # Устанавливаем курсор на 1,5 см от нижнего края
        self.set_y(-15)
        # Настройка шрифта: Sans, italic, 8
        self.set_font("Sans", "", 8)
        # Установка цвета текста на серый:
        self.set_text_color(128)
        # вывод номера страницы
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def secTableData(self):
        self.cell(w=15,h=12, txt = "Время",align="C",)
        self.cell(w=115,h=12, txt = "Предмет",align="C",)
        self.cell(w=20,h=12, txt = "Кабинет",align="C",)
        self.cell(w=40,h=12, txt = "Преп",align="C",ln=1)

    def mainTable_Data(self,inputData):
        if len(inputData) != 1:
            self.cell(w=20,h=6, txt = str(inputData[0]),border=1,align="C",ln=0)
            self.cell(w=115,h=6, txt = str(inputData[1]),border=1,align="C",ln=0)
            self.cell(w=20,h=6, txt = str(inputData[2]),border=1,align="C",ln=0)
            self.cell(w=40,h=6, txt = str(inputData[3]),border=1,align="C",ln=1)
        else:
            self.cell(w=195,h=15, txt = str(inputData[0]),border=1,align="C",ln=1)
    

    def print_chapter(self,inputData):
        self.add_font("Sans", style="", fname="font/DejaVuSans.ttf", uni=True)
        self.add_page()
        self.secTableData()
        for i in inputData:
            print(i)
            self.mainTable_Data(i)