import csv

def saveCsv(file):
    with open(file, encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=',')
            data = []
            for i, row in enumerate(reader):
                if i>=1:
                    data.append(row)
            print(data)
    return data