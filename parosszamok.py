import sys
import os

user_input = ''
count_loop = 0
while not user_input.isdigit():
    os.system('cls' if os.name == 'nt' else 'clear')
    if count_loop > 0:
        print(' rossz input, csak szamot adjon meg')
    user_input = input('irjon be szamokat vagy exit: ')
    if user_input.lower() == 'exit':
        sys.exit('fuck you hibas adat, kilepes')
    count_loop += 1

odd_list= []
even_list= []

for i in user_input:
    if int(i) %2 == 0 and i not in even_list:
        even_list.append(i)
    elif int(i) %2 != 0 and i not in odd_list:
        odd_list.append(i)

if not even_list:
    print('Nincs paros szam a bevitelben')
else:
    if len(even_list) == 1:
        print('A paros szam a bevitelben: %s' % even_list[0])
    else:
        print('A paros szamok a bevitelben: %s' % even_list)

if not odd_list:
    print('Nincs paros szam a bevitelben')
else:
    if len(even_list) == 1:
        print('A paratlan szam a bevitelben: %s' % odd_list[0])
    else:
        print('A paratlan szamok a bevitelben: %s' % odd_list)