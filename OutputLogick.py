import datetime
import csv
import json
from random import random
from datemodul import weeknum
def saveTocsv(lister,file):
    filename = file
    # 'output'+datetime.date.today().__str__()+'.csv'
    csv.register_dialect('my_dialect', delimiter=',', lineterminator="\r")

    with open(filename, mode="w", encoding='utf-8-sig') as w_file:
    
        file_writer = csv.writer(w_file, 'my_dialect')
    
        file_writer.writerow(["Group","StudInLesson","Day","Les","Aud","Week","Subg","Name","CafI","Subject","Subj_type","Date","Subj_CafID","PrepID","Themas","Substitution_Name","Substitution_PrepID","Substitution_Subject","Substitution_Subj_type","Substitution_Subj_CafID","Lesson_ID","Lesson_Num"])
        
        
        
        for i in range(len(lister)):
            lister[i].lesson = lister[i].lesson.replace(',',"")
            #lister[i].lesson = lister[i].lesson.replace(',',"")
            
            if ('/' in lister[i].group):
                h=lister[i].group.split("/")
                lister[i].group = h[0].replace('/',"")
                secondsubgroup = h[1].replace('/',"")
                if('/' in lister[i].lesson):
                    l = lister[i].lesson.split("/")[1]
                    lister[i].lesson = lister[i].lesson.split("/")[0]
                else:
                    l = lister[i].lesson
                if ('/' in lister[i].teacher):
                    h=lister[i].teacher.split("/")
                    lister[i].teacher = h[0].replace('/',"")
                    secondsubgroup = h[1].replace('/',"")
                    
                newDataforCsv = [secondsubgroup,0,lister[i].weekday,lister[i].lessonPlace,lister[i].auditory,lister[i].week,0,lister[i].teacher,15,l,"л.",lister[i].weekdate,15,lister[i].teacherId,'По теме занятия',"","","","","","",""]
                file_writer.writerow(newDataforCsv)
            #if ('/' in lister[i].lesson):
            #    lister[i].lesson = lister[i].lesson.replace('/',"")
            elif('/' not in lister[i].group):
                newDataforCsv = [lister[i].group,0,lister[i].weekday,lister[i].lessonPlace,lister[i].auditory,lister[i].week,0,lister[i].teacher,15,lister[i].lesson,"л.",lister[i].weekdate,15,lister[i].teacherId,'По теме занятия',"","","","","","",""]
                file_writer.writerow(newDataforCsv)