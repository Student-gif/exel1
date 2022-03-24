import csv
class importer():

    def DBimport():
        with open('Имя.csv', 'r',encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            dataList = []
            for row in reader:
                dataList.append(row[0].split('\t'))
            return dataList
