import pickle

nummber_data = int(input('Mennyi adatot akar megadni: '))
data= []

for i in range(nummber_data):
    val = input(f'{i}.adat megadasa: ')
    data.append(val)

with open ('data.pickle', 'wb') as file:
    pickle.dump(data, file)
    