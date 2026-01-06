# szia hogy vagy ma
# m
# ma
# ma
# ma v
# ma va
# ...
# ma vagy hogy szia
var = input('Irjon be egy szoveget: ')
list1 = var.split(' ') # ['szia' , 'hogy' , 'vagy' , ma']
list1.reverse()
string1 = ' '.join(list1)
output = ''
for c in string1:
    output += c
    print(output)

