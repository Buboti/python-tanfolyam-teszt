print('Be akarok helyettesíteni ebbe a szövegbe valamnit ide{}'.format(' sikerult'))
print('s1: %s , s2: %s , s3: %s' %('alma' , 'sas' , 'hal') )
print(' ide valami %s' %('erdekes behelytetesiets'))
print('Egy %s' % '\tminden amit ideirok')
print('Elso: %s Masodik: %10.5f Harmadik: %r' % ('almafa', 1.124567, '\tcitrom'))

print('{0: <10} I {1} I {2: >10}'.format('Kosar' , 'Mennyiseg','Bolt'))
print('{0: <10} I {1:*^9} I {2: >10}'.format('Alma',3 , 'Tesco'))
print('{0: <10} I {1:*^9} I {2: >10}'.format('Citrom',1 ,'Spar'))
print('{0} I {1:*^9} I {2: >10}'.format('Paradicsom', 2, 'Aldi'))

l1= [1, 3, 6, 9, 3, 2 ,4 , 5, 3, 5]
print(list(l1))
print(list(set(l1)))

p1 = set()
p1.add(1)
print(p1)

a1 = (1, 2, 3)
a2 = (33, 44)
print('a1','a2')

Szavak1 = {'v1':'hallo' , 'v2':'maki'}
print(Szavak1['v1'])
print(Szavak1['v2'])

t1 = (1, 2, 3, 4 , 8)
print(len(t1))

t3 = (50,)
print(t3)