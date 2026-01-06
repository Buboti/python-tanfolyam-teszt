var = input('Irjon be egy szoveget: ')
count = 0
for character in var:
    if character.lower() in ['a', 'á' , 'é' 'e', 'i','í' ,'o', 'u', 'ó', 'ö', 'ő', 'ú', 'ü', 'ű']:
        count += 1

print('A szoveg %s karakter hosszu' %len(var))
print('A szovegben %s db maganhangzo szerepel' %count)
