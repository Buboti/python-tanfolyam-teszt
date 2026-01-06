# def fgv_neve(PATAMETER):
#    utasitasok

def first(name):
    """"
    Ez a fgv koszon
    """
    print('Hello ' + name)

first('Botond')
print(first.__doc__)

def second(num):
    if num % 2 == 0:
        return 'Paros szam'
        print('OK')
    return 'Nem paros szam'

print(second(2))
print(second(3))

def third(num):
    return num * num

var1 = lambda num: num * num

print(third(3))
print(var1(3))

print(third.__name__)
print(var1.__name__)

var2 = lambda a,b : a + b
print(var2(1,2))

users = [
    {'username':'elek', 'email':'teszt@elek.hu','orders': ['T1','T2','T3']},
    {'username':'jakab', 'email':'teszt@jakab.hu','orders': []},
    {'username':'feri', 'email':'teszt@feri.hu','orders': []},
    {'username':'pista', 'email':'teszt@pista.hu','orders': ['T4','T5','T6']},
    {'username':'bela', 'email':'teszt@bela.hu','orders': []},
    {'username':'mari', 'email':'teszt@elek.hu','orders': ['T1','T2','T3']}
]

#nincs rendelése?
wo_users= list(filter(lambda u: not u ['orders'], users))
print(wo_users)

wo_users2= [user for user in users if not user ['orders']]
print(wo_users2)

#usernevek nagybetusitese:

user_names = list(map(lambda user : user['username'].upper(), filter(lambda u: not u ['orders'], users)))
print(user_names)

user_names2 = [user['username'].upper() for user in users if not user ['orders']]
print(user_names2)

