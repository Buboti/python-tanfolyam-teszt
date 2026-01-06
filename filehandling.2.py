import csv
from csv import DictReader, DictWriter

with open('test.csv', 'r', encoding='utf-8',newline='') as file:
    dict_reader = DictReader(file)
    for row in dict_reader:
        print(row['Gyumolcs'])

with open('test4.csv', 'r', encoding='utf-8',newline='') as file:
    header = ['Nev','Email','Lakhely']
    dic_writer = DictWriter(file, fieldnames=header, dialect='valami')
    dic_writer.writeheader()
    dic_writer.writerows({
        'Nev':'Gyumolcs',
        'Email':'Email',
        'Lakhely':'Lakhely'
    })


