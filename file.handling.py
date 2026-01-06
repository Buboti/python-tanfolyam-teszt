import csv
from csv import DictReader

file_read = open('text.txt', 'r', encoding='utf-8')
print(file_read.read())
file_read.close()

with open('text.txt', 'r', encoding='utf-8') as var:
    print(var.read())

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write('alma\r\n')
    file.write('barack\r\n')
    file.write('citrom\r\n')

with open('text.txt', 'a', encoding='utf-8') as file:
    file.write('test\n')

with open('text.txt', 'r+', encoding='utf-8') as file:
    file.seek(6)
    file.write('###')

#with open ('nincs.txt', 'r+', encoding='utf-8') as file:
  #  print(file.read())

with open ('test.csv', 'r', encoding='utf-8') as file:
    var = csv.reader(file)
    print(var)
    for item in var:
        print(item)

print ('-'* 50)

with open ('test3.csv', 'r', encoding='utf-8') as file:
    var = csv.reader(file, delimiter=';')
    print(var)
    for item in var:
        print(item)

print ('-'* 50)

csv.register_dialect('valami', delimiter=';', quoting=csv.QUOTE_NONE)
with open ('test3.csv', 'r', encoding='utf-8') as file:
    var = csv.reader(file, dialect='valami')
    for item in var:
        print(item)

data= [
    [1,2,3,'cici'],
    ['egy','ketto','harom','negy']
]


