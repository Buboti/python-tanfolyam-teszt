import pickle

str1 = 'teszt'
dict1 = {'gyumolcs':'alma', 'zoldseg':'krumpli'}
tup = (31, 'valami', True)
list1 = [1, 2, 3, 4 ,5, 6]

with open('data2.pickle', 'wb') as file:
    pickle.dump(str1, file)
    pickle.dump(dict1, file)
    pickle.dump(tup, file)
    pickle.dump(list1, file)

with open('data2.pickle', 'rb') as file:
    v1 = pickle.load(file)
    v2 = pickle.load(file)
    v3 = pickle.load(file)
    v4 = pickle.load(file)
    print(v1)
    print(v2)
    print(v3)
    print(v4)