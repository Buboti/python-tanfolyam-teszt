var = int(input ('Melyik szamnak keressuk a faktorialisat'))
original_value = var
str1 = ''
fac = 1

while var != 0:
    str1 = str1 + str(var) + '*'
    fac = fac * var
    var -= 1

print('A faktorialis a %s szamnak (%s!=%s) az %s' %(original_value, original_value, str1[:-3],fac))