var = input('Irjon be egy tetszoleges szamot: ')
parosak = set()
paratlanok = set()
for n in var:
    if n.isnumeric():
        if int(n) %2 == 0:
            parosak.add(n)
        else:
            paratlanok.add(n)
print( 'Paros szamok: ', ", " . join(sorted(parosak)))
print( 'Paratlan szamok: ', ", " . join(sorted(paratlanok)))