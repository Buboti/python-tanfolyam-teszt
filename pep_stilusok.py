import os
import sys


def long_method_name(variable_one, variable_two,
                     variable_three, variable_four):
    print(variable_two)


userAge = 33
user_age = 33
b = 1
c = 2
a = b + c

total = (b * c) + (a * b) + \
        (a * c) + (a - b) + (b + c)


def fn1():
    import base64  #akkor szabad nem az eljén importálni, ha csak 1 helyen használunk valami importot
    print('')


some_var = True
if some_var == True:
    print('')

#region cimke szoveg
if some_var:
    print('gg')
#endregion

if some_var == None:
    print('ddd')

if not some_var:
    print('fff')

def multiply(x):
    return x * 2

multiply_val = lambda x : x * 2

list1 = [1, 2, 3]
dic1 = {'k1': 'v1'}

name = 'Elek'
age = 33

var = 'Hello' +name + 'kor' + str(age)
var = f'Hello {name} kor:{age}'
var = 'Hello {} kor:{}'.format(name, ag
if some_var: print('gg')

if some_var and list1 and dic1 and var:
    print('gg')

def calculate_sum(a, b):
    """
    Summarize 2 numbers
    Args:
        a (int): first number
        b (int): second number
    Returns:
        int: sum of two numbers
    """
    return a + b

print('pozitiv') if age › 0 else print('negativ')

# TODO: Valamit meg kell csinalni