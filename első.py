s1 = 'Teszt Elek'
 # s1 #Syntac Error ezért meg ezért jött)) )
print(s1)
print(s1[0])
print(s1[1])
# s1[0] = 'A'
print(s1[:3])
print(s1[:])
print(s1[-1])
print(s1[:-1])
print(s1[::2])
print(s1[::-1])
print(s1 + 'a nevem')
print(s1 * 10)
print(s1[::-2])
print(s1.upper())
print()
print(s1.upper())
s1 = s1 + " a nevem amit leírok"
print(s1)
print(s1.split())
print(s1.split('e'))
print('Ez egy teszt szöveg berakok valamit ide {}'.format('alma') )
print('Ez egy teszt szöveg berakok valamit ide %s' %'alma')
print('Elso: %s Masodik: %s Harmadik: %s' %('alma','alma2','alma3'))
# print('Elso: {} Masodik: {} Hamradik): {}' .format('alma'))
print('Egy %s' % '\talma')
print('Egy %r' % '\talma')
print('A szam: %s' %4.75)
print('A szam: %d' %4.75)
print('A szam: %f' %4.75123)
print('A szam: %10.1f' %4.75123)
print('Elso: %s Masodik: %6.3f Harmadik: %r' % ('almafa', 1.124567, '\ncitrom'))
print('A szoveg: {} {} {}'.format('alma', 'barack', 'citrom'))
print('A szoveg: {1} {2} {0}'.format('alma', 'barack', 'citrom'))
print('A szoveg: {a} {b} {c}'.format(a='alma', c='barack', b='citrom'))
print('{0:10} I {1} I'.format('Kosar' , 'Mennyiseg'))
print('{0:10} I {1:9} I'.format('Alma',3))
print('{0:10} I {1:9} I'.format('Citrom',1))
print('{0:10} I {1:9} I'.format('Paradicsom',2))
print('-'*50)
print('{0:10} I {1} I {2:}'.format('Kosar' , 'Mennyiseg','Bolt'))
print('{0:10} I {1:^9} I {2}'.format('Alma',3 , 'Tesco'))
print('{0:10} I {1:^9} I {2}'.format('Citrom',1 ,'Spar'))
print('{0:10} I {1:^9} I {2}'.format('Paradicsom', 2, 'Aldi'))

print('{0:=<10} I {1} I {2:+>10}'.format('Kosar' , 'Mennyiseg','Bolt'))
print('{0:=<10} I {1:*^9} I {2:+>10}'.format('Alma',3 , 'Tesco'))
print('{0:=<10} I {1:*^9} I {2:+>10}'.format('Citrom',1 ,'Spar'))
print('{0} I {1:*^9} I {2:+>10}'.format('Paradicsom', 2, 'Aldi'))
print('A szam: {0:10.2f}'.format(12.123456))
nev='\tJakab'
print(f'A nevem {nev!r}')
print(300 == 100)
print( 300 < 500)
lista1 = ['alma' , 'barack' , 12 , True]
print(len(lista1))
print(lista1[0])
print(lista1[1:])
print(lista1 + ['uj elem'])
lista1 = lista1 + ['uj elem']
print(lista1)
lista1.append('citrom')
print(lista1)
pop_valtozo = lista1.pop()
print(pop_valtozo)
print(lista1)
lista1.reverse()
print(lista1)
# lista1.sort()
# print(lista1)
lista1= ['b' , 'a' , 'd', 'c','g' ]
lista1.sort()
print(lista1)

string1 =11
number1 = [1,2,3]

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
matrix = [l1, l2, l3]
print(matrix)
print(matrix[0])
print(matrix[1][1])
string_list = ['alma', 'barack', 'citrom']
print(string_list[2][3:])
print(string_list[2][-3:])

col1 = [cv[0] for cv in matrix]
print(col1)
print('Elso: %s Masodik: %s Harmadik: %s' %('alma','alma2','alma3'))
# print('Elso: {} Masodik: {} Hamradik): {}' .format('alma'))
print('Egy %s' % '\talma')
print('Egy %r' % '\talma')
print('A szam: %s' %4.75)
print('A szam: %d' %4.75)
print('A szam: %f' %4.75123)
print('A szam: %10.1f' %4.75123)
print('Elso: %s Masodik: %6.3f Harmadik: %r' % ('almafa', 1.124567, '\ncitrom'))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
matrix1 = [list1, list2, list3]
print([item[0] for item in [matrix1[cv] for cv in [0 , 2]]])
print('-' * 50)

val = input('Irjon be egy szoveget:')
list1 = list(val)
print(list1)
print('Az elso es az utolso eleme a %s es a %s' %(list1[0], list1[-1]))
print('Az elso es az utolso elem kivetelevel a lista: %s' %list1[1:-1])
print('A listanak %s eleme van' %len(list1))
print('A lista elemei szovegkent:  %s' %''.join(list1))
print('Szokozok menten feldarabolva: %s' %val.split(' '))

