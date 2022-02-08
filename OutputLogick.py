import csv
def saveTocsv(lister):
    csv.register_dialect('my_dialect', delimiter=';', lineterminator="\r")
    
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    
        file_writer = csv.writer(w_file, 'my_dialect')
    
        file_writer.writerow(["TeacherId", "lessNum", "weekday","teacher","group","lesson","Audit"])
    
        for i in lister:
    
            file_writer.writerow(i)