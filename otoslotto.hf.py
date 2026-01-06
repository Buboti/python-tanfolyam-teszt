import csv

with open ('otos.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    last5colums= []
    for row in reader:
        try:
            numbers = [int(x) for x in row[-5:]]
            last5colums.append(numbers)
        except ValueError:
            pass

from collections import Counter

most_common_numbers = []

for col in range (5):
    column_values= [row[col] for row in last5colums]
    counter = Counter(column_values)
    most_common= counter.most_common(1)[0][0]
    most_common_numbers.append(most_common)

print( 'Az egyes oszlopok legyakoribb szamai sorban: ', most_common_numbers)

all_numbers =[]
for row in last5colums:
    all_numbers.extend(row)
from collections import Counter
counter = Counter(all_numbers)
top5 = counter.most_common(10)
print("Top 10 leggyakoribb szám (szám, előfordulás):", top5)

all_numbers =[]
for row in last5colums:
    all_numbers.extend(row)
from collections import Counter
counter = Counter(all_numbers)
rarest5 =sorted(counter.items(), key=lambda x: x[1])[:10]
print('Top 10 legritkabb szám (szám, előfordulás): ', rarest5)


