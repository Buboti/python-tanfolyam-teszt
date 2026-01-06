var = input('irjon be valamit: ')

if var.isalpha():
    print('A beirt szoveg csak betuket tartalmaz')
elif var.isnumeric():
    print('A beirt szoveg csak szamokat tartalmaz')
else:
    print('Mindent tartalmaz')


