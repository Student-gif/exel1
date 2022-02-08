import csv
import json
def saveTocsv(lister):
    csv.register_dialect('my_dialect', delimiter=',', lineterminator="\r")
    
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    
        file_writer = csv.writer(w_file, 'my_dialect')
    
        file_writer.writerow(["Group","Day","Les","Aud","Week","Subg","Name","CafI","Subj","Subj_type","Start","Subj_CafI","PrepID"])
        
        
        
        for i in range(len(lister)):
            newDataforCsv = [lister[i].group,lister[i].weekday,lister[i].lessonPlace,lister[i].auditory,23,lister[i].teacher,"",15,lister[i].lesson,"",-100,100,lister[i].teacherId]
            file_writer.writerow(newDataforCsv)

            
            