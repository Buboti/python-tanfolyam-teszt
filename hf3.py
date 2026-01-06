n = int(input('Melyik szam faktorialisat keresi: '))
fakt = 1
szorz = []
for v in range( 1 , n +1 ):
    fakt = fakt * v
    szorz.append(str(v))
hogy = '*'.join(szorz)
print(f"{n}!: {hogy} : {fakt}")
