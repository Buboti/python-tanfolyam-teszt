def kozott_van(a, b ,c):
    if min(a, c) < b < max(a, c):
        print(f"A {b} szam az {a} és {c} kozott van.")
    else:
        print(f"A {b} szam nincs a {a} es {c} kozott")

elso = float(input("Add meg az első számot: "))
masodik = float(input("Add meg a második számot: "))
harmadik = float(input("Add meg a harmadik számot: "))

kozott_van(elso, masodik, harmadik)

#Róbert megoldása:
def check_range(num: int, small_num: int, big_num: int)-> None:
    if num in range(small_num , big_num):
        print('{} szam benne van a tartomanyban: {} es a {} kozott'
              .format(num, small_num, big_num))
    else:
        print('A taromanyon kivul esik!')
check_range(5,2, 7)

def is_in_range(num: int, small_num: int, big_num: int)-> bool:
    """
    Chek number is in the range of (small_num, big_num)
    :param num: The number to check
    :param small_num: The range lowest value
    :param big_num: The range biggest value
    :return: True, if the number is in the range os small_num and big_num
    :raises Value Erros: If the small_num is bigger than the big_num
    """
    if small_num > big_num:
        raise ValueError(f'The small_num {small_num} is bigger than the big_num {big_num}')
    return small_num <= num <= big_num

def display_is_in_range(num: int, small_num: int, big_num: int)-> None:
    if is_in_range(num, small_num, big_num):
        print('{} szam benne van a tartomanyban: {} es a {} kozott'
              .format(num, small_num, big_num))
    else:
        print('A taromanyon kivul esik!')
display_is_in_range(5, 2, 7)