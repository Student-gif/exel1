from calendar import c
import csv
import datetime
import math
from operator import le
from pickle import NONE
import time
from pydantic import NoneBytes, NoneStr

days = [
    [1, 21],
    [22, 42],
    [43, 63],
    [64, 84],
    [85, 105],
    [106, 126]
]
week = 23
AUDIT = [1, 53]


class lesson():
    audit = ""
    teather = ""
    group = ""
    week = 0
    weak_day = 0
    num = 0
    dis = ""

    def __str__(self):
        return {
            "audit": self.audit,
            "teather": self.teather,
            "group": self.group,
            "week": self.week,
            "weak_day": self.weak_day,
            "dis": self.dis,
            "num": self.num
        }


with open('input.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    data = []
    for i, row in enumerate(reader):
        data.append(row)
        if i > 129:
            break

audits = []
for index, audit in enumerate(data[1]):
    if index > AUDIT[0] and index < AUDIT[1]:
        audits.append((index, audit))
week = data[0][0]


lessons = []
for ind_day, day in enumerate(days):
    for io, au in enumerate(audits):
        n = 0
        for index, row in enumerate(data):
            if index > day[1]:
                break
            if index > day[0]:
                cell = row[au[0]]
                if (index) % 3 != 2:
                    continue
                n += 1
                if cell != None and cell != '':
                    if('/' in cell):
                        les1 = lesson()

                        les1.group = au[1]
                        les1.teather = cell.split("/")[0].strip()
                        if('/' in data[index+1][au[0]]):
                            les1.audit = data[index+1][au[0]
                                                       ].split("/")[0].strip()
                        else:
                            les1.audit = data[index+1][au[0]].strip()
                        les1.dis = data[index+2][au[0]].strip()
                        les1.week = week
                        les1.weak_day = ind_day+1
                        les1.num = n

                        les2 = lesson()

                        les2.group = au[1]
                        les2.teather = cell.split("/")[1].strip()
                        if('/' in data[index+1][au[0]]):
                            les2.audit = data[index+1][au[0]
                                                       ].split("/")[1].strip()
                        else:
                            les2.audit = data[index+1][au[0]].strip()
                        les2.dis = data[index+2][au[0]].strip()
                        les2.week = week
                        les2.weak_day = ind_day+1
                        les2.num = n

                        lessons.append(les1)
                        lessons.append(les2)
                    else:
                        les = lesson()
                        les.group = data[index+1][au[0]].strip()
                        les.teather = cell.strip()
                        les.audit = au[1] 
                        les.dis = data[index+2][au[0]].strip()
                        les.week = week
                        les.weak_day = ind_day+1
                        les.num = n
                        lessons.append(les)
                        #print(les.__str__())

with open("outout.csv", "w", encoding='UTF-8') as file:
    file.write(
        'Group;Day;Les;Aud;Week;Subg;Name;CafID;Subject;Subj_type;Start;End;Subj_CafID;PrepID\n')
    for les in lessons:
        file.write(les.group+';'+les.num.__str__()+';'+les.weak_day.__str__()+';'+les.audit.replace(
            '- ', '-')+';'+les.week.__str__()+';'+les.teather+';;15;'+les.dis+';;-100;-100;0;0')
        file.write("\n")

#        {
#          "subject" : "Ветеринарно-санитарная экспертиза",
#          "type" : "л.",
#          "subgroup" : 0,
#          "time_start" : "13:30",
#          "time_end" : "15:00",
#          "time" : 4,
#          "week" : 6,
#          "date" : "4-10-2021",
#          "teachers" : [{
#            "teacher_name" : "ст. преп.Маринич Л.Р."
#          }],
#          "auditories" : [{
#            "auditory_name" : "2-5"
#          }]
#        }
#groups = []
#for g in audits:
#    js = {
#        "group_name": g[1],
#       "course": datetime.date.today().year-2000-int(g[1].split('-')[2]),
#        "days": [{
#            "weekday": 1,
#            "lessons": []
#        }, {
#            "weekday": 2,
#            "lessons": []
#        }, {
#            "weekday": 3,
#            "lessons": []
#        }, {
#            "weekday": 4,
#            "lessons": []
#        }, {
#            "weekday": 5,
#            "lessons": []
#        }, {
#            "weekday": 6,
#            "lessons": []
#        }]
#    }
#    if js not in groups:
#        groups.append(js)
#tims = [
#    ('08:00', '09:30'),
#    ('09:40', '11:10'),
#    ('11:30', '12:50'),
#    ('13:30', '15:00'),
#    ('15:10', '16:40'),
#    ('16:50', '18:20'),
#    ('18:30', '20:00'),
#    ('20:10', '21:40')
#]
#for g in groups:
#    for weekday in range(6):
#        for l in lessons:
#            if(l.group == g["group_name"]):
#                if(l.weak_day == weekday):
#                    t = tims[l.num]
#                    g["days"][weekday]["lessons"].append({
#                        "subject": l.dis,
#                        "type": "л.",
#                        "subgroup": 0,
#                        "time_start":  t[0],
#                        "time_end":  t[1],
#                        "time": l.num,
#                        "week": weekday+1,
#                        "date": "",
#                        "teachers": [{
#                            "teacher_name": l.teather
#                        }],
#                        "auditories": [{
#                            "auditory_name": l.audit.replace('- ', '-')
#                        }]
#                    })
#
#
#with open("outout.json", "w", encoding='UTF-8') as file:
#    js = {
#        "faculty_name": 'null',
#        "date_start": 'null',
#        "date_end": 'null',
#        "groups": [gr for gr in groups]
#    }
#    jsAll = {"faculties" : [js]}
#    file.write(jsAll.__str__().replace("'",'"'))
#