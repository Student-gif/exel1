import csv
import json
from random import random
from datemodul import weeknum
def saveTocsv(lister):
    filename = str(random())+'.csv'
    csv.register_dialect('my_dialect', delimiter=',', lineterminator="\r")

    with open(filename, mode="w", encoding='utf-8') as w_file:
    
        file_writer = csv.writer(w_file, 'my_dialect')
    
        file_writer.writerow(["Group","StudInLesson","Day","Les","Aud","Week","Subg","Name","CafI","Subject","Subj_type","Date","Subj_CafID","PrepID","Themas","Substitution_Name","Substitution_PrepID","Substitution_Subject","Substitution_Subj_type","Substitution_Subj_CafID","Lesson_ID","Lesson_Num"])
        
        
        
        for i in range(len(lister)):
            newDataforCsv = [lister[i].group,0,lister[i].weekday,lister[i].lessonPlace,lister[i].auditory,weeknum,0,lister[i].teacher,15,lister[i].lesson,"л.",lister[i].weekdate,15,lister[i].teacherId,'По теме занятия',"","","","","","",""]
            file_writer.writerow(newDataforCsv)

            
            