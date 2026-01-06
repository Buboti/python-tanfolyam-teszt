 # for ciklusvaltozo in kollekcio:
 #    CM

list1= [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in list1:
    if item %2 == 0:
     print(item)

sum = 0
for item in list1:
    sum = item + sum
print('Az osszeg: ' + str(sum))

for item in 'Ez egy szoveg':
    print(item)

t1 = (1, 2, 3, 4)
for t in t1:
    print(t)

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

for (t1, t2) in list2:
    print('Elso ertek: ' + str(t1))
    print('Masodik ertek: ' + str(t2))

dic1 = {'k1': 1, 'k2': 2, 'k3': 3}
for (k, v) in dic1.items():
    print(k)
    print(v)
    
for val in dic1.values():
    print(val)
